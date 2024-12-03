# 🏏 IPL Data Chatbot

The **IPL Data Chatbot** is an interactive web application built with **Streamlit** that allows users to query IPL (Indian Premier League) data from 2008 to 2024 using natural language. The chatbot uses **OpenAI's GPT-4** to generate SQL queries dynamically and fetches data from a **Snowflake** database.

**🌐 [Try the IPL Data Chatbot Here](https://iplchatbot.streamlit.app/)**

---
## ✨ Features

- **Natural Language Querying**: Users can ask questions in plain English.
- **Dynamic SQL Generation**: Converts user queries into SQL using OpenAI GPT-4.
- **Real-Time Data Fetching**: Retrieves data from Snowflake and displays it in a user-friendly format.
- **Data Export**: Download query results as a CSV file.
- **Query Validation**: Ensures SQL queries are valid and data integrity is maintained.
- **Insights and Summaries**: Provides clear and concise summaries of query results.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **Database**: [Snowflake](https://www.snowflake.com/)
- **AI Integration**: [OpenAI GPT-4](https://openai.com/)
- **Environment Variables**: Managed using `st.secrets` in Streamlit.

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Streamlit
- Snowflake Python Connector
- OpenAI Python Library (`openai`)
  
---
### 2. Clone the Repository
```
git clone https://github.com/Kaustubhk28/sql-gpt.git
```
---

## ⚙️ Configure Environment Variables
To securely configure the application, use the following steps:

Navigate to the .streamlit directory in the project.

Create a secrets.toml file with the following content:

[general]
SNOWFLAKE_USER = "your_snowflake_username"
SNOWFLAKE_PASSWORD = "your_snowflake_password"
SNOWFLAKE_ACCOUNT = "your_snowflake_account"
SNOWFLAKE_DATABASE = "your_snowflake_database"
SNOWFLAKE_SCHEMA = "your_snowflake_schema"
SNOWFLAKE_WAREHOUSE = "your_snowflake_warehouse"
OPENAI_API_KEY = "your_openai_api_key"

Replace the placeholders (your_snowflake_username, your_openai_api_key, etc.) with your actual credentials.

---

## 🚀 Run the Application Locally
To run the application on your local machine:

Start the app:
```
streamlit run app.py
```
Open your web browser and navigate to:
```
http://localhost:8501
```
The application should now be running locally!

---

## 📁 Project Structure
Here’s a breakdown of the project structure:
```
ipl-data-chatbot/
├── app.py                # Main Streamlit application script
├── fetch_data.py         # Script for fetching data from Snowflake
├── langchain_utils.py    # Generates SQL queries using OpenAI GPT-4
├── requirements.txt      # Python dependencies
├── .streamlit/           
│   └── secrets.toml      # Environment variable configuration file
└── README.md             # Project documentation
```
---
🔗 IPL Data Chatbot

## 💡 Features
Natural Language Querying: Ask questions like, "Which team scored the most runs in 2023?"
Dynamic SQL Query Generation: Uses GPT-4 to convert natural language to SQL.
Interactive Results: View, validate, and download query results as CSV.
Secure Configuration: Sensitive credentials are stored securely using Streamlit's secrets.

---

## ❤️ Acknowledgments
Streamlit: For creating a powerful framework for interactive web apps.
OpenAI GPT-4: For natural language understanding and SQL generation.
Snowflake: For efficient and scalable database management.

