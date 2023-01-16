from flask import Blueprint, session, redirect

logout_blueprint = Blueprint('logout', __name__)

@logout_blueprint.route('/logout')
def logout():
    session['userId'] = None
    session['userPhone'] = None
    session['userName'] = None
    session['userSurname'] = None
    return redirect('/')