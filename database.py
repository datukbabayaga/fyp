import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="", database="")

if connection.is_connected():
    print('COnnected Successfully')

else:
    print('failed')

connection.close()