import mysql.connector as myconn

mydb = myconn.connect(host = "localhost", user = "root", password = "Meet#2806", database = "joinsqlandpy")
db_cursor=mydb.cursor()
db_cursor.execute("show tables")
for i in db_cursor:
    print(i)
print("Table created!")
