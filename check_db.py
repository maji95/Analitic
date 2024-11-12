import pymysql

DB_HOST = "127.0.0.1"
DB_USER = "manager"
DB_PASSWORD = "admin"
DB_NAME = "clinic_management"

def create_connection():
    """Создает соединение с MySQL и выводит таблицы"""
    try:
        print("Попытка подключения к базе данных...")
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        print("Соединение установлено.")
        
        with connection.cursor() as cursor:
            # Выполняем запрос на получение таблиц
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            print("Список таблиц в базе данных:")
            for table in tables:
                print(table[0])  # Печатаем имя таблицы

        connection.close()  # Закрываем соединение
    except pymysql.MySQLError as e:
        print(f"Ошибка подключения: {e}")

if __name__ == "__main__":
    create_connection()
