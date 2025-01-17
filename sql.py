import sqlite3

connection=sqlite3.connect("student.db")
cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT); 

"""
cursor.execute(table_info)

cursor.execute('''Insert into STUDENT values("Vishnudeep Panicker","Data Science","A",100)''')
cursor.execute('''Insert into STUDENT values("Rajshree Gosal","Data Science","A",30)''')
cursor.execute('''Insert into STUDENT values("Vicky","Data Science","A",90)''')
cursor.execute('''Insert into STUDENT values("Sreekanth Changaroth","Data Science","A",100)''')
cursor.execute('''Insert into STUDENT values("Chittaranjan Das","Data Science","A",40)''')
cursor.execute('''Insert into STUDENT values("Rahul verma","Data Science","B",90)''')

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close()
