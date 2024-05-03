from flask import request, jsonify, make_response, render_template
import os
import jwt

async def post_login_admin():
    if not request.json:
        return jsonify({"error": "Request body is required"}), 400
    
    if not request.json.get("password"):
        return jsonify({"error": "Password is required"}), 400

    if request.json.get("password") != os.getenv("ADMIN_PASSWORD"):
        return jsonify({"error": "Invalid password"}), 401
    
    session = jwt.encode(
        payload={"role": "admin"},
        key=os.getenv("JWT_SECRET"),
        algorithm="HS256")
    
    resp = make_response(jsonify({"session": session}), 200)

    resp.set_cookie("session", session, httponly=True)

    return resp
