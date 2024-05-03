from flask import jsonify, request
from prisma import Prisma

async def patch_account(id):
    db = Prisma()

    await db.connect()

    email = request.json.get("email")
    password = request.json.get("password")

    dataToUpdate = {}

    if email:
        dataToUpdate["email"] = email

    if password:
        dataToUpdate["password"] = password
        
    data = await db.account.update(
        where={
            "id": id
        },
        data=dataToUpdate
    )
    
    await db.disconnect()

    if not data:
        return jsonify({"error": "Account not found"}), 404
    
    return jsonify({
        "data": "Successfully updated account",
    }), 200
