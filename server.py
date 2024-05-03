from src import create_app
from dotenv import load_dotenv
import asyncio
from waitress import serve
import os

load_dotenv()

async def main():
    app = create_app()
    print(f"Server running on http://localhost:{os.getenv('PORT')}")
    serve(app, host="0.0.0.0", port=int(os.getenv("PORT")))

if __name__ == '__main__':
    asyncio.run(main())
