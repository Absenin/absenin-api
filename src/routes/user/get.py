from prisma import Prisma
from flask import jsonify, request
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

async def get_user():
    decoded = jwt.decode(
        jwt=request.cookies.get("session"),
        key=os.getenv("JWT_SECRET"),
        algorithms=["HS256"]
    )

    db = Prisma()

    await db.connect()
        
    data = await db.user.find_many(
        where={
            "account_id": decoded.get("id")
        }
    )

    users = []

    for item in data:
        users.append({
            "nim": item.nim,
            "name": item.name,
            "photo": item.photo,
            "created_at": item.created_at,
            "id": item.id,
        })

    await db.disconnect()
    
    return jsonify({
        "data": users,
    }), 200
