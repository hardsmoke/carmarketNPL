import pandas as pd

def get_user(conn, phoneUser):
    return pd.read_sql('''
        SELECT *
        FROM user
        WHERE phoneUser = :phoneUser
        ''', conn, params={"phoneUser": phoneUser})

def add_user(conn, phoneUser, passwordUser, nameUser, surnameUser):
    query = '''
        INSERT INTO user(phoneUser, passwordUser, nameUser, surnameUser) VALUES
        (:phoneUser, :passwordUser, :nameUser, :surnameUser);
        '''

    cur = conn.cursor()
    cur.execute(query, {"phoneUser" : phoneUser, "passwordUser" : passwordUser, "nameUser" : nameUser, "surnameUser" : surnameUser})
    conn.commit()