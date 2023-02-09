#from sqlalchemy import sql
#from openpyxl import Workbook
import pypyodbc

db_host = '10.245.1.82'
db_name = 'BitStream'
db_user = 'admin'
db_password = 'DB@Admin123789'
connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'
db = pypyodbc.connect(connection_string)
if db.connection is None:
    print("Cannot connect to DB")
sql
