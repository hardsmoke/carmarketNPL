import pandas as pd

def get_cars(conn):
    return pd.read_sql('''
        SELECT 
            car.*,
            nameCompany,
            nameModelCar
        FROM car
        JOIN modelcar ON modelcar_idModelCar == modelcar.idModelCar
        JOIN company ON company_idCompany == company.idCompany
        ''', conn)

def set_image_to_car(conn, carId, base64):
    query = '''
        UPDATE car
        SET base64img = :base64
        WHERE idCar == :carId
    '''

    cur = conn.cursor()
    cur.execute(query, {"carId" : carId, "base64" : base64})
    conn.commit()

def get_all_companies(conn):
    return pd.read_sql('''
        SELECT 
            nameCompany
        FROM
            company
    ''', conn)

def get_all_models(conn):
    return pd.read_sql('''
        SELECT 
            *
        FROM
            modelcar
    ''', conn)

def get_models(conn, company_id):
    return pd.read_sql('''
        SELECT 
            *
        FROM
            modelcar
        WHERE
            company_idCompany == :company_id
    ''', conn, params={"company_id" : company_id}) 

def get_all_transmissions(conn):
    return pd.read_sql('''
        SELECT 
            nameTransmission
        FROM
            transmission
    ''', conn)

def get_all_bodytypes(conn):
    return pd.read_sql('''
        SELECT 
            nameBodyTypeCar
        FROM
            bodytypecar
    ''', conn)

def get_all_drivetrains(conn):
    return pd.read_sql('''
        SELECT 
            nameDrivetrain
        FROM
            drivetrain
    ''', conn)

def get_all_cities(conn):
    return pd.read_sql('''
        SELECT 
            nameCity
        FROM
            city
    ''', conn)

def get_advertisments(conn, company, model, transmission, price_from, price_to, releaseYear_from, releaseYear_to, milleage_to):
    return pd.read_sql('''
        SELECT 
            *
        FROM
            car
    ''', conn, params={"company": company, 
                        "model": model, 
                        "transmission": transmission, 
                        "price_from": price_from, "price_to": price_to, 
                        "releaseYear_from": releaseYear_from, "releaseYear_to": releaseYear_to, 
                        "milleage_to": milleage_to})

def get_all_active_advertisments(conn):
    return pd.read_sql('''
        SELECT 
            advertisment.*,
            userCar.car_idCar,
            userCar.user_idUser,
            car.mileageCar,
            car.releaseYearCar,
            car.horsepowers,
            car.bodyTypeCar_idBodyTypeCar,
            car.drivetrain_idDrivetrain,
            car.transmission_idTransmission,
            car.base64img,
            company.idCompany,
            company.nameCompany,
            modelcar.idModelCar,
            modelcar.nameModelCar,
            bodytypecar.nameBodyTypeCar,
            drivetrain.nameDrivetrain,
            transmission.nameTransmission,
            city.nameCity,
            user.nameUser,
            user.surnameUser,
            user.phoneUser
        FROM
            advertisment
        JOIN userCar ON idUserCar == userCar_idUserCar
        JOIN car ON idCar == car_idCar
        JOIN modelcar ON idModelCar == modelcar_idModelCar
        JOIN company ON idCompany == company_idCompany
        JOIN city ON city_idCity == idCity
        JOIN bodytypecar ON bodyTypeCar_idBodyTypeCar == idBodyTypeCar
        JOIN drivetrain ON idDrivetrain == car.drivetrain_idDrivetrain
        JOIN transmission ON idTransmission == transmission_idTransmission
        JOIN user ON idUser == user_idUser 
        WHERE endDateTime IS NULL
    ''', conn)

def filterByCompany(conn, df, company_id):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = '''
        SELECT
            *
        FROM
            advertisment_filtered
        WHERE idCompany == :company_id
    '''

    return pd.read_sql(query, conn, params={"company_id": company_id})

def filterByModel(conn, df, model_id):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        WHERE idModelCar == {model_id}
    '''

    return pd.read_sql(query, conn)

def filterByTransmission(conn, df, transmission_id):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        WHERE transmission_idTransmission == {transmission_id}
    '''

    return pd.read_sql(query, conn)

def filterByBodyType(conn, df, bodytype_id):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        WHERE bodyTypeCar_idBodyTypeCar == {bodytype_id}
    '''

    return pd.read_sql(query, conn)

def filterByDrivetrain(conn, df, drivetrain_id):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        WHERE drivetrain_idDrivetrain == {drivetrain_id}
    '''

    return pd.read_sql(query, conn)

def filterByCity(conn, df, city_id):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        WHERE city_idCity == {city_id}
    '''

    return pd.read_sql(query, conn)

def filterByPriceFrom(conn, df, price_from):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        WHERE carPrice >= {price_from}
    '''

    return pd.read_sql(query, conn)

def filterByPriceTo(conn, df, price_to):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        WHERE carPrice <= {price_to}
    '''

    return pd.read_sql(query, conn)

def filterByReleaseYearFrom(conn, df, releaseYear_from):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        WHERE releaseYearCar >= {releaseYear_from}
    '''

    return pd.read_sql(query, conn)

def filterByReleaseYearTo(conn, df, releaseYear_to):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        WHERE releaseYearCar <= {releaseYear_to}
    '''

    return pd.read_sql(query, conn)

def filterByMileage(conn, df, mileage_to):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        WHERE mileageCar <= {mileage_to}
    '''

    return pd.read_sql(query, conn)

def sortByDate_new(conn, df):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        ORDER BY startDateTime DESC
    '''

    return pd.read_sql(query, conn)

def sortByDate_old(conn, df):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        ORDER BY startDateTime ASC
    '''

    return pd.read_sql(query, conn)

def sortByPrice_low(conn, df):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        ORDER BY carPrice ASC
    '''

    return pd.read_sql(query, conn)

def sortByPrice_high(conn, df):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        ORDER BY carPrice DESC
    '''

    return pd.read_sql(query, conn)

def sortByMileage_low(conn, df):
    df.to_sql(con=conn, name='advertisment_filtered', if_exists='replace', index=False)

    query = f'''
        SELECT
            *
        FROM
            advertisment_filtered
        ORDER BY mileageCar ASC
    '''

    return pd.read_sql(query, conn)

def get_user(conn, idUser):
    query = f'''
        SELECT
            idUser,
            phoneUser
        FROM
            user
        where idUser == :idUser
    '''

    return pd.read_sql(query, conn, params={"idUser" : idUser})