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
#print(connection_string)


#print(connection_url)

engine = create_engine(connection_url)

#print(engine)

df = pd.read_csv('C:/Users/Ezra/Documents/Data Analysis/archive/artist.csv')

insert = df.to_sql('artist',con=engine,if_exists='replace',index=False)

#print(df.info)