from flask import Blueprint, request, redirect, session, render_template

from models.signin_model import get_user
from utils import get_db_connection

signin_blueprint = Blueprint('signin', __name__)

@signin_blueprint.route('/sign-in')
def signin():
    conn = get_db_connection()

    invalid_data = False
    phoneNumber = request.values.get("phoneNumber")
    password = request.values.get("password")

    if (phoneNumber and password):
        user_df = get_user(conn, phoneNumber, password)
        if (len(user_df) != 0):
            session['userId'] = str(user_df.iloc[0].idUser)
            session['userPhone'] = user_df.iloc[0].phoneUser
            session['userName'] = user_df.iloc[0].nameUser
            session['userSurname'] = user_df.iloc[0].surnameUser
            
            return redirect('/mycars')
        else:
            invalid_data = True

    return render_template('signin.html',
                            invalid_data = invalid_data)