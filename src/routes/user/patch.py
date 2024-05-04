from flask import jsonify, request
from prisma import Prisma

async def patch_user(id):
    db = Prisma()
    await db.connect()
        
    data = await db.user.update(
        where={
            "id": id
        },
        data={
            "nim": request.json.get("nim"),
            "name": request.json.get("name"),
        }
    )
    
    await db.disconnect()

    if not data:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({
        "data": "Successfully updated user",
    }), 200
