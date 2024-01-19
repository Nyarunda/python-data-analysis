import pandas as pd
import pyodbc 
from sqlalchemy.engine import URL
from sqlalchemy import create_engine

""""connection_string = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=localhost;"
                      "Database=Strategic;"
                      "UID=ezra;"
                      "PWD=07Nyarunda;"
                      "schema=Strategic;") """

connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=Strategic;UID=ezra;PWD=07Nyarunda"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
print(connection_string)


print(connection_url)

engine = create_engine(connection_url)

print(engine)

files = ['artist','canvas_size','image_link','museum','museum_hours','product_size','subject','work']

for file in files:
    df = pd.read_csv(f'C:/Users/Ezra/Documents/Data Analysis/archive/{file}.csv')
    insert = df.to_sql(file,con=engine,if_exists='replace',index=False)

print(df.info)