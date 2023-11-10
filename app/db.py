from flask_sqlalchemy import SQLAlchemy

# Crea la instancia de SQLAlchemy
db = SQLAlchemy()

# Configura la base de datos usando la instancia db
def configure_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:w^f.j9Q4-5k?@localhost/REST'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

# Otras configuraciones de la base de datos, como modelos y vínculos, pueden ir aquí