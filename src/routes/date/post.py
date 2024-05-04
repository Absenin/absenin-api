from flask import request, jsonify
from prisma import Prisma
from datetime import datetime
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

async def post_date():
    if not request.json:
        return jsonify({"error": "Request body is required"}), 400
    
    if not request.json.get("date"):
        return jsonify({"error": "Date is required"}), 400
    
    try:
        datetime.fromtimestamp(int(request.json.get("date")))
    except:
        return jsonify({"error": "Invalid timestamp"}), 400
    
    decoded = jwt.decode(
        jwt=request.cookies.get("session"),
        key=os.getenv("JWT_SECRET"),
        algorithms=["HS256"]
    )

    day = datetime.fromtimestamp(int(request.json.get("date"))).day
    month = datetime.fromtimestamp(int(request.json.get("date"))).month
    year = datetime.fromtimestamp(int(request.json.get("date"))).year
    
    db = Prisma()
    
    await db.connect()

    alvailable = await db.date.find_first(
        where={
            "day": day,
            "month": month,
            "year": year,
            "account_id": decoded.get("id")
        }
    )

    if alvailable:
        await db.disconnect()
        return jsonify({"error": "Date already exists"}), 400
    
    await db.date.create(
        data={
            "day": day,
            "month": month,
            "year": year,
            "account_id": decoded.get("id")
        }
    )

    await db.disconnect()
    
    return jsonify({"message": "Date created successfully"}), 201
