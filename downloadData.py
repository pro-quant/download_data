import streamlit as st
import yfinance as yf
import pandas as pd

# Title and description
st.title("Stock Data Downloader")
st.write(
    "Download stock market data for up to 10 symbols from Yahoo Finance, view it, and export it to CSV."
)

# Default ticker symbols
default_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

# Symbol selection
st.write("### Select Symbols")
selected_symbols = st.multiselect(
    "Choose stock symbols from the defaults or enter custom symbols below:",
    options=default_symbols,
    default=default_symbols[:2],
)
custom_symbols = st.text_area(
    "Enter up to 10 custom symbols (comma-separated):",
    "",
    placeholder="e.g., FB, NFLX, NVDA",
)
custom_symbols_list = [sym.strip().upper() for sym in custom_symbols.split(",") if sym.strip()]
all_symbols = selected_symbols + custom_symbols_list
all_symbols = list(set(all_symbols))  # Remove duplicates

if len(all_symbols) > 10:
    st.error("You can select a maximum of 10 symbols. Please adjust your input.")

# Data type selection: Adjusted Close or Close
st.write("### Select Data Type")
data_type = "Adj Close" if st.checkbox("Fetch Adjusted Closing Price", value=True) else "Close"

# Date inputs for the start and end dates
start_date = st.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2023-01-01"))

# Button to fetch data
if st.button("Download Data"):
    if not all_symbols:
        st.error("Please select at least one stock symbol.")
    else:
        try:
            # Fetch data for all symbols
            all_data = {}
            for symbol in all_symbols:
                st.write(f"Fetching {data_type} data for {symbol}...")
                data = yf.download(symbol, start=start_date, end=end_date)
                if not data.empty:
                    all_data[symbol] = data[data_type]
                else:
                    st.warning(f"No data found for {symbol}.")

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
