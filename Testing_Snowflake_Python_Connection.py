import snowflake.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve Snowflake connection details from environment variables
USER = os.getenv("SNOWFLAKE_USER")
PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")
ROLE = os.getenv("SNOWFLAKE_ROLE")

try:
    # Establish connection
    conn = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        warehouse=WAREHOUSE,
        database=DATABASE,
        schema=SCHEMA,
        role=ROLE
    )

    # Execute a query to confirm the connection
    cursor = conn.cursor()
    cursor.execute("SELECT CURRENT_VERSION()")
    version = cursor.fetchone()
    print(f"Successfully connected to Snowflake! Current version: {version[0]}")

    # List tables in the schema
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    if tables:
        print("Tables in the schema:")
        for table in tables:
            print(f"- {table[1]}")  # Table name is typically the second field
    else:
        print("No tables found in the schema.")

except Exception as e:
    print(f"Error connecting to Snowflake: {e}")
finally:
    if conn:
        conn.close()
        print("Connection closed.")
