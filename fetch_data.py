import os
import snowflake.connector
import pandas as pd

def fetch_data(query):
    # Connect to Snowflake using environment variables
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    )
    try:
        cursor = conn.cursor()
        cursor.execute(query)

        # Fetch column names and data
        columns = [desc[0] for desc in cursor.description]
        results = cursor.fetchall()
        if not results:
            return pd.DataFrame([], columns=columns)
        return pd.DataFrame(results, columns=columns)
    except Exception as e:
        raise Exception(f"SQL Error: {e}")
    finally:
        conn.close()

