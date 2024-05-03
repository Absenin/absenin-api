from flask import jsonify
from prisma import Prisma

async def get_account():
    db = Prisma()

    await db.connect()
        
    data = await db.account.find_many()

    accounts = []

    for item in data:
        accounts.append({
            "id": item.id,
            "email": item.email,
            "createdAt": item.created_at,
        })

    await db.disconnect()
    
    return jsonify({
        "data": accounts,
    }), 200
