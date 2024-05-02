from src import create_app
import asyncio

async def main():
    app = create_app()
    app.run(port=3001)

if __name__ == '__main__':
    asyncio.run(main())
