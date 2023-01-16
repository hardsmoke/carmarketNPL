import pandas as pd

def get_advertisments(conn, userId):
    return pd.read_sql('''
        SELECT 
            advertisment.*,
            userCar.user_idUser
        FROM
            advertisment
        JOIN userCar ON idUserCar == userCar_idUserCar
        WHERE user_idUser == :userId
    ''', conn, params={"userId" : userId})
    
def remove_advertisment(conn, advertisment_id):
    query = '''
        UPDATE advertisment
        SET endDateTime = DATETIME()
        WHERE advertisment_id == :advertisment_id
        '''

    cur = conn.cursor()
    cur.execute(query, {"advertisment_id" : advertisment_id})
    conn.commit()