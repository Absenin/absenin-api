from flask import jsonify, request
from prisma import Prisma

async def delete_user(id):
    db = Prisma()

    await db.connect()
        
    data = await db.user.delete(
        where={
            "id": id
        }
    )
    
    await db.disconnect()

    if not data:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({
        "data": "Successfully deleted user",
    }), 200
