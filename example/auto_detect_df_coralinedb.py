# please install coralinedb first
# using pip install coralinedb
# ----------------------------------------

# import library
import os
import pandas as pd
import coralinedb as cdb
import coralinede as cde

# set file name and file paths
file_name = ''
file_path = os.path.join('/home/user/', file_name)

# set schema name and table name to save DataFrame as a table
schema_name = ''
table_name = ''

# set database credential
DB_HOST = ''
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
sql_db = cdb.MySQLDB(DB_HOST, DB_USER, DB_PASSWORD)

# save DataFrame as a table in Database
sql_db.save_table(df, schema_name, table_name, if_exists='append', dtype=dtype_dict)