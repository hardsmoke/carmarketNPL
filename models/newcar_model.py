def add_car(conn, idModel, idBodyTypeCar, idDrivetrain, idTransmission, horsepowers, releaseYear, mileage, base64img):
    query = '''
        INSERT INTO car(modelcar_idModelCar, bodyTypeCar_idBodyTypeCar, drivetrain_idDrivetrain, transmission_idTransmission, horsepowers, releaseYearCar, mileageCar, base64img) VALUES
        (:idModel, :idBodyTypeCar, :idDrivetrain, :idTransmission, :horsepowers, :releaseYear, :mileage, :base64img);
        '''

    cur = conn.cursor()
    cur.execute(query, {"idModel" : idModel,
                        "idTransmission" : idTransmission,
                        "idDrivetrain" : idDrivetrain,
                        "idBodyTypeCar" : idBodyTypeCar,
                        "releaseYear" : releaseYear,
                        "mileage" : mileage,
                        "horsepowers" : horsepowers,
                        "base64img" : base64img})
    conn.commit()

    return cur.lastrowid

def add_usercar(conn, idCar, idUser):
    query = '''
    INSERT INTO usercar(car_idCar, user_idUser) VALUES
    (:idCar, :idUser);
    '''

    cur = conn.cursor()
    cur.execute(query, {"idCar" : idCar, "idUser" : idUser})
    conn.commit()