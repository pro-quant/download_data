import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Function to fetch stock data
def fetch_stock_data(tickers, start_date, end_date):
    data_frames = []
    for ticker in tickers:
        try:
            df = yf.download(ticker, start=start_date, end=end_date, progress=False)[["Adj Close"]]
            if df.empty:
                st.warning(f"No data found for {ticker}. Check the ticker symbol or adjust the date range.")
            else:
                df.rename(columns={"Adj Close": ticker}, inplace=True)
                data_frames.append(df)
        except Exception as e:
            st.error(f"Error fetching data for {ticker}: {e}")
    if not data_frames:
        return None
    return pd.concat(data_frames, axis=1)

# Streamlit UI
st.title("Stock Data Downloader")
st.markdown(
    "Enter up to 10 ticker symbols, and this app will fetch the adjusted closing prices for the specified date range."
)

# Sidebar inputs
st.sidebar.header("Input Parameters")
tickers = st.sidebar.text_input("Enter up to 10 Ticker Symbols (comma-separated)", value="AAPL, MSFT, META")
tickers = [ticker.strip().upper() for ticker in tickers.split(",")]

if len(tickers) > 10:
    st.error("Please enter no more than 10 ticker symbols.")
else:
    start_date = st.sidebar.date_input("Start Date", value=datetime.today() - timedelta(days=365 * 3))
    end_date = st.sidebar.date_input("End Date", value=datetime.today())

    if st.button("Fetch Data"):
        with st.spinner("Fetching stock data..."):
            stock_data = fetch_stock_data(tickers, start_date, end_date)

            if stock_data is not None:
                st.subheader("Stock Data Preview")
                st.write(stock_data)

                # Convert the DataFrame to CSV for download
                csv_data = stock_data.to_csv(index=True)
                st.download_button(
                    label="Download CSV",
                    data=csv_data,
                    file_name="stock_data.csv",
                    mime="text/csv",
                )
