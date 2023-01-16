import pandas
from flask import Blueprint, session, request, render_template

from models.myads_model import get_active_advertisments_full, get_nonactive_advertisments_full, advertisments_cars_except, add_advertisment, get_userCarId
from models.index_model import get_all_cities
from utils import get_db_connection

myads_blueprint = Blueprint('myads', __name__)

@myads_blueprint.route('/myads')
def myads():
    conn = get_db_connection()

    df_active_ads = pandas.DataFrame()
    df_nonactive_ads = pandas.DataFrame()
    df_exception = pandas.DataFrame()
    df_cities = get_all_cities(conn)

    if (session.get('userId', default=None) != None):
        df_cities = get_all_cities(conn)
        df_active_ads = get_active_advertisments_full(conn, session['userId'])
        df_nonactive_ads = get_nonactive_advertisments_full(conn, session['userId'])
        df_exception = advertisments_cars_except(conn, session['userId'])

    return render_template('myads.html',
                            ads = df_active_ads,
                            nonactive_ads = df_nonactive_ads,
                            avble_cars = df_exception,
                            cities = df_cities,
                            len = len)