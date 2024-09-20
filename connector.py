import mysql.connector as myconn

mydb = myconn.connect(host = "localhost", user = "root", password = "Meet#2806")
db_cursor=mydb.cursor()

db_cursor.execute("create database joinsqlandpy")
print(mydb, "connection establisted....")