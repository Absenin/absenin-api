from flask import Blueprint
from .post import post_login_admin

login_admin_bp = Blueprint("login_admin", __name__, url_prefix="/login")

@login_admin_bp.route("/admin", methods=["POST"])
async def login_admin():
    return await post_login_admin()
