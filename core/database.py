from sqlmodel import SQLModel, create_engine, Session
from core.config import Config
from models.models import Evaluation # import all models, so that they are created in the database

engine = create_engine(Config.DATABASE_URL, echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
