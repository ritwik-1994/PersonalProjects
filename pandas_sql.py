import pandas.io 
import sql
import sqlite3

conn = sqlite3.connect('/home/shipsy/Downloads/Final Zajil SQL Format.sql')
query = "Select * from shipment where cod_amount = 42.00;"
results = sql.red_sql(query, con = conn)
reasults.head()
