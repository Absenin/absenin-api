from flask import Blueprint
from .post import post_login_account

login_account_bp = Blueprint("login_account", __name__, url_prefix="/login")

@login_account_bp.route("/account", methods=["POST"])
async def login_account():
    return await post_login_account()
