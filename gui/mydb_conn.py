import mysql.connector
conn = mysql.connector.connect(user = "root", 
password = "",
host = "127.0.0.1",
database = "toyo",)
conn.close()