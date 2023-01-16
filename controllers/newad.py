from flask import Blueprint, redirect, session, request

from models.newad_model import get_userCarId, add_advertisment
from utils import get_db_connection

newad_blueprint = Blueprint('newad', __name__)

@newad_blueprint.route('/newad')
def newad():
    conn = get_db_connection()

    if (session.get('userId', default=None) != None):
        if (request.values.get('car_to_ad') != None and request.values.get('city_to_ad') and request.values.get('price_to_ad')):
            userId = session.get('userId')
            carId = request.values.get('car_to_ad')
            idUserCar = get_userCarId(conn, userId, carId)
            cityId = request.values.get('city_to_ad')
            price = request.values.get('price_to_ad')
            description = request.values.get('desc_to_ad')
            add_advertisment(conn, int(idUserCar.iloc[0]), cityId, price, description)

    return redirect('/myads')