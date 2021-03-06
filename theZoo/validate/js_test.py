import pandas as pd
from sqlalchemy import create_engine

USER = 'user'
PASS = 'pass'
HOST = 'pg'
PORT = '5432'
DB = 'gtest'


db_string = f"postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}"

engine = create_engine(db_string)

df = pd.read_sql_query("SELECT * FROM items WHERE spider = 'JS'",
                       con=engine)

print("DB QUERY for JS Spider")
print(df.tail(5))

