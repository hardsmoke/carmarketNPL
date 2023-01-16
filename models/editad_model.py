def edit_advertisment(conn, idUserCar, idCity, price, desc):
    query = '''
        UPDATE advertisment
        SET carPrice = :price, city_idCity = :idCity, description = :desc
        WHERE userCar_idUserCar == :idUserCar
    '''

    cur = conn.cursor()
    cur.execute(query, {"idUserCar" : idUserCar, "idCity" : idCity, "price" : price, "desc" : desc})
    conn.commit()