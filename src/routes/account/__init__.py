from flask import Blueprint
from .post import post_account
from .get import get_account
from .delete import delete_account
from .patch import patch_account

account_bp = Blueprint("account", __name__, url_prefix="/account")

@account_bp.route("", methods=["GET"])
async def get_account_route():
    return await get_account()

@account_bp.route("", methods=["POST"])
async def post_account_route():
    return await post_account()

@account_bp.route("/<id>", methods=["DELETE"])
async def delete_account_route(id):
    return await delete_account(id)

@account_bp.route("/<id>", methods=["PATCH"])
async def patch_account_route(id):
    return await patch_account(id)