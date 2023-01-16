from flask import Blueprint, request, session, redirect
import base64

from models.index_model import get_models
from models.newcar_model import add_car, add_usercar
from utils import get_db_connection

newcar_blueprint = Blueprint('newcar', __name__)

@newcar_blueprint.route('/newcar', methods=["POST", "GET"])
def newcar():
    conn = get_db_connection()

    if (session.get('userId', default=None) != None):
        userId = session.get('userId')
        company = int(request.values.get('company_to_add')) + 1
        model = int(request.values.get('model_to_add'))
        transmission = request.values.get('transmission_to_add')
        drivetrain = request.values.get('drivetrain_to_add')
        bodytypecar = request.values.get('bodytypecar_to_add')
        releaseyear = request.values.get('releaseYear_to_add')
        horsepowers = request.values.get('horsepowers_to_add')
        mileage = request.values.get('mileage_to_add')
        df_model = get_models(conn, company)

        file = request.files.get('file')
        base64img = None
        if (file):
            base64img = base64.standard_b64encode(file.read()).decode()

        idModelCar = int(df_model.iloc[model].idModelCar)
        idCar = add_car(conn, idModelCar, bodytypecar, drivetrain, transmission, horsepowers, releaseyear, mileage, base64img)
        add_usercar(conn, idCar, userId)

    return redirect('mycars')