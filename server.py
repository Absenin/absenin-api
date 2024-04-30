from src import create_app, connect_db

if __name__ == '__main__':
    connect_db()
    app = create_app()
    app.run(port=3001)
