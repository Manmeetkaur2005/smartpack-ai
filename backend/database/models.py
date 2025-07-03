from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    length = Column(Float)
    width = Column(Float)
    height = Column(Float)
    weight = Column(Float)
    fragile = Column(Boolean)

class Box(Base):
    __tablename__ = "boxes"
    id = Column(Integer, primary_key=True)
    box_type = Column(String)
    efficiency = Column(Float)
    co2_saved = Column(Float)

# --- DB Setup ---
DB_URL = "sqlite:///smartpack.db"

engine = create_engine(DB_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
