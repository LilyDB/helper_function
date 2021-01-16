import os
import urllib
import pandas as pd
import datetime
from sqlalchemy import create_engine


def getdf_sqlserver(server_alias,database_name,query):
    params = urllib.parse.quote_plus(
            'DRIVER={SQL Server};\
            SERVER='+server_alias+';\
            DATABASE='+database_name+';\
            Trusted_Connection=True')
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
    df = pd.read_sql_query(query,engine)
    engine.dispose()
    return df

def pushdf_sqlserver(server_alias,database_name,schema,table,if_exists,df):
    params = urllib.parse.quote_plus(
            'DRIVER={SQL Server};\
            SERVER='+server_alias+';\
            DATABASE='+database_name+';\
            Trusted_Connection=True')
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
    engine.connect()
    df.reset_index(inplace=True)
    df.to_sql(name=table, schema=schema, con=engine, index=False, if_exists=if_exists)
    engine.dispose()
    print("done")
