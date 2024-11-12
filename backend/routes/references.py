# backend/routes/references.py
from fastapi import APIRouter, HTTPException
from backend.db.database import get_db_connection

router = APIRouter()

@router.get("/db-table/{table_name}")
def get_table_data(table_name: str):
    try:
        # Подключаемся к базе данных через функцию get_db_connection
        connection = get_db_connection()
        
        with connection.cursor() as cursor:
            # Проверяем, существует ли таблица
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]
            
            if table_name not in tables:
                return {"status": "error", "message": f"Table '{table_name}' not found in the database"}
            
            # Выполняем запрос для получения данных из указанной таблицы
            query = f"SELECT * FROM `{table_name}`"  # Экранируем имя таблицы для безопасности
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]  # Получаем имена столбцов

        connection.close()
        
        # Преобразуем данные в список словарей, где ключи — это имена столбцов
        table_data = [dict(zip(columns, row)) for row in rows]
        
        return {"status": "success", "data": table_data}
    
    except Exception as e:
        print(f"Error retrieving data from table '{table_name}': {e}")
        return {"status": "error", "message": str(e)}
