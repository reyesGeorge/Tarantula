import pandas as pd
from sqlalchemy import create_engine

USER = 'user'
PASS = 'pass'
HOST = 'pg'
PORT = '5432'
DB = 'legalist'


db_string = f"postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}"

engine = create_engine(db_string)

df = pd.read_sql_query("SELECT * FROM items WHERE spider = 'Scroll'",
                       con=engine)
print("DB QUERY for Scroll Spider")
print(df.tail(5))

