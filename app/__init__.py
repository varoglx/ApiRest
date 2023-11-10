from flask import Flask
from flask_cors import CORS
 
from app.db import db, configure_db  
from sqlalchemy import text  
from flask_sqlalchemy import SQLAlchemy

from app.REST.models import Usuarios


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.debug = True  
CORS(app)

db = configure_db(app)


from app.controllers import general
from app.REST.restController import restBP


app.register_blueprint(restBP)
CORS(app, resources={r"/post_data_usuarios/<int:index>": {"origins": "*"}})
CORS(app, resources={r"/get_data_usuarios": {"origins": "*"}})
CORS(app, resources={r"/post_data_usuarios/<int:index>":{"origins":"*" }})
CORS(app, resources={r"/registrar_usuario":{"origins":"*" }})