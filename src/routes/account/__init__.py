from flask import Blueprint
from .post import post_account
from .get import get_account

account_bp = Blueprint("account", __name__, url_prefix="/account")

@account_bp.route("", methods=["GET"])
async def get_account_route():
    return await get_account()

@account_bp.route("", methods=["POST"])
async def post_account_route():
    return await post_account()
