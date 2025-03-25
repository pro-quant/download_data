import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from io import BytesIO
from tickers import tickers

# Title and description
st.title("Stock Data Downloader")
st.write(
    "Download stock market data for up to 20 symbols from Yahoo Finance, "
    "limited to daily Closing Price or Adjusted Closing Price, and download it as csv or excel file."
)


# Convert tickers dictionary to a list of "Ticker: Company Name" for dropdown
dropdown_options = [f"{ticker}: {name}" for ticker, name in tickers.items()]

# Symbol selection
st.write("### Select Symbols")
selected_options = st.multiselect(
    "Choose up to 20 stock symbols from the list below:",
    options=dropdown_options,
    default=["AAPL: Apple Inc.", "MSFT: Microsoft Corporation", "GOOGL: Alphabet Inc."],
    max_selections=20,
)

# Extract selected tickers
selected_symbols = [option.split(":")[0].strip() for option in selected_options]

# Input for custom tickers
custom_tickers = st.text_input(
    "Enter additional ticker symbols (comma-separated, e.g., FB, NFLX, NVDA):",
    "",
)
custom_symbols_list = [sym.strip().upper() for sym in custom_tickers.split(",") if sym.strip()]
all_symbols = list(set(selected_symbols + custom_symbols_list))

# Data type selection
st.write("### Select Data Type")
data_type = st.radio(
    "Select the type of data to download:",
    options=["Closing Price", "Adjusted Closing Price"],
    index=1,
)

# Date input
start_date = st.date_input("Start Date", value=datetime.today() - timedelta(days=365 * 4))
end_date = st.date_input("End Date", value=datetime.today())

# Function to fetch stock data with auto_adjust=False to access both 'Close' and 'Adj Close'
def fetch_stock_data(tickers, start_date, end_date):
    adjusted_end_date = end_date + timedelta(days=1)
    data_frames = []
    for ticker in tickers:
        try:
            df = yf.download(
                ticker,
                start=start_date,
                end=adjusted_end_date,
                progress=False,
                interval="1d",
                auto_adjust=False
            )
            if df.empty:
                st.warning(f"No data found for {ticker}. Check the ticker symbol or adjust the date range.")
            else:
                column = "Close" if data_type == "Closing Price" else "Adj Close"
                df = df[[column]]
                df.rename(columns={column: ticker}, inplace=True)
                df.index = df.index.date
                data_frames.append(df)
        except Exception as e:
            st.error(f"Error fetching data for {ticker}: {e}")
    if not data_frames:
        return None
    df_concat = pd.concat(data_frames, axis=1)
    df_concat = df_concat.loc[:, ~df_concat.columns.duplicated()]
    return df_concat

# Button to fetch data
if st.button("Fetch Data"):
    if not all_symbols:
        st.error("Please select or enter at least one stock symbol.")
    else:
        with st.spinner("Fetching stock data..."):
            stock_data = fetch_stock_data(all_symbols, start_date, end_date)

            if stock_data is not None:
                # Flatten MultiIndex columns if needed
                if isinstance(stock_data.columns, pd.MultiIndex):
                    stock_data.columns = [col[1] if isinstance(col, tuple) else col for col in stock_data.columns]

                # Reset index and set date column
                stock_data = stock_data.copy()
                stock_data.index.name = "Date"
                stock_data.reset_index(inplace=True)

                st.write("### Data Preview")
                st.write("#### Head:")
                st.dataframe(stock_data.head())
                st.write("#### Tail:")
                st.dataframe(stock_data.tail())

                output_excel = BytesIO()
                output_csv = BytesIO()
                try:
                    stock_data.to_excel(output_excel, index=False, sheet_name="Stock Data")
                    stock_data.to_csv(output_csv, index=False)
                    st.download_button(
                        label="Download Excel File",
                        data=output_excel.getvalue(),
                        file_name="stock_data.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    )
                    st.download_button(
                        label="Download CSV File",
                        data=output_csv.getvalue(),
                        file_name="stock_data.csv",
                        mime="text/csv",
                    )
                except Exception as e:
                    st.error(f"Failed to save data: {e}")
            else:
                st.error("No valid data fetched. Please check your symbols and date range.")

# Code snippet section
st.write("### How to Read the Downloaded File in Python and R")

st.write("#### Python: Read the Downloaded Excel File")
python_code_snippet = """
import os
import pandas as pd

# Reading downloaded file from the 'Downloads' folder
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
file_path = os.path.join(downloads_folder, "stock_data.xlsx")

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Display the first few rows
print(df.head())
"""
st.code(python_code_snippet, language="python")

st.write("#### R: Read the Downloaded Excel File")
r_code_snippet = """
# Load necessary library
library(readxl)

# Reading downloaded file from the 'Downloads' folder
downloads_folder <- file.path(Sys.getenv("USERPROFILE"), "Downloads")
file_path <- file.path(downloads_folder, "stock_data.xlsx")

# Read the Excel file into a data frame
df <- read_excel(file_path)

# Display the first few rows
print(head(df))
"""
st.code(r_code_snippet, language="r")
