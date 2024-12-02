import os
import snowflake.connector
import pandas as pd
import streamlit as st

def fetch_data(query):
    # Connect to Snowflake using environment variables
    conn = snowflake.connector.connect(
        user = st.secrets["SNOWFLAKE_USER"],
        password = st.secrets["SNOWFLAKE_PASSWORD"],
        account = st.secrets["SNOWFLAKE_ACCOUNT"],
        warehouse = st.secrets["SNOWFLAKE_WAREHOUSE"],
        database = st.secrets["SNOWFLAKE_DATABASE"],
        schema = st.secrets["SNOWFLAKE_SCHEMA"]
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

