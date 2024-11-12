import pymysql

# Настройки подключения к базе данных
DB_HOST = "192.168.101.70"
DB_USER = "manager_new"
DB_PASSWORD = "admin"
DB_NAME = "clinic_management"

# Функция для подключения к базе данных
def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )
