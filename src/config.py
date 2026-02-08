import os
from dotenv import load_dotenv

load_dotenv()

# Gemini & SQL Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SQL_PWD = os.getenv("SQL_PASSWORD")

# NEW: Microsoft Bot Configuration
MS_APP_ID = os.getenv("MICROSOFT_APP_ID")
MS_APP_PASSWORD = os.getenv("MICROSOFT_APP_PASSWORD")
MS_APP_TYPE = os.getenv("MICROSOFT_APP_TYPE")
MS_TENANT_ID = os.getenv("MICROSOFT_APP_TENANT_ID")

# SQL Server Configuration (Keep as is)
DB_CONFIG = {
    "driver": "ODBC Driver 17 for SQL Server",
    "server": "localhost",
    "database": "MineriaLogisticaDB",
    "username": "sa",
    "password": SQL_PWD
}

CONNECTION_URI = (
    f"mssql+pyodbc://{DB_CONFIG['username']}:{DB_CONFIG['password']}@"
    f"{DB_CONFIG['server']}/{DB_CONFIG['database']}?driver={DB_CONFIG['driver']}"
)