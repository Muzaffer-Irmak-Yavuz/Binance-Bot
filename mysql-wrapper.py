import mysql.connector


connection = mysql.connector.connect()

sql_select_Query = "select * from links"

cursor = connection.cursor()
cursor.execute(sql_select_Query)
# get all records
records = cursor.fetchall()
print("Total number of rows in table: ", cursor.rowcount)

print("\nPrinting each row")
for row in records:
    print("Link = ", row[0], )
    print("Id = ", row[1])



if connection.is_connected():
    connection.close()
    cursor.close()
    print("MySQL connection is closed")