import pandas
from flask import Blueprint, session, render_template

from utils import get_db_connection
from models.index_model import get_all_companies, get_models, get_all_transmissions, get_all_bodytypes, get_all_drivetrains
from models.mycars_model import get_cars

mycars_blueprint = Blueprint('mycars', __name__)

@mycars_blueprint.route('/mycars')
def mycars():
    conn = get_db_connection()

    df_cars = pandas.DataFrame()
    df_companies = get_all_companies(conn)
    df_models = get_models(conn, 1)

    df_transmissions = get_all_transmissions(conn)
    df_bodytypes = get_all_bodytypes(conn)
    df_drivetrains = get_all_drivetrains(conn)

    idUser = -1

    if (session.get('userId', default=None) != None):
        idUser = session['userId']
        df_cars = get_cars(conn, idUser)

    html = render_template('mycars.html',
                            idUser = idUser,
                            cars = df_cars,
                            companies = df_companies,
                            models = df_models,
                            transmissions = df_transmissions,
                            bodytypes = df_bodytypes,
                            drivetrains = df_drivetrains,
                            len = len)

    return html