import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Function to fetch stock data
def fetch_stock_data(tickers, start_date, end_date):
    data_frames = []
    errors = []
    for ticker in tickers:
        try:
            # Download adjusted close prices
            df = yf.download(ticker, start=start_date, end=end_date, progress=False)[["Adj Close"]]
            if df.empty:
                errors.append(f"No data found for {ticker}.")
            else:
                df.rename(columns={"Adj Close": ticker}, inplace=True)
                data_frames.append(df)
        except Exception as e:
            errors.append(f"Error fetching data for {ticker}: {e}")
    # Combine all valid data into a single DataFrame
    combined_data = pd.concat(data_frames, axis=1) if data_frames else None
    return combined_data, errors

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
            stock_data, errors = fetch_stock_data(tickers, start_date, end_date)

            # Display any errors
            if errors:
                st.warning("The following issues occurred while fetching data:")
                for error in errors:
                    st.warning(error)

            # Display fetched data
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
            else:
                st.error("No valid data available for the selected tickers.")
