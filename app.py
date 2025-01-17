import streamlit as st
from dotenv import load_dotenv

load_dotenv()
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("API_KEY"))

def get_gemini_response(query, prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt,query])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt='\nYou are an expert in converting English questions to SQL queries! The SQL database has the name STUDENT and the following columns: "NAME", "CLASS", "SECTION","MARKS". \n\nFor example:\n\nExample1: How many entries of the records are present?, The SQL command will be something like SELECT * FROM STUDENT ;\n\nExample2: Tell me all the students studying in the data science class?, The SQL command will be something like SELECT * FROM STUDENT WHERE CLASS="Data Science" ; \nAlso, the SQL should not have ``` in the beginning or end and sql word in the output.\n'

st.set_page_config(page_title="Retrieving SQL Query")
st.header("Gemini App to retrieve SqL Query")
query=st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(query,prompt)
    data=read_sql_query(response, "student.db")
    st.header("The response is")
    for row in data:
        print(row)
        st.header(row)
