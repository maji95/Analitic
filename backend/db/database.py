# backend/db/database.py
import pymysql

# Настройки подключения к базе данных
DB_HOST = "127.0.0.1"
DB_USER = "manager"
DB_PASSWORD = "admin"
DB_NAME = "clinic_management"

def get_db_connection():
    """Функция для подключения к базе данных."""
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
