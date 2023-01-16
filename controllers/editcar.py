import base64

from flask import Blueprint, redirect, session, request

from models.index_model import get_models
from models.mycars_model import get_base64img, edit_car
from utils import get_db_connection

editcar_blueprint = Blueprint('editcar', __name__)

@editcar_blueprint.route('/editcar', methods=["POST", "GET"])
def editcar():
    conn = get_db_connection()

    if (session.get('userId', default=None) != None):
        carId = request.values.get('idCar')
        company = int(request.values.get('company_to_edit')) + 1
        model = int(request.values.get('model_to_edit')) + 1
        transmission = request.values.get('transmission_to_edit') 
        drivetrain = request.values.get('drivetrain_to_edit')
        bodytypecar = request.values.get('bodytypecar_to_edit')
        releaseYear = request.values.get('releaseYear_to_edit')
        horsepowers = request.values.get('horsepowers_to_edit')
        mileage = request.values.get('mileage_to_edit')

        file = request.files.get('file')
        base64img = None
        if (file):
            base64img = base64.standard_b64encode(file.read()).decode()
        else:
            base64img = get_base64img(conn, carId).iloc[0].base64img

        df_models = get_models(conn, company)
        idModelCar = int(df_models.idModelCar.iloc[model - 1])

        edit_car(conn, carId, idModelCar, transmission, drivetrain, bodytypecar, releaseYear, horsepowers, mileage, base64img)        

    return redirect('/mycars')