from src.connection import get_db_connection
from sqlalchemy import text

def probar_conexion_sql():
    print("--- Probando Conexión a SQL Server ---")
    try:
        # 1. Inicializar el objeto de base de datos
        db = get_db_connection()
        
        # 2. Ejecutar un 'SELECT 1' simple para verificar conectividad
        with db._engine.connect() as conexion:
            resultado = conexion.execute(text("SELECT 1"))
            if resultado.scalar() == 1:
                print("✅ Éxito: Conexión establecida con 'MineriaLogisticaDB'.")
            
            # 3. Listar tablas para confirmar visibilidad de metadatos
            print("\nTablas disponibles en la base de datos:")
            print(db.get_usable_table_names())
            
    except Exception as e:
        print(f"❌ La conexión falló: {str(e)}")

if __name__ == "__main__":
    probar_conexion_sql()