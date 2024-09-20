import mysql.connector as myconn

mydb = myconn.connect(host = "localhost", user = "root", password = "Meet#2806", database = "joinsqlandpy")
db_cursor=mydb.cursor()

db_cursor.execute("select * from joinsqlandpy.Emp")

for db_data in db_cursor.fetchall():
    print(db_data)