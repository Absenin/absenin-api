from flask import Blueprint
from .get import get_user

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/", methods=["GET"])
def get_user_route():
    return get_user()
