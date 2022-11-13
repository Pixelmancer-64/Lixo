import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2481632",
    database='YggdrasilProject'
)

mycursor = mydb.cursor()
csv_data = csv.reader(open('/home/hugo/Documents/GENERA/GENUS.csv'))
header = next(csv_data)
print(header)
for row in csv_data:
    print(row[2])
    sql = "INSERT INTO herbarium_genus(name, family_id) VALUES (%s, %s)"
    mycursor.execute(sql, (row[1], row[2]))
    mydb.commit()
