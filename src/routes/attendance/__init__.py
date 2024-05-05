from flask import Blueprint
from .post import post_attendance
from .put import put_attendance

attendance_bp = Blueprint("attendance", __name__, url_prefix="/attendance")

@attendance_bp.route("", methods=["POST"])
async def post_attendance_route():
    return await post_attendance()

@attendance_bp.route("", methods=["PUT"])
async def put_attendance_route():
    return await put_attendance()