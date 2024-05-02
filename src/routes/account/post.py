from flask import request, jsonify
from prisma import Prisma
import bcrypt

async def post_account():
    if not request.json:
        return jsonify({"error": "Request body is required"}), 400
    
    if not request.json.get("email"):
        return jsonify({"error": "Email is required"}), 400
    
    if not request.json.get("password"):
        return jsonify({"error": "Password is required"}), 400
    
    db = Prisma()

    passwordBytes = str.encode(request.json.get("password"))
    salt = bcrypt.gensalt() 
    passwordHash = bcrypt.hashpw(passwordBytes, salt)

    await db.connect()
        
    await db.account.create(
        data={
            "email": request.json.get("email"),
            "password": passwordHash.decode("utf-8")
        }
    )

    await db.disconnect()
    
    return jsonify({"message": "Account created successfully"}), 201
