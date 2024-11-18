import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from io import BytesIO

# Title and description
st.title("Stock Data Downloader")
st.write(
    "Download stock market data for up to 20 symbols from Yahoo Finance, "
    "limited to daily Closing Price or Adjusted Closing Price, and export it to Excel."
)

tickers = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc.",
    "AMZN": "Amazon.com Inc.",
    "TSLA": "Tesla Inc.",
    "META": "Meta Platforms Inc.",
    "NFLX": "Netflix Inc.",
    "NVDA": "NVIDIA Corporation",
    "AMD": "Advanced Micro Devices Inc.",
    "INTC": "Intel Corporation",
    "BABA": "Alibaba Group Holding Ltd.",
    "V": "Visa Inc.",
    "JPM": "JPMorgan Chase & Co.",
    "WMT": "Walmart Inc.",
    "PG": "Procter & Gamble Co.",
    "UNH": "UnitedHealth Group Inc.",
    "DIS": "The Walt Disney Company",
    "MA": "Mastercard Inc.",
    "HD": "The Home Depot Inc.",
    "PYPL": "PayPal Holdings Inc.",
    "COST": "Costco Wholesale Corporation",
    "PEP": "PepsiCo Inc.",
    "KO": "Coca-Cola Company",
    "NKE": "Nike Inc.",
    "MRK": "Merck & Co. Inc.",
    "PFE": "Pfizer Inc.",
    "ABT": "Abbott Laboratories",
    "T": "AT&T Inc.",
    "VZ": "Verizon Communications Inc.",
    "CSCO": "Cisco Systems Inc.",
    "XOM": "Exxon Mobil Corporation",
    "CVX": "Chevron Corporation",
    "BA": "Boeing Company",
    "MMM": "3M Company",
    "CAT": "Caterpillar Inc.",
    "GE": "General Electric Company",
    "IBM": "International Business Machines Corporation",
    "ORCL": "Oracle Corporation",
    "ADBE": "Adobe Inc.",
    "CRM": "Salesforce Inc.",
    "SQ": "Block Inc.",
    "SPOT": "Spotify Technology S.A.",
    "UBER": "Uber Technologies Inc.",
    "LYFT": "Lyft Inc.",
    "TWTR": "Twitter Inc.",
    "SNAP": "Snap Inc.",
    "SHOP": "Shopify Inc.",
    "ETSY": "Etsy Inc.",
    "ROKU": "Roku Inc.",
    "ZM": "Zoom Video Communications Inc.",
    "PLTR": "Palantir Technologies Inc.",
    "SPCE": "Virgin Galactic Holdings Inc.",
    "NKLA": "Nikola Corporation",
    "QS": "QuantumScape Corporation",
    "DKNG": "DraftKings Inc.",
    "PTON": "Peloton Interactive Inc.",
    "BYND": "Beyond Meat Inc.",
    "DOCU": "DocuSign Inc.",
    "CRWD": "CrowdStrike Holdings Inc.",
    "ZS": "Zscaler Inc.",
    "DDOG": "Datadog Inc.",
    "NET": "Cloudflare Inc.",
    "MDB": "MongoDB Inc.",
    "FSLY": "Fastly Inc.",
    "OKTA": "Okta Inc.",
    "TEAM": "Atlassian Corporation Plc",
    "PANW": "Palo Alto Networks Inc.",
    "SPLK": "Splunk Inc.",
    "NOW": "ServiceNow Inc.",
    "WDAY": "Workday Inc.",
    "F": "Ford Motor Company",
    "GM": "General Motors Company",
    "TM": "Toyota Motor Corporation",
    "HMC": "Honda Motor Co. Ltd.",
    "RIVN": "Rivian Automotive Inc.",
    "LCID": "Lucid Group Inc.",
    "TSM": "Taiwan Semiconductor Manufacturing Company",
    "ASML": "ASML Holding N.V.",
    "NXPI": "NXP Semiconductors N.V.",
    "QCOM": "QUALCOMM Incorporated",
    "AVGO": "Broadcom Inc.",
    "TXN": "Texas Instruments Inc.",
    "LRCX": "Lam Research Corporation",
    "AMAT": "Applied Materials Inc.",
    "MU": "Micron Technology Inc.",
    "KLAC": "KLA Corporation",
    "STX": "Seagate Technology Holdings Plc",
    "WDC": "Western Digital Corporation",
    "ADSK": "Autodesk Inc.",
    "EA": "Electronic Arts Inc.",
    "ATVI": "Activision Blizzard Inc.",
    "TTWO": "Take-Two Interactive Software Inc.",
    "SONY": "Sony Group Corporation",
    "NTDOY": "Nintendo Co. Ltd.",
    "CDNS": "Cadence Design Systems Inc.",
    "SNPS": "Synopsys Inc.",
    "ANSS": "ANSYS Inc.",
    "ERIC-B.ST": "Ericsson (Telefonaktiebolaget L M Ericsson)",
    "VOLV-B.ST": "AB Volvo",
    "HMB.ST": "Hennes & Mauritz AB",
    "SAND.ST": "Sandvik AB",
    "ATCO-A.ST": "Atlas Copco AB",
    "ATCO-B.ST": "Atlas Copco AB Series B",
    "ALFA.ST": "Alfa Laval AB",
    "ASSA-B.ST": "ASSA ABLOY AB",
    "BOL.ST": "Boliden AB",
    "ELUX-B.ST": "Electrolux AB",
    "GETI-B.ST": "Getinge AB",
    "HEXA-B.ST": "Hexagon AB",
    "INDT.ST": "Industrivärden AB",
    "KINV-B.ST": "Kinnevik AB",
    "LATO-B.ST": "Latour AB",
    "LUND-B.ST": "Lundin Energy AB",
    "MTG-B.ST": "Modern Times Group MTG AB",
    "NDA-SE.ST": "Nordea Bank Abp",
    "SEB-A.ST": "Skandinaviska Enskilda Banken AB",
    "SHB-A.ST": "Svenska Handelsbanken AB",
    "SKF-B.ST": "SKF AB",
    "SSAB-A.ST": "SSAB AB",
    "SSAB-B.ST": "SSAB AB Series B",
    "SWED-A.ST": "Swedbank AB",
    "TEL2-B.ST": "Tele2 AB",
    "TELIA.ST": "Telia Company AB",
    "TRATON.ST": "Traton SE",
    "WALL-B.ST": "Wallenius Wilhelmsen ASA",
    "ABB.ST": "ABB Ltd.",
    "AZN.ST": "AstraZeneca PLC",
    "EQT.ST": "EQT AB",
    "SECU-B.ST": "Securitas AB",
    "SCAB.ST": "Scandinavian Tobacco Group A/S",
    "AXFO.ST": "Axfood AB",
    "BALD-B.ST": "Balder AB",
    "CAST.ST": "Castellum AB",
    "DIOS.ST": "Dios Fastigheter AB",
    "FABG.ST": "Fabege AB",
    "HM-B.ST": "H&M Hennes & Mauritz AB",
    "INVE-B.ST": "Investor AB",
    "JM.ST": "JM AB",
    "KIND-SDB.ST": "Kindred Group plc",
    "KLOV.ST": "Klövern AB",
    "LIFCO-B.ST": "Lifco AB",
    "NP3.ST": "NP3 Fastigheter AB",
    "PEAB-B.ST": "Peab AB",
    "RATO-B.ST": "Ratos AB",
    "SECT-B.ST": "Sectra AB",
    "SINCH.ST": "Sinch AB",
    "SWMA.ST": "Swedish Match AB",
    "THULE.ST": "Thule Group AB",
    "TREL-B.ST": "Trelleborg AB",
    "VIT-B.ST": "Vitrolife AB",
    "ALM.ST": "Alm Equity AB",
    "CIBUS.ST": "Cibus Nordic Real Estate AB",
    "CORE-B.ST": "Corem Property Group AB",
    "NYF.ST": "Nyfosa AB",
    "VESTUM.ST": "Vestum AB",
    "SBB-B.ST": "Samhällsbyggnadsbolaget i Norden AB",
    "WIHL.ST": "Wihlborgs Fastigheter AB",
    "GARO.ST": "Garo AB",
    "ZETB.ST": "ZetaDisplay AB",
    "VOLO.ST": "Volvo AB",
    "AAK.ST": "AAK AB",
    "STORB.ST": "Storskogen Group AB",
    "G5EN.ST": "G5 Entertainment AB",
    "QIFAB.ST": "Questerre Energy Corporation",
    "LUMI.ST": "Loomis AB",
    "RESURS.ST": "Resurs Holding AB",
    "TRIAN.ST": "TriOptima AB"
}


# Convert tickers dictionary to a list of "Ticker: Company Name" for dropdown
dropdown_options = [f"{ticker}: {name}" for ticker, name in tickers.items()]

# Symbol selection
st.write("### Select Symbols")
selected_options = st.multiselect(
    "Choose up to 20 stock symbols from the list below:",
    options=dropdown_options,
    default=["AAPL: Apple Inc.", "MSFT: Microsoft Corporation",
             "GOOGL: Alphabet Inc."],  # Default selections
    max_selections=20,
)

# Extract selected tickers
selected_symbols = [option.split(":")[0].strip()
                    for option in selected_options]

# Validate symbol count
if len(selected_symbols) > 20:
    st.error("You can select a maximum of 20 symbols. Please adjust your input.")

# Input for custom tickers
custom_tickers = st.text_input(
    "Enter additional ticker symbols (comma-separated, e.g., FB, NFLX, NVDA):",
    "",
)
custom_symbols_list = [sym.strip().upper()
                       for sym in custom_tickers.split(",") if sym.strip()]
all_symbols = list(set(selected_symbols + custom_symbols_list))

# Data type selection: Closing Price or Adjusted Closing Price
st.write("### Select Data Type")
data_type = st.radio(
    "Select the type of data to download:",
    options=["Closing Price", "Adjusted Closing Price"],
    index=1,
)

# Date inputs for the start and end dates
start_date = st.date_input(
    "Start Date", value=datetime.today() - timedelta(days=365 * 3))
end_date = st.date_input("End Date", value=datetime.today())

# Function to fetch stock data


def fetch_stock_data(tickers, start_date, end_date):
    # Increment the end_date by one day to ensure it's included, as by default Yahoo excludes the last date
    adjusted_end_date = end_date + timedelta(days=1)

    data_frames = []
    for ticker in tickers:
        try:
            # Download daily data
            df = yf.download(ticker, start=start_date,
                             end=adjusted_end_date, progress=False, interval="1d")
            if df.empty:
                st.warning(f"No data found for {
                           ticker}. Check the ticker symbol or adjust the date range.")
            else:
                if data_type == "Closing Price":
                    df = df[["Close"]]
                elif data_type == "Adjusted Closing Price":
                    df = df[["Adj Close"]]

                # Rename the column to the ticker name
                df.rename(columns={df.columns[0]: ticker}, inplace=True)

                # Ensure the index is formatted as a date string without time
                df.index = df.index.date

                data_frames.append(df)
        except Exception as e:
            st.error(f"Error fetching data for {ticker}: {e}")
    if not data_frames:
        return None
    return pd.concat(data_frames, axis=1)


# Button to fetch data
if st.button("Download Data"):
    if not all_symbols:
        st.error("Please select or enter at least one stock symbol.")
    else:
        with st.spinner("Fetching stock data..."):
            stock_data = fetch_stock_data(all_symbols, start_date, end_date)

            if stock_data is not None:
                # Reset index to move the date into a column
                stock_data.reset_index(inplace=True)

                # Rename the date column
                stock_data.rename(columns={"index": "Date"}, inplace=True)

                # Flatten MultiIndex columns (if present)
                if isinstance(stock_data.columns, pd.MultiIndex):
                    stock_data.columns = [col[1] if isinstance(
                        col, tuple) else col for col in stock_data.columns]

                st.write("### Data Preview")
                st.write("#### Head:")
                st.dataframe(stock_data.head())
                st.write("#### Tail:")
                st.dataframe(stock_data.tail())

                # Save as Excel using pandas
                output = BytesIO()
                try:
                    stock_data.to_excel(output, index=False,
                                        sheet_name="Stock Data")
                    excel_data = output.getvalue()

                    # Provide download button for Excel
                    st.download_button(
                        label="Download Excel File",
                        data=excel_data,
                        file_name="stock_data.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    )
                except Exception as e:
                    st.error(f"Failed to save data to Excel: {e}")
            else:
                st.error(
                    "No valid data fetched. Please check your symbols and date range.")

# Code snippet for users
st.write("### How to Read the Downloaded File in Python")
st.write('This code will read the downloaded excel file FROM the "Downloads" folder')
code_snippet = """
import os
import pandas as pd

# Default path to the Downloads folder (update if needed)
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
file_path = os.path.join(downloads_folder, "stock_data.xlsx")

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Display the first few rows
print(df.head())
"""
st.code(code_snippet, language="python")
