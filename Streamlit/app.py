import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Analysis App")   # streamlit run app.py --server.address localhost
st.write("This is a simple data analysis app using Streamlit.")

df= pd.DataFrame({
    'Column1': np.random.randn(100),
    'Column2': np.random.rand(100)
})

st.write(df)

createchart = pd.DataFrame({
    'x': np.arange(100),
    'y': np.random.rand(100)
})
st.line_chart(createchart)
