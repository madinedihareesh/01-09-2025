import sqlite3

conn=sqlite3.connect('univ.db')

cursor=conn.cursor()

data=cursor.execute('select * from students inner join dept on students.deptid=dept.deptid').fetchall()
print(data)
conn.commit()

cursor.close()

conn.close()