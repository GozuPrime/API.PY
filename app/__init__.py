from flask import Flask
from flask_cors import CORS
from .config.db import create_db 
from .router.pacientes_routes import paciente_bp
from .router.comportamiento_routes import comportamiento_bp

def create_app():
    app=Flask(__name__)
    CORS(app)

    # CREA LA BASE DE DATOS SQLITE
    #create_db()

    # Registrar Blueprints
    app.register_blueprint(paciente_bp)
    app.register_blueprint(comportamiento_bp)


    return app