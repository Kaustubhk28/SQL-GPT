# 🏏 IPL Data Chatbot

The **IPL Data Chatbot** is an interactive web application built with **Streamlit** that allows users to query IPL (Indian Premier League) data from 2008 to 2024 using natural language. The chatbot uses **OpenAI's GPT-4** to generate SQL queries dynamically and fetches data from a **Snowflake** database.

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

### 2. Clone the Repository

```bash
git clone https://github.com/Kaustubhk28/sql-gpt.git

