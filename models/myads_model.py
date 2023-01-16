import pandas as pd

def get_active_advertisments_full(conn, idUser):
    return pd.read_sql('''
        SELECT 
            car.*,
            modelcar.nameModelCar,
            company.nameCompany,
            bodytypecar.nameBodyTypeCar,
            drivetrain.nameDrivetrain,
            transmission.nameTransmission,
            userCar.idUserCar,
            advertisment.advertisment_id,
            advertisment.carPrice,
            advertisment.description,
            advertisment.startDateTime,
            advertisment.endDateTime,
            city.nameCity,
            city.idCity
        FROM
            car
            JOIN modelcar ON idModelCar == modelCar_idModelCar
            JOIN company ON idCompany == company_idCompany
            JOIN bodytypecar ON idBodyTypeCar == bodyTypeCar_idBodyTypeCar
            JOIN drivetrain ON idDrivetrain == drivetrain_idDrivetrain
            JOIN transmission ON idTransmission == transmission_idTransmission
            JOIN userCar ON car_idCar == idCar
            JOIN advertisment ON userCar_idUserCar == idUserCar
            JOIN city ON idCity == city_idCity
        WHERE 
            user_idUser == :idUser and advertisment.endDateTime IS NULL
        ORDER BY advertisment.endDateTime DESC
        ''', conn, params={"idUser": idUser})

def get_nonactive_advertisments_full(conn, idUser):
    return pd.read_sql('''
        SELECT 
            car.*,
            modelcar.nameModelCar,
            company.nameCompany,
            bodytypecar.nameBodyTypeCar,
            drivetrain.nameDrivetrain,
            transmission.nameTransmission,
            userCar.idUserCar,
            advertisment.advertisment_id,
            advertisment.carPrice,
            advertisment.description,
            advertisment.startDateTime,
            advertisment.endDateTime,
            city.nameCity,
            city.idCity
        FROM 
            car
            JOIN modelcar ON idModelCar == modelCar_idModelCar
            JOIN company ON idCompany == company_idCompany
            JOIN bodytypecar ON idBodyTypeCar == bodyTypeCar_idBodyTypeCar
            JOIN drivetrain ON idDrivetrain == drivetrain_idDrivetrain
            JOIN transmission ON idTransmission == transmission_idTransmission
            JOIN userCar ON car_idCar == idCar
            JOIN advertisment ON userCar_idUserCar == idUserCar
            JOIN city ON idCity == city_idCity
        WHERE 
            user_idUser == :idUser AND advertisment.endDateTime IS NOT NULL
        ORDER BY advertisment.endDateTime DESC
        ''', conn, params={"idUser": idUser})

def get_advertisments(conn, idUser):
    return pd.read_sql('''
        SELECT
            *
        FROM
            advertisment
        JOIN userCar ON idUserCar == userCar_idUserCar
        WHERE 
            user_idUser == :idUser
    ''', conn, params={"idUser": idUser})

def get_cars(conn, idUser):
    return pd.read_sql('''
        SELECT
            *
        FROM
            car
        JOIN userCar ON car_idCar == idCar
        WHERE 
            user_idUser == :idUser
    ''', conn, params={"idUser": idUser})

def advertisments_cars_except(conn, idUser):
    return pd.read_sql('''
        SELECT
            car.*,
            modelcar.nameModelCar,
            company.nameCompany
        FROM
            (SELECT userCar.car_idCar
            FROM car
            JOIN userCar ON car_idCar == idCar
            WHERE user_idUser == :idUser
            EXCEPT
            SELECT userCar.car_idCar
            FROM advertisment
            JOIN userCar ON idUserCar == userCar_idUserCar
            WHERE user_idUser == :idUser and advertisment.endDateTime IS NULL)
        JOIN car ON idCar == car_idCar
        JOIN modelcar ON idModelCar == modelCar_idModelCar
        JOIN company ON idCompany == company_idCompany
    ''', conn, params={"idUser": idUser})

def get_userCarId(conn, idUser, idCar,):
    return pd.read_sql('''
        SELECT idUserCar 
        FROM userCar 
        WHERE user_idUser == :idUser AND car_idCar == :idCar
    ''', conn, params={"idUser" : idUser, "idCar" : idCar})

def add_advertisment(conn, idUserCar, idCity, price, desc):
    query = '''
        INSERT INTO advertisment(userCar_idUserCar, carPrice, description, city_idCity, startDateTime) VALUES
        (:idUserCar, :price, :desc, :idCity, DATE());
        '''

    cur = conn.cursor()
    cur.execute(query, {"idUserCar" : idUserCar, "idCity" : idCity, "price" : price, "desc" : desc})
    conn.commit()