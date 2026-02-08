from src.agent_logic import create_mining_agent
import time

def ejecutar_agente_terminal():
    print("--- Iniciando Agente de Logística Minera (Modo Terminal) ---")
    print("Inicializando Gemini y el Agente SQL... por favor espera.")
    
    try:
        # 1. Instanciar el agente igual que en main.py
        agent_executor = create_mining_agent()
        print("✅ ¡Agente listo! Escribe 'salir' para terminar.\n")
        
        while True:
            consulta_usuario = input("Tú: ")
            
            if consulta_usuario.lower() in ["salir", "exit", "quit"]:
                print("Cerrando sesión del agente...")
                break
            
            tiempo_inicio = time.time()
            
            # 2. Invocar al agente
            # Esto imita el comportamiento de on_message_activity en Teams
            respuesta = agent_executor.invoke({"input": consulta_usuario})
            
            tiempo_fin = time.time()
            
            print(f"\nBot: {respuesta['output']}")
            print(f"--- (Tiempo de procesamiento: {tiempo_fin - tiempo_inicio:.2f}s) ---\n")
            
    except Exception as e:
        print(f"❌ Error del Agente: {str(e)}")

if __name__ == "__main__":
    ejecutar_agente_terminal()