from flask import Blueprint
from .post import post_date
from .get import get_date

date_bp = Blueprint("date", __name__, url_prefix="/date")

@date_bp.route("/<timestamp>", methods=["GET"])
async def get_date_route(timestamp):
    return await get_date(timestamp)

@date_bp.route("", methods=["POST"])
async def post_date_route():
    return await post_date()