from models import Base, engine

def init_db():
    print("🔧 Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created.")

if __name__ == "__main__":
    init_db()
