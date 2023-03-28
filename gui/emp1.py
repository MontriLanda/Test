import mysql.connector
conn = mysql.connector.connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "toyo"
)
cursor=conn.cursor()
add_emp = "insert into employee values ('','supot','store','25000')"
cursor.execute(add_emp)
conn.commit()
conn.close()