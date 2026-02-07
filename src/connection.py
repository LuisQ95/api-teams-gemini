from langchain_community.utilities import SQLDatabase
from src.config import CONNECTION_URI

def get_db_connection():
    """Returns a LangChain SQLDatabase object."""
    return SQLDatabase.from_uri(CONNECTION_URI)