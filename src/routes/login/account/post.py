from flask import request, jsonify, make_response
import os
import jwt
from prisma import Prisma
import bcrypt
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

async def post_login_account():
    if not request.json:
        return jsonify({"error": "Request body is required"}), 400
    
    if not request.json.get("email"):
        return jsonify({"error": "Email is required"}), 400

    if not request.json.get("password"):
        return jsonify({"error": "Password is required"}), 400
    
    db = Prisma()

    await db.connect()
    
    account = await db.account.find_unique(
        {
            "email": request.json.get("email")
        }
    )

    await db.disconnect()

    hashedPassword = account.password

    if not bcrypt.checkpw(str.encode(request.json.get("password")), str.encode(hashedPassword)):
        return jsonify({"error": "Invalid password"}), 401

    
    if not account:
        return jsonify({"error": "Account not found"}), 404
    
    session = jwt.encode(
        payload={
            "role": "account",
            "email": str(account.email),
            "id": str(account.id),
            "created_at": datetime.now().timestamp()
        },
        key=os.getenv("JWT_SECRET"),
        algorithm="HS256"
    )
    
    resp = make_response(jsonify({"session": session}), 200)

    resp.set_cookie("session", session, httponly=True, max_age=60*60*2)

    return resp
