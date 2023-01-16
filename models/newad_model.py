import pandas as pd

def get_userCarId(conn, idUser, idCar):
    return pd.read_sql('''
        SELECT idUserCar 
        FROM userCar 
        WHERE user_idUser == :idUser AND car_idCar == :idCar
    ''', conn, params={"idUser" : idUser, "idCar" : idCar})

def add_advertisment(conn, idUserCar, idCity, price, desc):
    query = '''
        INSERT INTO advertisment(userCar_idUserCar, carPrice, description, city_idCity, startDateTime) VALUES
        (:idUserCar, :price, :desc, :idCity, DATETIME());
        '''

    cur = conn.cursor()
    cur.execute(query, {"idUserCar" : idUserCar, "idCity" : idCity, "price" : price, "desc" : desc})
    conn.commit()