from src.agent_logic import create_mining_agent

def main():
    agent_executor = create_mining_agent()

    user_query = "List the top 3 trucks with the most hauling cycles."
    
    print(f"--- Querying Agent ---")
    try:
        response = agent_executor.invoke({"input": user_query})
        print(f"Response: {response['output']}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()