import mysql.connector

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = "password"
DB_NAME = "mia_azienda_db"

db = mysql.connector.connect(
    host= "localhost",
    port=3306,
    user="root",
    password= "password"
)

cursor = db.cursor()
cursor.execute(f"create database if not exists `{DB_NAME}`")
print("Connesso a MySQL:", db.is_connected())

db.database = DB_NAME


cursor.execute("Show tables")
print(cursor.fetchall())