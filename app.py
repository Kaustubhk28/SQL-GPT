# import os
# import streamlit as st
# from fetch_data import fetch_data
# from langchain_utils import generate_sql_query, execute_query_and_summarize
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Custom styles
# st.set_page_config(
#     page_title="IPL Data Chatbot",
#     page_icon="🏏",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # Main Title
# st.markdown(
#     """
#     <style>
#         .main-title {
#             text-align: center;
#             color: #4CAF50;
#             font-size: 2.5rem;
#             font-weight: bold;
#         }
#         .subtitle {
#             text-align: center;
#             color: #555555;
#             font-size: 1.2rem;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
# st.markdown('<div class="main-title">🏏 IPL Data Chatbot</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Ask Questions About IPL Data (2008-2024)</div>', unsafe_allow_html=True)

# # Sidebar
# st.sidebar.title("⚙️ Options")
# st.sidebar.info("Use this chatbot to query IPL data using natural language.")

# # Input Section
# st.markdown("<h3>📋 Enter Your Query</h3>", unsafe_allow_html=True)
# question = st.text_input(
#     "Type your question below (e.g., 'Which team scored the most runs in 2023?')",
#     placeholder="Ask your question...",
#     key="question_input",
# )

# # Submit Button
# if st.button("Submit 🟢"):
#     if question:
#         with st.spinner("🤖 Processing your query..."):
#             try:
#                 # Generate SQL query
#                 sql_query = generate_sql_query(question)

#                 # Display generated SQL query
#                 st.markdown("<h4>🛠️ Generated SQL Query</h4>", unsafe_allow_html=True)
#                 st.code(sql_query, language="sql")

#                 # Execute query
#                 results, summary = execute_query_and_summarize(sql_query)

#                 # Results Section
#                 st.markdown("<h4>📊 Query Results</h4>", unsafe_allow_html=True)
#                 if not results.empty:
#                     st.dataframe(results, use_container_width=True)

#                     # Add export button
#                     csv = results.to_csv(index=False).encode("utf-8")
#                     st.download_button(
#                         label="📥 Download Results as CSV",
#                         data=csv,
#                         file_name="query_results.csv",
#                         mime="text/csv",
#                     )

#                 # Validation Section
#                 st.markdown("<h4>✅ Validation</h4>", unsafe_allow_html=True)
#                 st.info("Results validated successfully against the database.")
#             except Exception as e:
#                 st.error(f"❌ An error occurred while processing your query: {e}")
#     else:
#         st.warning("Please enter a question to proceed.")

# # Footer
# st.markdown(
#     """
#     ---
#     <div style="text-align: center; color: #888;">
#         Built with ❤️ using Streamlit
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

import streamlit as st
from fetch_data import fetch_data
from langchain_utils import generate_sql_query, execute_query_and_summarize

# Streamlit secrets for configuration
SNOWFLAKE_USER = st.secrets["SNOWFLAKE_USER"]
SNOWFLAKE_PASSWORD = st.secrets["SNOWFLAKE_PASSWORD"]
SNOWFLAKE_ACCOUNT = st.secrets["SNOWFLAKE_ACCOUNT"]
SNOWFLAKE_DATABASE = st.secrets["SNOWFLAKE_DATABASE"]
SNOWFLAKE_SCHEMA = st.secrets["SNOWFLAKE_SCHEMA"]
SNOWFLAKE_WAREHOUSE = st.secrets["SNOWFLAKE_WAREHOUSE"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Custom styles
st.set_page_config(
    page_title="IPL Data Chatbot",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Main Title
st.markdown(
    """
    <style>
        .main-title {
            text-align: center;
            color: #4CAF50;
            font-size: 2.5rem;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            color: #555555;
            font-size: 1.2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<div class="main-title">🏏 IPL Data Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask Questions About IPL Data (2008-2024)</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("⚙️ Options")
st.sidebar.info("Use this chatbot to query IPL data using natural language.")

# Input Section
st.markdown("<h3>📋 Enter Your Query</h3>", unsafe_allow_html=True)
question = st.text_input(
    "Type your question below (e.g., 'Which team scored the most runs in 2023?')",
    placeholder="Ask your question...",
    key="question_input",
)

# Submit Button
if st.button("Submit 🟢"):
    if question:
        with st.spinner("🤖 Processing your query..."):
            try:
                # Generate SQL query
                sql_query = generate_sql_query(question, OPENAI_API_KEY)

                # Display generated SQL query
                st.markdown("<h4>🛠️ Generated SQL Query</h4>", unsafe_allow_html=True)
                st.code(sql_query, language="sql")

                # Execute query
                results, summary = execute_query_and_summarize(
                    sql_query,
                    # SNOWFLAKE_USER,
                    # SNOWFLAKE_PASSWORD,
                    # SNOWFLAKE_ACCOUNT,
                    # SNOWFLAKE_DATABASE,
                    # SNOWFLAKE_SCHEMA,
                    # SNOWFLAKE_WAREHOUSE,
                )

                # Results Section
                st.markdown("<h4>📊 Query Results</h4>", unsafe_allow_html=True)
                if not results.empty:
                    st.dataframe(results, use_container_width=True)

                    # Add export button
                    csv = results.to_csv(index=False).encode("utf-8")
                    st.download_button(
                        label="📥 Download Results as CSV",
                        data=csv,
                        file_name="query_results.csv",
                        mime="text/csv",
                    )

                # Validation Section
                st.markdown("<h4>✅ Validation</h4>", unsafe_allow_html=True)
                st.info("Results validated successfully against the database.")
            except Exception as e:
                st.error(f"❌ An error occurred while processing your query: {e}")
    else:
        st.warning("Please enter a question to proceed.")

# Footer
st.markdown(
    """
    ---
    <div style="text-align: center; color: #888;">
        Built with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
