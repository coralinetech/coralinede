# import library
import os
import pandas as pd
import coralinede as cde
from sqlalchemy import create_engine

# set file name and file paths
file_name = ''
file_path = os.path.join('/home/user/', file_name)

# set schema name and table name to save DataFrame as a table
schema_name = ''
table_name = ''

# set database credential
DB_HOST = ''
DB_PORT = ''
DB_USER = ''
DB_PASSWORD = ''

# get simplified column name and detect delimiter 
arr_header, delimiter = cde.get_clean_col_and_delimiter(file_path)

# use pandas to read csv
df = pd.read_csv(file_path, sep=delimiter)

# assign new column name to DataFrame
df.columns = arr_header

# generate dictionary of SQLAlchemy (data type and data length)
dtype_dict = cde.get_datatype_each_col(df)

# initialize database connection
connection_string = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, schema_name)
engine = create_engine(connection_string)

# save DataFrame as a table in Database
df.to_sql(name=table_name, con=engine, index=False, if_exists='append', dtype=dtype_dict)