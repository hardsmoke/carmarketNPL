import pandas
from flask import Blueprint, request, session, render_template

from models.index_model import get_all_companies, get_models, get_all_transmissions, get_all_active_advertisments, get_all_cities, get_all_bodytypes, get_all_drivetrains, get_user
from models.index_model import filterByCompany, filterByModel, filterByTransmission, filterByPriceFrom, filterByPriceTo, filterByBodyType, filterByDrivetrain
from models.index_model import filterByReleaseYearFrom, filterByReleaseYearTo, filterByMileage, filterByCity
from models.index_model import sortByDate_new, sortByDate_old, sortByMileage_low, sortByPrice_high, sortByPrice_low
from utils import get_db_connection

index_blueprint = Blueprint('index', __name__)
update_models_blueprint = Blueprint('update_models', __name__)

@index_blueprint.route('/')
def index():
    conn = get_db_connection()

    selected_company_id = 0
    selected_model_id = 0
    selected_transmission_id = 0
    selected_bodytype_id = 0
    selected_drivetrain_id = 0
    selected_city_id = 0
    price_from = -1
    price_to = -1
    releaseYear_from = -1
    releaseYear_to = -1
    mileage_to = -1

    selected_sort = 1

    if request.args.get('clear') == None:
        if request.values.get('company'):
            session["selected_company_id"] = int(request.values.get('company'))
        if request.values.get('model_to_filter'):
            session["selected_model_id"] = int(request.values.get('model_to_filter'))
        if request.values.get('transmission'):
            session["selected_transmission_id"] = int(request.values.get('transmission'))
        if request.values.get('bodytype'):
            session["selected_bodytype_id"] = int(request.values.get('bodytype'))
        if request.values.get('drivetrain'):
            session["selected_drivetrain_id"] = int(request.values.get('drivetrain'))
        if request.values.get('city'):
            session["selected_city_id"] = int(request.values.get('city'))
        if request.values.get('price_from'):
            session["price_from"] = int(request.values.get('price_from'))
        else:
            session["price_from"] = -1
        if request.values.get('price_to'):
            session["price_to"] = int(request.values.get('price_to'))
        else:
            session["price_to"] = -1
        if request.values.get('releaseYear_from'):
            session["releaseYear_from"] = int(request.values.get('releaseYear_from'))
        else:
            session["releaseYear_from"] = -1
        if request.values.get('releaseYear_to'):
            session["releaseYear_to"] = int(request.values.get('releaseYear_to'))
        else:
            session["releaseYear_to"] = -1
        if request.values.get('mileage_to'):
            session["mileage_to"] = int(request.values.get('mileage_to'))
        else:
            session["mileage_to"] = -1
    else:
        session["selected_company_id"] = None
        session["selected_model_id"] = None
        session["selected_transmission_id"] = None
        session["selected_bodytype_id"] = None
        session["selected_drivetrain_id"] = None
        session["selected_city_id"] = None
        session["price_from"] = None
        session["price_to"] = None
        session["releaseYear_from"] = None
        session["releaseYear_to"] = None
        session["mileage_to"] = None

    if request.values.get('sort'):
        session["selected_sort"] = int(request.values.get('sort'))

    if (session.get("selected_sort", default=None) != None):
        selected_sort = session["selected_sort"]

    df_ads = get_all_active_advertisments(conn)
    df_companies = get_all_companies(conn)
    df_models = pandas.core.frame.DataFrame
    if (session.get("selected_company_id", default=None) != None):
        df_models = get_models(conn, session["selected_company_id"])
    df_transmissions = get_all_transmissions(conn)
    df_bodytypes = get_all_bodytypes(conn)
    df_drivetrains = get_all_drivetrains(conn)
    df_cities = get_all_cities(conn)
    
    if (session.get("selected_company_id", default=None) != None and session["selected_company_id"] != 0):
        selected_company_id = session["selected_company_id"]
        df_ads = filterByCompany(conn, df_ads, selected_company_id)
        if (session.get("selected_model_id", default=None) != None and session["selected_model_id"] != 0):
            selected_model_id = session["selected_model_id"]
            df_ads = filterByModel(conn, df_ads, df_models.iloc[0].idModelCar + selected_model_id - 1)
    
    if (session.get("selected_transmission_id", default=None) != None and session["selected_transmission_id"] != 0):
        selected_transmission_id = session["selected_transmission_id"]
        df_ads = filterByTransmission(conn, df_ads, session["selected_transmission_id"])

    if (session.get("selected_bodytype_id", default=None) != None and session["selected_bodytype_id"] != 0):
        selected_bodytype_id = session["selected_bodytype_id"]
        df_ads = filterByBodyType(conn, df_ads, selected_bodytype_id)

    if (session.get("selected_drivetrain_id", default=None) != None and session["selected_drivetrain_id"] != 0):
        selected_drivetrain_id = session["selected_drivetrain_id"]
        df_ads = filterByDrivetrain(conn, df_ads, selected_drivetrain_id)

    if (session.get("selected_city_id", default=None) != None and session["selected_city_id"] != 0):
        selected_city_id = session["selected_city_id"]
        df_ads = filterByCity(conn, df_ads, selected_city_id)

    if (session.get("price_from", default=None) != None and session["price_from"] != -1):
        price_from = session["price_from"]
        df_ads = filterByPriceFrom(conn, df_ads, price_from)

    if (session.get("price_to", default=None) != None and session["price_to"] != -1):
        price_to = session["price_to"]
        df_ads = filterByPriceTo(conn, df_ads, price_to)

    if (session.get("releaseYear_from", default=None) != None and session["releaseYear_from"] != -1):
        releaseYear_from = session["releaseYear_from"]
        df_ads = filterByReleaseYearFrom(conn, df_ads, releaseYear_from)

    if (session.get("releaseYear_to", default=None) != None and session["releaseYear_to"] != -1):
        releaseYear_to = session["releaseYear_to"]
        df_ads = filterByReleaseYearTo(conn, df_ads, releaseYear_to)

    if (session.get("mileage_to", default=None) != None and session["mileage_to"] != -1):
        mileage_to = session["mileage_to"]
        df_ads = filterByMileage(conn, df_ads, mileage_to)

    match selected_sort:
        case 1: df_ads = sortByDate_new(conn, df_ads)
        case 2: df_ads = sortByDate_old(conn, df_ads)
        case 3: df_ads = sortByPrice_low(conn, df_ads)
        case 4: df_ads = sortByPrice_high(conn, df_ads)
        case 5: df_ads = sortByMileage_low(conn, df_ads)

    html = render_template('index.html',
                            selected_company_id = selected_company_id,
                            selected_model_id = selected_model_id,
                            selected_transmission_id = selected_transmission_id,
                            selected_bodytype_id = selected_bodytype_id,
                            selected_drivetrain_id = selected_drivetrain_id,
                            selected_city_id = selected_city_id,
                            price_from = price_from,
                            price_to = price_to,
                            releaseYear_from = releaseYear_from,
                            releaseYear_to = releaseYear_to,
                            mileage_to = mileage_to,

                            ads = df_ads,
                            models = df_models,
                            companies = df_companies,
                            transmissions = df_transmissions,
                            bodytypes = df_bodytypes,
                            drivetrains = df_drivetrains,
                            cities = df_cities,

                            selected_sort = selected_sort,

                            len = len)

    return html

@update_models_blueprint.route('/update_models', methods=['POST', 'GET'])
def update_models():
    content = request.json
    conn = get_db_connection()
    df_models = get_models(conn, int(content.get('idCompany')))

    return df_models.to_json()