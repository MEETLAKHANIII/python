import mysql.connector as myconn

mydb = myconn.connect(host = "localhost", user = "root", password = "Meet#2806", database = "joinsqlandpy")
db_cursor=mydb.cursor()
db_deletedata="delete from joinsqlandpy.Emp where Ename=%s"
db_value=("pratham",)
db_cursor.execute(db_deletedata,db_value)
mydb.commit()

print(db_cursor.rowcount,"Record deleted.")