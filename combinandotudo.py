import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2481632",
    database='YggdrasilProject'
)
mycursor = mydb.cursor()
csv_data = csv.reader(
    open('/home/hugo/dev/WebCrawlers/yggdrasil/Species/speciesB.csv'))
header = next(csv_data)
print(header)
for row in csv_data:
    print(row)
    sql = "INSERT INTO herbarium_species(name, genus_id) VALUES (%s, %s)"
    mycursor.execute(sql, row)
    mydb.commit()
