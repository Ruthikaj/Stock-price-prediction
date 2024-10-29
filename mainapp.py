import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
""")

# User input for the ticker symbol
user_input = st.text_input("Enter a Ticker Symbol (e.g., GOOGL, AAPL, MSFT)", "GOOGL")

# Get data on the user-specified ticker
tickerData = yf.Ticker(user_input)
try:
    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
    st.write(f"## Stock Closing Price of {user_input}")
    st.line_chart(tickerDf['Close'])

    st.write(f"## Stock Volume of {user_input}")
    st.line_chart(tickerDf['Volume'])
except:
    st.write("Invalid Ticker Symbol. Please enter a valid ticker symbol.")
