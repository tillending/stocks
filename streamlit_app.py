import streamlit as st
# import pandas as pd
import yfinance as f

st.write("""
# My first app
Hello *world!*
""")

df = pd.read_csv("my_data.csv")
st.line_chart(df)
