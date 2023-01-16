import pandas as pd

def get_cars(conn, idUser):
    return pd.read_sql('''
        SELECT 
            car.*,
            modelcar.idModelCar,
            modelcar.nameModelCar,
            company.idCompany,
            company.nameCompany,
            bodytypecar.nameBodyTypeCar,
            drivetrain.nameDrivetrain,
            transmission.nameTransmission,
            userCar.idUserCar
        FROM 
            car
            JOIN modelcar ON idModelCar == modelCar_idModelCar
            JOIN company ON idCompany == company_idCompany
            JOIN bodytypecar ON idBodyTypeCar == bodyTypeCar_idBodyTypeCar
            JOIN drivetrain ON idDrivetrain == drivetrain_idDrivetrain
            JOIN transmission ON idTransmission == transmission_idTransmission
            JOIN userCar ON car_idCar == idCar
        WHERE 
            user_idUser == :idUser
        ''', conn, params={"idUser": idUser})

def get_base64img(conn, idCar):
    return pd.read_sql('''
        SELECT 
            car.base64img
        FROM 
            car
        WHERE 
            idCar == :idCar
        ''', conn, params={"idCar": idCar})

def edit_car(conn, idCar, model, transmission, drivetrain, bodytypecar, releaseYear, horsepowers, mileage, base64img):
    query = '''
        UPDATE car
        SET modelCar_idModelCar = :model, bodyTypeCar_idBodyTypeCar = :bodytypecar, drivetrain_idDrivetrain = :drivetrain, transmission_idTransmission = :transmission,
            mileageCar = :mileage, releaseYearCar = :releaseYear, horsepowers = :horsepowers, base64img = :base64img
        WHERE idCar == :idCar
    '''

    cur = conn.cursor()
    cur.execute(query, 
                    {"idCar" : idCar,
                    "model" : model,
                    "transmission" : transmission, 
                    "drivetrain" : drivetrain,
                    "bodytypecar" : bodytypecar,
                    "releaseYear" : releaseYear,
                    "horsepowers" : horsepowers,
                    "mileage" : mileage,
                    "base64img" : base64img})
    conn.commit()

def get_userCarId(conn, idUser, idCar):
    return pd.read_sql('''
        SELECT idUserCar 
        FROM userCar 
        WHERE user_idUser == :idUser AND car_idCar == :idCar
    ''', conn, params={"idUser" : idUser, "idCar" : idCar})

def remove_car(conn, idCar):
    query = '''
        DELETE FROM car
        WHERE idCar == :idCar
        '''

    cur = conn.cursor()
    cur.execute(query, {"idCar" : idCar})
    conn.commit()

def remove_usercar(conn, usercarId):
    query = '''
        DELETE FROM userCar
        WHERE idUserCar == :usercarId
        '''

    cur = conn.cursor()
    cur.execute(query, {"usercarId" : usercarId})
    conn.commit()

def remove_advertisment(conn, usercarId):
    query = '''
        DELETE FROM advertisment
        WHERE userCar_idUserCar == :usercarId
        '''

    cur = conn.cursor()
    cur.execute(query, {"usercarId" : usercarId})
    conn.commit()