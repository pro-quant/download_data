import streamlit as st
import yfinance as yf
import pandas as pd

# Title and description
st.title("Stock Data Downloader")
st.write(
    "Download stock market data for up to 10 symbols from Yahoo Finance, "
    "limited to Closing Price or Adjusted Closing Price, and export it to CSV."
)

# Predefined list of 100 tickers
tickers = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NFLX", "NVDA", "AMD", "INTC",
    "BABA", "V", "JPM", "WMT", "PG", "UNH", "DIS", "MA", "HD", "PYPL",
    "COST", "PEP", "KO", "NKE", "MRK", "PFE", "ABT", "T", "VZ", "CSCO",
    "XOM", "CVX", "BA", "MMM", "CAT", "GE", "IBM", "ORCL", "ADBE", "CRM",
    "SQ", "SPOT", "UBER", "LYFT", "TWTR", "SNAP", "SHOP", "ETSY", "ROKU", "ZM",
    "PLTR", "SPCE", "NKLA", "QS", "DKNG", "PTON", "BYND", "DOCU", "CRWD", "ZS",
    "DDOG", "NET", "MDB", "FSLY", "OKTA", "TEAM", "PANW", "SPLK", "NOW", "WDAY",
    "F", "GM", "TM", "HMC", "RIVN", "LCID", "TSM", "ASML", "NXPI", "QCOM",
    "AVGO", "TXN", "LRCX", "AMAT", "MU", "KLAC", "STX", "WDC", "WDAY", "ADSK",
    "EA", "ATVI", "TTWO", "UBSFY", "SONY", "NTDOY", "CDNS", "SNPS", "ANSS", "MENT"
]

# Symbol selection
st.write("### Select Symbols")
selected_symbols = st.multiselect(
    "Choose up to 10 stock symbols from the list below:",
    options=tickers,
    default=tickers[:5],
    max_selections=10,
)

# Data type selection: Closing Price or Adjusted Closing Price
st.write("### Select Data Type")
data_type = st.radio(
    "Select the type of data to download:",
    options=["Closing Price", "Adjusted Closing Price"],
    index=1,
)

# Date inputs for the start and end dates
start_date = st.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2023-01-01"))

# Button to fetch data
if st.button("Download Data"):
    if not selected_symbols:
        st.error("Please select at least one stock symbol.")
    else:
        try:
            # Fetch data for all selected symbols
            all_data = {}
            for symbol in selected_symbols:
                st.write(f"Fetching {data_type} for {symbol}...")
                data = yf.download(symbol, start=start_date, end=end_date, progress=False)
                if data_type == "Closing Price":
                    all_data[symbol] = data["Close"]
                elif data_type == "Adjusted Closing Price":
                    all_data[symbol] = data["Adj Close"]

            if all_data:
                # Combine data into one DataFrame
                combined_data = pd.DataFrame(all_data)
                st.write("### Data Preview")
                st.write("#### Head:")
                st.dataframe(combined_data.head())
                st.write("#### Tail:")
                st.dataframe(combined_data.tail())

                # Convert combined data to CSV
                csv_data = combined_data.to_csv().encode("utf-8")
                st.download_button(
                    label="Download CSV",
                    data=csv_data,
                    file_name="stock_data.csv",
                    mime="text/csv",
                )
            else:
                st.error("No valid data fetched. Please check your symbols and date range.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
