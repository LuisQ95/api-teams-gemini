from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import create_sql_agent
from src.config import GEMINI_API_KEY
from src.connection import get_db_connection

def create_mining_agent():
    # Initialize Gemini
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro", 
        google_api_key=GEMINI_API_KEY,
        temperature=0
    )
    
    # Connect to the DB
    db = get_db_connection()
    
    # Create the SQL Agent
    # We use 'openai-tools' type as it is highly compatible with Gemini's reasoning
    agent_executor = create_sql_agent(
        llm=llm,
        db=db,
        agent_type="openai-tools",
        verbose=True
    )
    
    return agent_executor