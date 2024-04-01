import mysql.connector


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='nhl_test')

cursor = connection.cursor()
cursor.execute("SELECT id FROM teams")
for x in cursor:
    print(x[0])

