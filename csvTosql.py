import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2481632",
    database='covid'
)

mycursor = mydb.cursor()
csv_data = open('/home/hugo/Documents/sql/result_interno.csv')
header = next(csv_data).replace('\n', '').replace('\t', ',')

times = '%s'

for _ in range(len(header.split(','))-1):
    times += ",%s"

for row in csv_data:
    row = row.replace('\n', '').split('\t')
    for i in range(len(row)):
        if(row[i] == "NULL" or row[i] == "Null"):
            row[i] = None

    sql = f"INSERT INTO casos_dados_internos_por_semana({header}) VALUES ({times})"
    
    mycursor.execute(sql, row)
    mydb.commit()
