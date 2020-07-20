# SQLAlchemy Data Type Generator
> This library is the SQLAlchemy Data Type and Data Length Generator from Pandas DataFrame.
---
## How to use
### Import this library 
```
   import coralinede as cde 
```
### Detect Delimiter and Get Simplified Column Name 
```
    arr_header, delimiter = cde.get_clean_col_and_delimiter(file_path)
```
### Generate Dictionary of SQLAlchemy from Pandas DataFrame
```
    dtype_dict = cde.get_datatype_each_col(df)
```
---
## Example Usages
1. usage with coralinedb - coralinede/example/auto_detect_df_coralinedb.py
1. usage with sqlalchemy - coralinede/example/auto_detect_df_sqlalchemy.py