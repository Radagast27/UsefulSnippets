library(RODBC)  
 dbconnection <- odbcDriverConnect('driver={SQL Server};server=.;database=CLARO;trusted_connection=true')  
 initdata <- sqlQuery(dbconnection,paste('SELECT * FROM [CLARO].[dbo].[Fielding];')) 