from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import unquote
from backend.db_config import get_db_connection, DB_NAME
from backend.mappings import TABLE_MAPPING, COLUMN_MAPPING

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def format_data(data, button_name, available_columns):
    formatted_data = []
    # Для страховых таблиц всегда используем doctor_name
    if button_name in ["Oftalmologie_Insurance", "Traumatologie_Insurance"]:
        for row in data:
            formatted_row = {
                # Принудительно используем doctor_name без маппинга
                "doctor_name": row["doctor_name"]  
            }
            # Добавляем месячные данные
            for month in ["January", "February", "March", "April", "May", "June", 
                         "July", "August", "September", "October", "November", "December"]:
                formatted_row[month] = row.get(month, 0) if month in available_columns else 0
            formatted_data.append(formatted_row)
        return formatted_data

    # Для остальных таблиц используем маппинг как раньше
    mapping = COLUMN_MAPPING.get(button_name, {})
    first_column_key = mapping.get("doctor_name", "doctor_name")
    
    for row in data:
        formatted_row = {}
        if first_column_key in row and first_column_key in available_columns:
            formatted_row[first_column_key] = row[first_column_key]
        else:
            formatted_row[first_column_key] = "Unknown"
        
        for month in ["January", "February", "March", "April", "May", "June",
                     "July", "August", "September", "October", "November", "December"]:
            formatted_row[month] = row.get(month, 0) if month in available_columns else 0
        formatted_data.append(formatted_row)
    
    return formatted_data



@app.get("/db-table/{button_name}")
def get_table_data(button_name: str):
    try:
        decoded_button_name = unquote(button_name)
        table_name = TABLE_MAPPING.get(decoded_button_name)
        if not table_name:
            raise HTTPException(status_code=404, detail=f"No table mapping found for button '{decoded_button_name}'")

        connection = get_db_connection()
        with connection.cursor() as cursor:
            # Выполняем запрос, чтобы получить информацию о колонках таблицы
            cursor.execute(f"SHOW COLUMNS FROM `{table_name}`")
            columns_info = cursor.fetchall()
            available_columns = [column['Field'] for column in columns_info]

            # Выполняем запрос, чтобы получить данные из таблицы
            cursor.execute(f"SELECT * FROM `{table_name}`")
            rows = cursor.fetchall()

        connection.close()

        # Форматируем данные с учетом доступных колонок
        formatted_data = format_data(rows, decoded_button_name, available_columns)
        return {"status": "success", "data": formatted_data}

    except Exception as e:
        return {"status": "error", "message": str(e)}
