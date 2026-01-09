import streamlit as st
import requests

st.title("Simple Add with Backend")

x = st.number_input("Enter X", value=0)
y = st.number_input("Enter Y", value=0)

if st.button("Add"):
    try:
        response = requests.post("http://localhost:5000/add", json={"x": x, "y": y}) #Streamlit sends those values to Flask:
        result = response.json()["result"]
        st.success(f"The result is: {result}")
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to the backend. Make sure the Flask server is running.")
