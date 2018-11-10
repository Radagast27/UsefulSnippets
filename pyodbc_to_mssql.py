import pyodbc

cnxn = pyodbc.connect('driver={SQL Server};server=.;database=CLARO;trusted_connection=true')
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM [CLARO].[dbo].[Fielding];')
row = cursor.fetchone() 
while row: 
    print(row[0] + ': ' + str(row[1]))
    row = cursor.fetchone()
