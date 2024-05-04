from flask import jsonify, request
from prisma import Prisma
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

async def post_user():
    if not request.json:
        return jsonify({"error": "Request body is required"}), 400
    
    if not request.json.get("nim"):
        return jsonify({"error": "NIM is required"}), 400
    
    if not request.json.get("name"):
        return jsonify({"error": "Name is required"}), 400
    
    decoded = jwt.decode(
        jwt=request.cookies.get("session"),
        key=os.getenv("JWT_SECRET"),
        algorithms=["HS256"]
    )
    
    db = Prisma()
    
    await db.connect()

    available = await db.user.find_first(
        where={
            "nim": request.json.get("nim"),
            "account_id": decoded.get("id")
        }
    )

    if available:
        await db.disconnect()
        return jsonify({"error": "User already exists"}), 400
        
    await db.user.create(
        data={
            "name": request.json.get("name"),
            "nim": request.json.get("nim"),
            "account_id": decoded.get("id")
        }
    )

    await db.disconnect()
    
    return jsonify({"message": "User created successfully"}), 201