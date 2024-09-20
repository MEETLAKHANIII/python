import mysql.connector as myconn

mydb = myconn.connect(host = "localhost", user = "root", password = "Meet#2806", database = "joinsqlandpy")
db_cursor=mydb.cursor()
db_insert="insert into Emp(Roll,Ename) values(%s,%s)"
db_list=[(2,"Meet"),(3,"Pratham"),(4,"jay"),(5,"jay"),(6,"sahil"),(6,"rohit")]
db_cursor.executemany(db_insert,db_list)
mydb.commit()
print(db_cursor.rowcount, "Recode inserted")
