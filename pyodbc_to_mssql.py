import pyodbc

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=WideWorldImporters;UID=UserID;PWD=YourPassword')
cursor = cnxn.cursor()
cursor.execute("SELECT TOP (100) Comments, count(*) FROM WideWorldImporters.Sales.Orders GROUP BY Comments")
row = cursor.fetchone() 
while row: 
    print(row[0] + ': ' + str(row[1]))
    row = cursor.fetchone()
