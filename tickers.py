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
    "TTWO": "Take-Two Interactive Software Inc.",
    "SONY": "Sony Group Corporation",
    "NTDOY": "Nintendo Co. Ltd.",
    "CDNS": "Cadence Design Systems Inc.",
    "SNPS": "Synopsys Inc.",
    "ANSS": "ANSYS Inc.",
    "AVPT": "AvePoint, Inc.",
    # swedish stocks
    "ERIC-B.ST": "Ericsson (Telefonaktiebolaget L M Ericsson)",
    "VOLV-B.ST": "AB Volvo",
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
    "ABB.ST": "ABB Ltd.",
    "AZN.ST": "AstraZeneca PLC",
    "EQT.ST": "EQT AB",
    "SECU-B.ST": "Securitas AB",
    "AXFO.ST": "Axfood AB",
    "BALD-B.ST": "Balder AB",
    "CAST.ST": "Castellum AB",
    "DIOS.ST": "Dios Fastigheter AB",
    "FABG.ST": "Fabege AB",
    "HM-B.ST": "H&M Hennes & Mauritz AB",
    "INVE-B.ST": "Investor AB",
    "JM.ST": "JM AB",
    "KIND-SDB.ST": "Kindred Group plc",
    "LIFCO-B.ST": "Lifco AB",
    "NP3.ST": "NP3 Fastigheter AB",
    "PEAB-B.ST": "Peab AB",
    "RATO-B.ST": "Ratos AB",
    "SECT-B.ST": "Sectra AB",
    "SINCH.ST": "Sinch AB",
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
    "VOLO.ST": "Volvo AB",
    "AAK.ST": "AAK AB",
    "G5EN.ST": "G5 Entertainment AB",
    "LUMI.ST": "Loomis AB",
    "RESURS.ST": "Resurs Holding AB",
    "TIGO": "Millicom International Cellular S.A.",
    "TIGO-SDB.ST": "Millicom International Cellular S.A. (Swedish)",
    # Sweden
    "^OMX": "OMX Stockholm 30",
    "^OMXSPI": "OMX Stockholm All-Share Index",

    # United States Major Indices
    "^GSPC": "S&P 500",
    "^DJI": "Dow Jones Industrial Average",
    "^IXIC": "NASDAQ Composite",
    "^NYA": "NYSE Composite (DJ)",
    "^XAX": "NYSE AMEX Composite Index",
    "^RUT": "Russell 2000",
    "^VIX": "CBOE Volatility Index",

    # Additional US Indices
    "^SP400": "S&P MidCap 400",
    "^SP600": "S&P SmallCap 600",
    "^NDX": "NASDAQ-100",
    "^SOX": "PHLX Semiconductor Index",
    "^TRAN": "Dow Jones Transportation Average",
    "^RUA": "Russell 3000",
    "^RUI": "Russell 1000",
    "^XMI": "NYSE ARCA Major Market Index",

    # United Kingdom
    "^FTSE": "FTSE 100",

    # Germany
    "^GDAXI": "DAX Performance Index",

    # France
    "^FCHI": "CAC 40",

    # Europe
    "^STOXX50E": "EURO STOXX 50",
    "^N100": "Euronext 100 Index",
    "^BFX": "BEL 20",

    # Russia
    "MOEX.ME": "Moscow Exchange MICEX-RTS",

    # Hong Kong
    "^HSI": "Hang Seng Index",

    # Singapore
    "^STI": "STI Index",

    # Australia
    "^AXJO": "S&P/ASX 200",
    "^AORD": "ALL ORDINARIES",

    # India
    "^BSESN": "S&P BSE SENSEX",

    # Indonesia
    "^JKSE": "IDX Composite",

    # Malaysia
    "^KLSE": "FTSE Bursa Malaysia KLCI",

    # New Zealand
    "^NZ50": "S&P/NZX 50 Index Gross",

    # South Korea
    "^KS11": "KOSPI Composite Index",

    # Taiwan
    "^TWII": "TSEC Weighted Index",

    # Canada
    "^GSPTSE": "S&P/TSX Composite Index",

    # Brazil
    "^BVSP": "IBOVESPA",

    # Mexico
    "^MXX": "IPC Mexico",

    # Chile
    "^IPSA": "S&P IPSA",

    # Argentina
    "^MERV": "MERVAL",

    # Israel
    "^TA125.TA": "TA-125",

    # South Africa
    "^JN0U.JO": "Top 40 USD Net TRI Index",

    # Currencies (US Dollar, British Pound, Euro, Yen, Australian Dollar)
    "DX-Y.NYB": "US Dollar Index",
    "^XDB": "British Pound Currency Index",
    "^XDE": "Euro Currency Index",
    "^XDN": "Japanese Yen Currency Index",
    "^XDA": "Australian Dollar Currency Index",

    # China
    "000001.SS": "SSE Composite Index",

    # Japan
    "^N225": "Nikkei 225",

    # Add more popular US indices
    "^DJT": "Dow Jones Transportation Average",
    "^DJU": "Dow Jones Utility Average",
    "^DWCF": "Dow Jones U.S. Total Stock Market Index",
    "^W5000": "Wilshire 5000 Total Market Index"
}
