import mysql.connector
#we need to connect host,user,password
mydb=mysql.connector.connect(host="localhost",user='root',password='chitra123')
#check whether object is created
print(mydb)
#create database into it
mycurser=mydb.cursor()#curser method is used to perform query operation
# mycurser.execute("CREATE DATABASE Mydb_python")#execute method in curser is used to create db**sql query is create databases
# mycurser.execute("show databases")#to see the list of database **sql query is "show database"
# for x in mycurser:
#     print(x)

"""
Information_schema contains metadata about databases in mysql. For e.g. names of tables,columns in a database etc. 
performance_schema is for monitoring MySQL Server execution at a low level. 
The performance_schema is intended to provide access to useful information about server execution
"""
#create table
mycurser.execute("USE Mydb_python")
# #mycurser.execute("create table Employee(Name varchar(50),Dept varchar(50),salary int)")
# mycurser.execute("create table TEST(Name varchar(250),Dept varchar(200),salary int)")
#print table
# mycurser.execute("show tables")
# for x in mycurser:
#     print(x)
# sql="insert into Employee Values('Chitra','Python',50000)"
# # #to save contents in table use commit
# mycurser.execute(sql)
# mydb.commit()
# print(mycurser.rowcount,"record inserted")
#insert multiple valus to table
# sql="insert into Employee(Name,Dept,salary)values(%s,%s,%s)"
# val=[
#     ('Aathira','python',51000),
#     ('Sibin','python',60000),
#     ('Degish','python',80000)
# ]
# mycurser.executemany(sql,val)
# mydb.commit()
# print(mycurser.rowcount,"record inserted")
# mycurser.execute("show tables")
#fetch record values
# mycurser.execute("select* from employee")
# myresult=mycurser.fetchall()
# # for x in myresult:
# #     print(x)
# print(myresult)
# mycurser.execute(" DELETE FROM employee where Name= 'Sibin'")
# mydb.commit()
#print(mycurser.rowcount,"record deleted")
# mycurser.execute("Update  employee set salary=95000 where Name='Degish'")
# mydb.commit()
# mycurser.execute("select Name from employee order by Name asc")
# mydb.commit()
# mycurser.execute("select distinct Name from employee")
# mydb.commit()
# print(mycurser.rowcount,"record distinct")