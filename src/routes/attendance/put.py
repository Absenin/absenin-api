from flask import jsonify, request, make_response
import jwt
import os
from prisma import Prisma
from dotenv import load_dotenv  
import bcrypt

load_dotenv()

async def put_attendance():
    if not request.json:
        return jsonify({"error": "Request body required"}), 400
        
    if not request.json.get("nim"):
        return jsonify({"error": "NIM is required"}), 400
    
    decoded = jwt.decode(
        jwt=request.cookies.get("user_attendance"),
        key=os.getenv("JWT_SECRET"),
        algorithms=["HS256"]
    )

    if not decoded:
        return jsonify({"error": "Invalid fingerprint"}), 400

    try:
        valid = bcrypt.checkpw(
            bytes(str(decoded), "utf-8"),
            bytes(request.cookies.get("hash_attendance"), "utf-8")
        )
    except:
        return jsonify({"error": "Invalid fingerprint"}), 400
    
    if not valid:
        return jsonify({"error": "Invalid fingerprint"}), 400

    db = Prisma()

    await db.connect()

    date = await db.date.find_first(
        where={
            "id": decoded.get("date_id"),
        }
    )

    if not date:
        await db.disconnect()
        return jsonify({"error": "Date not exists"}), 404
    
    user = await db.user.find_first(
        where={
            "nim": request.json.get("nim")
        }
    )

    if not user:
        await db.disconnect()
        return jsonify({"error": "User not exists"}), 404
        
    alreadyAttendance = await db.attendance.find_first(
        where={
            "OR": [
                {
                    "user_id": user.id,
                    "date_id": date.id,
                },
                {
                    "ip_address": decoded.get("ip"),
                    "date_id": date.id
                },
                {
                    "visitor_identifier": decoded.get("fingerprint"),
                    "date_id": date.id
                }
            ]
        }
    )

    if alreadyAttendance:
        await db.disconnect()
        return jsonify({"error": "User already attend"}), 400
    
    await db.attendance.create(
        data={
            "date_id": date.id,
            "user_id": user.id,
            "ip_address": decoded.get("ip"),
            "visitor_identifier": decoded.get("fingerprint")
        }
    )

    return jsonify({"message": "Attendance added successfully"}), 201
