from flask import Blueprint, session, request, redirect

from models.mycars_model import remove_car, get_userCarId, remove_usercar, remove_advertisment
from utils import get_db_connection

removecar_blueprint = Blueprint('removecar', __name__)

@removecar_blueprint.route('/removecar', methods=["POST"])
def removecar():
    conn = get_db_connection()

    if (session.get('userId') != None):
        if (request.values.get('idCar')):
            car_id = int(request.values.get('idCar'))
            user_id = int(session.get('userId'))
            df_usercar = get_userCarId(conn, user_id, car_id)
            idUserCar = int(df_usercar.iloc[0])
            remove_advertisment(conn, idUserCar)
            remove_usercar(conn, idUserCar)
            remove_car(conn, car_id)

    return redirect('/mycars')