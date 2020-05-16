import mysql.connector as mysql ;

conn = mysql.connect(host='localhost',database='mydbs',user='root',password='testrun')

if conn.is_connected():
    print("connected to mysql db")

cursor= conn.cursor()
cursor.execute('use classicmodels')
#cursor.execute('select * from customers')
cursor.execute('''SELECT DISTINCT
    state
FROM
    customers
WHERE
    state IS NOT NULL
LIMIT 5;''')

'''row= cursor.fetchone()'''

'''while row is not None:
    print(row)
    row=cursor.fetchone()'''

rows = cursor.fetchall()
print("total no of records ",cursor.rowcount)

for row in rows:
    print(row)


cursor.close()

conn.close()