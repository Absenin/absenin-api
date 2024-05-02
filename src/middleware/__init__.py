from flask import request, jsonify
import os
import jwt
from prisma import Prisma

access_route = {
    "account": ["/user"],
    "admin": ["/account"]
}

async def check_auth():
    if request.path == "/login/admin" or request.path == "/login/account":
        return None
    
    if not request.cookies.get("session"):
        return jsonify({"error": "Unauthorized"}), 401
    
    if request.headers.get("Authorization") != os.getenv("AUTH_TOKEN"):
        return jsonify({"error": "Invalid authorization token"}), 401
    
    decoded = jwt.decode(
        jwt=request.cookies.get("session"),
        key=os.getenv("JWT_SECRET"),
        algorithms=["HS256"]
    )

    if decoded.get("role") not in access_route:
        return jsonify({"error": "Unauthorized, unknown role"}), 401
    
    if request.path not in access_route.get(decoded.get("role")):
        return jsonify({"error": "Unauthorized, you cant access this path"}), 401

    if decoded.get("role") == "account":
        db = Prisma()

        await db.connect()

        account = await db.account.find_unique(
            {
                "email": decoded.get("email")
            }
        )

        await db.disconnect()

        if not account:
            return jsonify({"error": "Account not found"}), 404

        return None
    
    return None