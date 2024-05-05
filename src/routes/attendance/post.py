from flask import jsonify, request, make_response
import jwt
import os
from datetime import datetime
from dotenv import load_dotenv  
import bcrypt 

load_dotenv()

async def post_attendance():
    if not request.json:
        return jsonify({"error": "Request body required"}), 400
    
    if not request.json.get("ip"):
        return jsonify({"error": "IP is required"}), 400
    
    if not request.json.get("fingerprint"):
        return jsonify({"error": "Fingerprint is required"}), 400
    
    if not request.json.get("date_id"):
        return jsonify({"error": "Date ID is required"}), 400
    
    payload = {
        "ip": request.json.get("ip"),
        "fingerprint": request.json.get("fingerprint"),
        "date_id": request.json.get("date_id"),
        "created_at": datetime.now().timestamp(),
    }

    payloadBytes = bytes(str(payload), "utf-8")
    salt = bcrypt.gensalt() 
    payloadHash = bcrypt.hashpw(payloadBytes, salt)
    
    cookie = jwt.encode(
        payload=payload,
        key=os.getenv("JWT_SECRET"),
        algorithm="HS256"
    )

    resp = make_response(jsonify({
        "user_attendance": cookie,
        "hash_attendance": payloadHash.decode("utf-8")
    }), 200)

    resp.set_cookie("user_attendance", cookie, httponly=True, max_age=60*10)
    resp.set_cookie("hash_attendance", payloadHash.decode("utf-8"), httponly=True, max_age=60*10)
    
    return resp
