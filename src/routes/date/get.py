from flask import request, jsonify
from prisma import Prisma
from datetime import datetime
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

async def get_date(timestamp):
    try:
        datetime.fromtimestamp(int(timestamp))
    except:
        return jsonify({"error": "Invalid timestamp"}), 400
    
    decoded = jwt.decode(
        jwt=request.cookies.get("session"),
        key=os.getenv("JWT_SECRET"),
        algorithms=["HS256"]
    )

    day = datetime.fromtimestamp(int(timestamp)).day
    month = datetime.fromtimestamp(int(timestamp)).month
    year = datetime.fromtimestamp(int(timestamp)).year
    
    db = Prisma()
    
    await db.connect()

    data = await db.date.find_first(
        where={
            "day": day,
            "month": month,
            "year": year,
            "account_id": decoded.get("id")
        },
        include={
            "attendances": True,
        }
    )

    if not data:
        await db.disconnect()
        return jsonify({"error": "Date not exists"}), 404
    
    attendanceData = await db.attendance.find_many(
        where={
            "date_id": data.id
        },
        include={
            "User": True
        }
    )

    await db.disconnect()

    attendance = []

    for item in attendanceData:
        attendance.append({
            "id": item.id,
            "user": {
                "nim": item.User.nim,
                "name": item.User.name,
                "photo": item.User.photo
            },
            "created_at": item.created_at
        })
    
    return jsonify({"data": attendance or []}), 200
