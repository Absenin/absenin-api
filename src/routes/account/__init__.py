from flask import Blueprint
from .post import post_account

user_bp = Blueprint("account", __name__, url_prefix="/account")

@user_bp.route("/", methods=["POST"])
def post_account_route():
    return post_account()
