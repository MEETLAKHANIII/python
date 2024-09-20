import mysql.connector as myconn

mydb = myconn.connect(host = "localhost", user = "root", password = "Meet#2806", database = "joinsqlandpy")
db_cursor=mydb.cursor()
db_Updatedata="update joinsqlandpy.Emp set roll=%s where Ename=%s"
db_value=(7,"rohit")

db_cursor.execute(db_Updatedata,db_value)
mydb.commit()
print(db_cursor.rowcount,"Data updated")