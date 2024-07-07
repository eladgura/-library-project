from app import create_app, db

app = create_app()

def init_db():
    with app.app_context():
        db.create_all()
        print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)  # You can set debug=False in production
