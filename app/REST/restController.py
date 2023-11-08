
from flask import Blueprint, render_template, flash, redirect, jsonify, request, url_for
from app.db import db   
from datetime import  timedelta
import datetime
from app import app  # Importa la variable app desde app/__init__.py
from app.REST.models import Usuarios
import json
restBP = Blueprint('rest', __name__)

@restBP.route('/get_data_usuarios', methods=['GET'])
def get_data():
    todos_los_usuarios = Usuarios.query.all()
    
    usuarios_json = []
    for usuario in todos_los_usuarios:
        usuario_dict = {
            'id': usuario.id,
            'usuario': usuario.usuario,
            'contrasenna': usuario.contrasenna
        }
        usuarios_json.append(usuario_dict)

    return jsonify(usuarios_json)


@restBP.route('/post_data_usuarios/<int:index>', methods=['POST'])
def post_data(index):
    # Obtén los datos JSON del cuerpo de la solicitud

    nombre = request.form.get('nombre')
    contrasena = request.form.get('contrasena')
    


    user_to_edit = Usuarios.query.get(index)
    if user_to_edit is not None:
        # Actualizar los campos del usuario con los nuevos valores
        new_username = nombre
        new_password = contrasena

        user_to_edit.usuario = new_username
        user_to_edit.contrasenna = new_password

        # Confirmar los cambios en la base de datos
        db.session.commit()
    else:
        print(f"El usuario con ID {index} no se encontró.")
        response = {
            'boolean': False,

        }
        return jsonify(False)
    
    # Envía una respuesta, por ejemplo, un mensaje de éxito
    response = {
        'boolean': True,

    }
    return jsonify(True)

@restBP.route('/delete_usuario/<int:index>', methods=['POST'])
def delete_usuario(index):  
    print(index)
    user_to_delete = Usuarios.query.get(index)
    
    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
        return jsonify(True)
    else:
        return jsonify(False)
    