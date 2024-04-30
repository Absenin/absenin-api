from flask import Flask
from prisma import Prisma
from src.routes.user import user_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(user_bp)

    return app

def connect_db():
    db = Prisma()
    db.connect()

    return db