from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import create_sql_agent
from src.config import GEMINI_API_KEY
from src.connection import get_db_connection

def create_mining_agent():
    # Initialize Gemini
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key=GEMINI_API_KEY,
        temperature=0
    )

    # Connect to the DB
    db = get_db_connection()

    # 1. Define the system instructions in Spanish
    CUSTOM_PREFIX = """
        Eres un experto en logística minera. Tu misión es ayudar a los usuarios 
        a consultar la base de datos de ciclos de acarreo y estados de flota.
        
        REGLAS DE RESPUESTA:
        1. Responde SIEMPRE en español.
        2. Utiliza terminología minera técnica (Tajo, Chancadora, Guardia, etc.).
        3. Si el usuario pide datos numéricos o comparativos, utiliza tablas de Markdown.
        4. Si no encuentras datos, explica el motivo educadamente en español.
        """

    # Create the SQL Agent
    # We use 'openai-tools' type as it is highly compatible with Gemini's reasoning
    agent_executor = create_sql_agent(
        llm=llm,
        db=db,
        agent_type="openai-tools",
        verbose=True,
        prefix=CUSTOM_PREFIX
    )
    
    return agent_executor