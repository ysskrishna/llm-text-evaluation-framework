from sqlmodel import SQLModel, create_engine, Session
from core.config import Config
import streamlit as st

@st.cache_resource
def get_engine():
    return create_engine(Config.DATABASE_URL, echo=False)
    
def init_db():
    # import all models, so that they are created in the database
    from models.models import Evaluation
    SQLModel.__table_args__ = {'extend_existing': True} # TODO: we are extending the existing tables to resolve streamlit file changes, need to find a better solution
    SQLModel.metadata.create_all(get_engine())


def get_session():
    return Session(get_engine())
