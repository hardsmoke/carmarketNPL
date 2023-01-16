from flask import Blueprint, session, request, redirect, render_template

from models.signup_model import get_user, add_user
from utils import get_db_connection

signup_blueprint = Blueprint('signup', __name__)

@signup_blueprint.route('/sign-up')
def signup():
    conn = get_db_connection()

    invalid_phoneNumber = False

    entered_name = ""
    entered_surname = ""

    if (request.values.get("phoneNumber") and request.values.get("password") and request.values.get("name") and request.values.get("surname")):
        user_df = get_user(conn, request.values.get("phoneNumber"))
        if (user_df.shape[0] != 0):
            entered_name = request.values.get("name")
            entered_surname = request.values.get("surname")
            invalid_phoneNumber = True
        else:
            add_user(conn, request.values.get("phoneNumber"), request.values.get("password"), request.values.get("name"), request.values.get("surname"))
            user_df = get_user(conn, request.values.get("phoneNumber"))
            session['userId'] = str(user_df.iloc[0].idUser)
            session['userPhone'] = user_df.iloc[0].phoneUser
            session['userName'] = user_df.iloc[0].nameUser
            session['userSurname'] = user_df.iloc[0].surnameUser

            return redirect('/mycars')


    return render_template('signup.html',
                            invalid_phoneNumber = invalid_phoneNumber,
                            entered_name = entered_name,
                            entered_surname = entered_surname)