from flask import Blueprint, redirect, session, request

from models.editad_model import edit_advertisment
from models.newad_model import get_userCarId
from utils import get_db_connection

editad_blueprint = Blueprint('editad', __name__)

@editad_blueprint.route('/editad')
def editad():
    conn = get_db_connection()
    if (session.get('userId', default=None) != None):
        if (request.values.get('car_to_edit') and request.values.get('city_to_edit') and request.values.get('price_to_edit')):
            userId = session.get('userId')
            carId = request.values.get('car_to_edit')
            idUserCar = get_userCarId(conn, userId, carId)
            cityId = request.values.get('city_to_edit')
            price = request.values.get('price_to_edit')
            description = request.values.get('desc_to_edit')
            edit_advertisment(conn, int(idUserCar.iloc[0]), cityId, price, description)

    return redirect('/myads')