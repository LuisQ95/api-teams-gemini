from src.agent_logic import create_mining_agent, limpiar_respuesta_gemini
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

            # Limpiar y concatenar la respuesta
            texto_final = limpiar_respuesta_gemini(respuesta["output"])
            
            tiempo_fin = time.time()
            raw_output = respuesta["output"]
            if isinstance(raw_output, list) and len(raw_output) > 0 and "text" in raw_output[0]:
                final_response = raw_output[0]["text"]
            else:
                final_response = raw_output
            
            tiempo_fin = time.time()
            
            print("="*50)
            print(f"\nBot: {texto_final}")
            print("="*50)
            print(f"\nBot: {final_response}")
            print("="*50)
            print(f"\nBot: {respuesta['output']}")
            print("="*50)
            print(f"--- (Tiempo de procesamiento: {tiempo_fin - tiempo_inicio:.2f}s) ---\n")
            
    except Exception as e:
        print(f"❌ Error del Agente: {str(e)}")

if __name__ == "__main__":
    ejecutar_agente_terminal()