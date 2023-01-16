import pandas as pd

def get_user(conn, phoneUser, password):
    return pd.read_sql('''
        SELECT *
        FROM user
        WHERE phoneUser == :phoneUser AND passwordUser == :password
        ''', conn, params={"phoneUser": phoneUser, "password": password})