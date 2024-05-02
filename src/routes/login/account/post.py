from flask import request, jsonify, make_response
import os
import jwt
from prisma import Prisma
import bcrypt

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

    hashedPassword = account.password

    if not bcrypt.checkpw(str.encode(request.json.get("password")), str.encode(hashedPassword)):
        await db.disconnect()
        return jsonify({"error": "Invalid password"}), 401

    await db.disconnect()
    
    if not account:
        return jsonify({"error": "Account not found"}), 404
    
    resp = make_response()

    resp.set_cookie("session", jwt.encode(
        payload={
            "role": "account",
            "email": str(account.email)
        },
        key=os.getenv("JWT_SECRET"),
        algorithm="HS256"), httponly=True)

    return resp
