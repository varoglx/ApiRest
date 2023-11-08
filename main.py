# no tocar 
from app import app
from app.db import db

if __name__ == '__main__':
    with app.app_context():
        # Aquí dentro del contexto de la aplicación, puedes realizar operaciones que necesiten acceso a la base de datos
        db.create_all()  # Por ejemplo, crear las tablas en la base de datos

    # Luego, fuera del contexto de la aplicación, ejecutas la aplicación Flask
    app.run()
