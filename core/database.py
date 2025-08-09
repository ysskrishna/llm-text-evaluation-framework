from sqlmodel import SQLModel, create_engine, Session
from core.config import Config

engine = create_engine(Config.DATABASE_URL, echo=False)

def init_db():
    from models.models import Evaluation
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
