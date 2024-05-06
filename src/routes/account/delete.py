from flask import jsonify, request
from prisma import Prisma

async def delete_account(id):
    db = Prisma()

    await db.connect()

    data = await db.account.delete(
        where={
            "id": id
        },
    )
    
    await db.disconnect()

    if not data:
        return jsonify({"error": "Account not found"}), 404
    
    return jsonify({
        "data": "Successfully deleted account",
    }), 200
