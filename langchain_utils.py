import os
import snowflake.connector
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import streamlit as st


def generate_sql_query(question):
    schema_info = """
    Schema for IPL.PUBLIC.DELIVERIES:
    - MATCH_ID: NUMBER
    - INNING: NUMBER
    - BATTING_TEAM: VARCHAR
    - BOWLING_TEAM: VARCHAR
    - OVER: NUMBER
    - BALL: NUMBER
    - BATTER: VARCHAR
    - BOWLER: VARCHAR
    - NON_STRIKER: VARCHAR
    - BATSMAN_RUNS: NUMBER
    - EXTRA_RUNS: NUMBER
    - TOTAL_RUNS: NUMBER
    - EXTRAS_TYPE: VARCHAR
    - IS_WICKET: NUMBER
    - PLAYER_DISMISSED: VARCHAR
    - DISMISSAL_KIND: VARCHAR
    - FIELDER: VARCHAR

    Schema for IPL.PUBLIC.MATCHES:
    - ID: NUMBER
    - SEASON: VARCHAR
    - CITY: VARCHAR
    - DATE: DATE
    - MATCH_TYPE: VARCHAR
    - PLAYER_OF_MATCH: VARCHAR
    - VENUE: VARCHAR
    - TEAM1: VARCHAR
    - TEAM2: VARCHAR
    - TOSS_WINNER: VARCHAR
    - TOSS_DECISION: VARCHAR
    - WINNER: VARCHAR
    - RESULT: VARCHAR
    - RESULT_MARGIN: NUMBER
    - TARGET_RUNS: NUMBER
    - TARGET_OVERS: NUMBER
    - SUPER_OVER: BOOLEAN
    - METHOD: VARCHAR
    - UMPIRE1: VARCHAR
    - UMPIRE2: VARCHAR
    """

    prompt = PromptTemplate(
        template=f"""
        You are a SQL expert for Snowflake. Using the following table schemas:
        {schema_info}

        Generate a valid SQL query for Snowflake to answer the following question. 
        Ensure the correct use of data types, such as handling dates directly with DATE columns and BOOLEAN values for conditions. 
        Ensure that for questions about "most runs," you use SUM for aggregation and group by according to batting_team and match_id.
        Ensure the query calculates the average of the sum of total runs, grouped by match_id and batting_team.
        For queries related to "average(sum(total_runs))":
            - First calculate the total runs per match for each team using SUM.
            - Then calculate the average over these totals using AVG.
            - Ensure the query is grouped by BATTING_TEAM.
            - Use ORDER BY for ranking results where needed.
        Ensure to handle case sensitivity using ILIKE for string comparisons or convert the string column values to UPPER when comparing.
        Use LOWER() to handle case-insensitive matches when required.
        Ensure proper handling of NULL and invalid dates using the TRY_TO_DATE function.
        Do not include explanations or comments, only the SQL query itself.
        The question is:
        {{question}}
        """,
        input_variables=["question"]
    )

    # Initialize the ChatOpenAI model
    chat_model = ChatOpenAI(
        temperature=0, 
        model_name="gpt-4", 
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Generate the SQL query
    query = chat_model.predict(prompt.format(question=question))
    return query.strip()

def execute_query_and_summarize(query):
    conn = snowflake.connector.connect(
        user = st.secrets["SNOWFLAKE_USER"],
        password = st.secrets["SNOWFLAKE_PASSWORD"],
        account = st.secrets["SNOWFLAKE_ACCOUNT"],
        warehouse = st.secrets["SNOWFLAKE_WAREHOUSE"],
        database = st.secrets["SNOWFLAKE_DATABASE"],
        schema = st.secrets["SNOWFLAKE_SCHEMA"]
    )
    cursor = conn.cursor()

    try:
        # Execute the query
        cursor.execute(query)
        results = cursor.fetchall()

        # Get column names for results
        columns = [col[0] for col in cursor.description]
        results_df = pd.DataFrame(results, columns=columns)

        # Summarize the results
        if not results_df.empty:
            summary = f"The query returned {len(results_df)} rows."
            if len(results_df) > 0:
                summary += f" Example result: {results_df.iloc[0].to_dict()}"
        else:
            summary = "The query returned no results."
    except Exception as e:
        summary = f"An error occurred: {str(e)}"
        results_df = pd.DataFrame()

    # Close the connection
    cursor.close()
    conn.close()

    return results_df, summary
