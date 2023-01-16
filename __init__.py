from flask import Flask

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

from controllers.index import index_blueprint
from controllers.index import update_models_blueprint
from controllers.signin import signin_blueprint
from controllers.signup import signup_blueprint
from controllers.mycars import mycars_blueprint
from controllers.editcar import editcar_blueprint
from controllers.myads import myads_blueprint
from controllers.newcar import newcar_blueprint
from controllers.newad import newad_blueprint
from controllers.editad import editad_blueprint
from controllers.removead import removead_blueprint
from controllers.logout import logout_blueprint
from controllers.removecar import removecar_blueprint

app.register_blueprint(index_blueprint)
app.register_blueprint(signin_blueprint)
app.register_blueprint(signup_blueprint)
app.register_blueprint(mycars_blueprint)
app.register_blueprint(editcar_blueprint)
app.register_blueprint(myads_blueprint)
app.register_blueprint(newcar_blueprint)
app.register_blueprint(update_models_blueprint)
app.register_blueprint(newad_blueprint)
app.register_blueprint(editad_blueprint)
app.register_blueprint(removead_blueprint)
app.register_blueprint(logout_blueprint)
app.register_blueprint(removecar_blueprint)

if (__name__ == "__main__"):
    app.run(debug=True)