from app.db import db
from sqlalchemy import Column, String, Integer

class Usuarios(db.Model):
    id = db.Column(Integer, primary_key=True)
    
    # Especifica la longitud máxima para las columnas de cadena
    usuario = db.Column(String(255))  # Por ejemplo, aquí se establece una longitud máxima de 255 caracteres
    contrasenna = db.Column(String(255))  # También se establece una longitud máxima de 255 caracteres

    # Definir las relaciones con las tablas de Médicos y Centros Clínicos
