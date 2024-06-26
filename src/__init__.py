from flask import Flask
from prisma import Prisma
from src.routes.user import user_bp
from src.routes.account import account_bp
from src.middleware import check_auth
from src.routes.login.admin import login_admin_bp
from src.routes.login.account import login_account_bp
from src.routes.date import date_bp
from src.routes.attendance import attendance_bp

def create_app():
    app = Flask(__name__)

    @app.before_request
    async def before_request():
        return await check_auth()

    app.register_blueprint(user_bp)
    app.register_blueprint(account_bp)
    app.register_blueprint(login_admin_bp)
    app.register_blueprint(login_account_bp)
    app.register_blueprint(date_bp)
    app.register_blueprint(attendance_bp)

    return app