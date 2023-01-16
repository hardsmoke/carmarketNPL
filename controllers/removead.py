from flask import Blueprint, session, request, redirect

from models.removead_model import remove_advertisment, get_advertisments
from utils import get_db_connection

removead_blueprint = Blueprint('removead', __name__)

@removead_blueprint.route('/removead')
def removead():
    conn = get_db_connection()

    if (session.get('userId') != None):
        df_advertisments = get_advertisments(conn, session.get('userId'))
        if (request.values.get('advertisment_id')):
            advertisment_id = int(request.values.get('advertisment_id'))
            if (len(df_advertisments[df_advertisments["advertisment_id"] == advertisment_id]) != 0):
                remove_advertisment(conn, advertisment_id)

    return redirect('/myads')