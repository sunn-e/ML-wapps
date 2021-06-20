import yfinance as yf
import streamlit as st
import pandas as pf
from datetime import datetime

st.write("""
    # Stock price App
    
    **Google** stock **closing** price and **volume**
    """)

tickerSymbol = "GOOGL"
googleIPODate = "2004-8-18"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(
    period="1d", start=googleIPODate, end=datetime.today())


st.write("""
        ## Closing Price
         
        From IPO Day to Today
        """)
st.line_chart(tickerDf.Close)
st.write("""##Volume Price""")
st.line_chart(tickerDf.Volume)
