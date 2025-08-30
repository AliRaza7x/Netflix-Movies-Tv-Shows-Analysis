import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/netflix_titles.csv")

username = "root"
password = "0007"
host = "localhost"
port = "3306"
database = "netflix_db"

engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}")

df.to_sql("netflix_titles", engine, if_exists="replace", index=False)

print("✅ Data loaded into MySQL DB: netflix_db ")
