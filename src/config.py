import os
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

# Access the variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SQL_PWD = os.getenv("SQL_PASSWORD")

# SQL Server Configuration
DB_CONFIG = {
    "driver": "ODBC Driver 17 for SQL Server",
    "server": "localhost",
    "database": "MineriaLogisticaDB",
    "username": "sa",
    "password": SQL_PWD
}

# Constructing the SQLAlchemy URI
CONNECTION_URI = (
    f"mssql+pyodbc://{DB_CONFIG['username']}:{DB_CONFIG['password']}@"
    f"{DB_CONFIG['server']}/{DB_CONFIG['database']}?driver={DB_CONFIG['driver']}"
)