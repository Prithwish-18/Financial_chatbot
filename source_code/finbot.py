import google.generativeai as genai
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from io import BytesIO
from forex_python.converter import CurrencyRates, get_currency_name
import re
import requests
from bs4 import BeautifulSoup
from PIL import Image
import cv2
import numpy as np
import os


# Replace with your actual Gemini API key
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with your actual Gemini API key
genai.configure(api_key=API_KEY)

# Select the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

c = CurrencyRates()

# Simulated document content (unchanged for brevity)
DOCUMENT_CONTENT = """
Company
$3 \mathrm{~m}$                      MMM
a. o. smith                 AOS
abbott laboratories         ABT
abbvie                      ABBV
accenture                   ACN
adobe                       ADBE
advanced micro devices      AMD
aes corporation             AES
aflac                       AFL
agilent technologies        A
air products                APD
airbnb                      ABNB
akamai technologies         AKAM
albemarle corporation       ALB
alexandria real estate equities ARE
align technology            ALGN
allegion                    ALLE
alliant energy              LNT
allstate                    ALL
alphabet (class a)          GOOGL
alphabet (class c)          GOOG
altria                      MO
amazon                      AMZN
amcor                       AMCR
ameren                      AEE
american electric power     AEP
american express            AXP
american international group AIG
american tower              AMT
american water works        AWK
ameriprise financial        AMP
ametek                      AME
amgen                       AMGN
amphenol                    APH
analog devices              ADI
ansys                       ANSS
aon plc                     AON
apa corporation             APA
apollo global management    APO
apple                       AAPL
applied materials           AMAT
aptiv                       APTV
arch capital group          ACGL
archer daniels midland      ADM
arista networks             ANET
arthur j. gallagher \& co.  AJG
at\&t                       T
atmos energy                ATO
autodesk                    ADSK
automatic data processing   ADP
autozone                    AZO
avalonbay communities       AVB
avery dennison              AVY
axon enterprise             AXON
baker hughes                BKR
ball corporation            BALL
bank of america             BAC
baxter international        BAX
becton dickinson            BDX
berkshire hathaway          BRK.B
best buy                    BBY
bio-techne                  TECH
biogen                      BIIB
blackrock                   BLK
blackstone                  BX
bny mellon                  BK
boeing                      BA
booking holdings            BKNG
boston scientific           BSX
bristol myers squibb        BMY
broadcom                    AVGO
broadridge financial solutions BR
brown \& brown              BRO
brownå€"forman             BF.B
builders firstsource        BLDR
bunge global                BG
bxp,                        BXP
c.h. robinson               CHRW
cadence design systems      CDNS
caesars entertainment       CZR
camden property trust       CPT
campbell's company (the)    CPB
capital one                 COF
cardinal health             CAH
carmax                      KMX
carnival                    CCL
carrier global              CARR
caterpillar                 CAT
cboe global markets         CBOE
cbre group                  CBRE
cdw corporation             CDW
cencora                     COR
centene corporation         CNC
centerpoint energy          CNP
cf industries               CF
charles river laboratories  CRL
charles schwab corporation  SCHW
charter communications      CHTR
chevron corporation         CVX
chipotle mexican grill      CMG
chubb limited               CB
church \& dwight            CHD
cigna                       CI
cincinnati financial        CINF
cintas                      CTAS
cisco                       CSCO
citigroup                   C
citizens financial group    CFG
clorox                      CLX
cme group                   CME
cms energy                  CMS
coca-cola company (the)     KO
cognizant                   CTSH
colgate-palmolive           CL
comcast                     CMCSA
conagra brands              CAG
conocophillips              COP
consolidated edison         ED
constellation brands        STZ
constellation energy        CEG
cooper companies (the)      COO
copart                      CPRT
corning                     GLW
corpay                      CPAY
corteva                     CTVA
costar group                CSGP
costco                      COST
coterra                     CTRA
crowdstrike                 CRWD
crown castle                CCI
csx corporation             CSX
cummins                     CMI
cvs health                  CVS
danaher corporation         DHR
darden restaurants          DRI
davita                      DVA
dayforce                    DAY
deckers brands              DECK
deere \& company           DE
dell technologies           DELL
delta air lines             DAL
devon energy                DVN
dexcom                      DXCM
diamondback energy          FANG
digital realty              DLR
discover financial          DFS
dollar general              DG
dollar tree                 DLTR
dominion energy             D
domino's                    DPZ
doordash                    DASH
dover corporation           DOV
dow                         DOW
d. r. horton                DHI
dte energy                  DTE
duke energy                 DUK
dupont                      DD
eastman chemical company    EMN
eaton corporation           ETN
ebay                        EBAY
ecolab                      ECL
edison international        EIX
edwards lifesciences        EW
electronic arts             EA
elevance health             ELV
emerson electric            EMR
enphase energy              ENPH
entergy                     ETR
eog resources               EOG
epam systems                EPAM
eqt corporation             EQT
equifax                     EFX
equinix                     EQIX
equity residential          EQR
erie indemnity              ERIE
essex property trust        ESS
estă@e lauder companies (the) EL
everest group               EG
evergy                      EVRG
eversource energy           ES
exelon                      EXC
expand energy               EXE
expedia group               EXPE
expeditors international    EXPD
extra space storage         EXR
exxonmobil                  XOM
f5,                         FFIV
factset                     FDS
fair isaac                  FICO
fastenal                    FAST
federal realty investment trust FRT
fedex                       FDX
fidelity national information services FIS
fifth third bancorp         FITB
first solar                 FSLR
firstenergy                 FE
fiserv                      FI
ford motor company          F
fortinet                    FTNT
fortive                     FTV
fox corporation (class a)   FOXA
fox corporation (class b)   FOX
franklin resources          BEN
freeport-mcmoran            FCX
garmin                      GRMN
gartner                     IT
ge aerospace                GE
ge healthcare               GEHC
ge vernova                  GEV
gen digital                 GEN
generac                     GNRC
general dynamics            GD
general mills               GIS
general motors              GM
genuine parts company       GPC
gilead sciences             GILD
global payments             GPN
globe life                  GL
godaddy                     GDDY
goldman sachs               GS
halliburton                 HAL
hartford (the)              HIG
hasbro                      HAS
hca healthcare              HCA
healthpeak properties       DOC
henry schein                HSIC
hershey company (the)       HSY
hess corporation            HES
hewlett packard enterprise  HPE
hilton worldwide            HLT
hologic                     HOLX
home depot (the)            HD
honeywell                   HON
hormel foods                HRL
host hotels \& resorts      HST
howmet aerospace            HWM
hp                          HPQ
hubbell incorporated        HUBB
humana                      HUM
huntington bancshares       HBAN
huntington ingalls industries HII
ibm                         IBM
idex corporation            IEX
idexx laboratories          IDXX
illinois tool works         ITW
incyte                      INCY
ingersoll rand              IR
insulet corporation         PODD
intel                       INTC
intercontinental exchange   ICE
international flavors \& fragrances IFF
international paper         IP
interpublic group of companies (the) IPG
intuit                      INTU
intuitive surgical          ISRG
invesco                     IVZ
invitation homes            INVH
iqvia                       IQV
iron mountain               IRM
j.b. hunt                   JBHT
jabil                       JBL
jack henry \& associates    JKHY
jacobs solutions            J
johnson \& johnson          JNJ
johnson controls            JCI
jpmorgan chase              JPM
juniper networks            JNPR
kellanova                   K
kenvue                      KVUE
keurig dr pepper            KDP
keycorp                     KEY
keysight technologies       KEYS
kimberly-clark              KMB
kimco realty                KIM
kinder morgan               KMI
kkr \& co.                  KKR
kla corporation             KLAC
kraft heinz                 KHC
kroger                      KR
I3harris                    LHX
labcorp                     LH
lam research                LRCX
lamb weston                 LW
las vegas sands             LVS
leidos                      LDOS
lennar                      LEN
lennox international        LII
lilly (eli)                 LLY
linde plc                   LIN
live nation entertainment   LYV
Ikq corporation             LKQ
lockheed martin             LMT
loews corporation           L
lowe's                      LOW
lululemon athletica         LULU
lyondellbasell              LYB
m\&t bank                  MTB
marathon petroleum          MPC
marketaxess                 MKTX
marriott international      MAR
marsh mclennan              MMC
martin marietta materials   MLM
masco                       MAS
masterpiece                 MA
match group                 MTCH
mcormick \& company        MKC
mcdonald's                  MCD
mckesson corporation        MCK
medtronic                   MDT
merck \& co.               MRK
meta platforms              META
metlife                     MET
mettler toledo              MTD
mgm resorts                 MGM
microchip technology        MCHP
micron technology           MU
microsoft                   MSFT
mid-america apartment communities MAA
moderna                     MRNA
mohawk industries           MHK
molina healthcare           MOH
molson coors beverage company TAP
mondelez international      MDLZ
monolithic power systems    MPWR
monster beverage            MNST
moody's corporation         MCO
morgan stanley              MS
mosaic company (the)        MOS
motorola solutions          MSI
msci                        MSCI
nasdaq,                     NDAQ
netapp                      NTAP
netflix                     NFLX
newmont                     NEM
news corp (class a)         NWSA
news corp (class b)         NWS
nextera energy              NEE
nike,                       NKE
nisource                    NI
nordson corporation         NDSN
norfolk southern            NSC
northern trust              NTRS
northrop grumman            NOC
norwegian cruise line holdings NCLH
nrg energy                  NRG
nucor                       NUE
nvidia                      NVDA
nvr,                        NVR
nxp semiconductors          NXPI
oâ€ ${ }^{\text {TM }}$ reilly automotive ORLY
occidental petroleum        OXY
old dominion                ODFL
omnicom group               OMC
on semiconductor            ON
oneok                       OKE
oracle corporation          ORCL
otis worldwide              OTIS
paccar                      PCAR
packaging corporation of america PKG
palantir technologies       PLTR
palo alto networks          PANW
paramount global            PARA
parker hannifin             PH
paychex                     PAYX
paycom                      PAYC
paypal                      PYPL
pentair                     PNR
pepsico                     PEP
pfizer                      PFE
pg\&e corporation          PCG
philip morris international PM
phillips 66                 PSX
pinnacle west capital       PNW
pnc financial services      PNC
pool corporation            POOL
ppg industries              PPG
ppl corporation             PPL
principal financial group   PFG
procter \& gamble          PG
progressive corporation     PGR
prologis                    PLD
prudential financial        PRU
public service enterprise group PEG
ptc                         PTC
public storage              PSA
pultegroup                  PHM
quanta services             PWR
qualcomm                    QCOM
quest diagnostics           DGX
ralph lauder corporation    RL
raymond james financial     RJF
rtx corporation             RTX
realty income               O
regency centers             REG
regeneron pharmaceuticals   REGN
regions financial corporation RF
republic services           RSG
resmed                      RMD
revvity                     RVTY
rockwell automation         ROK
rollins,                    ROL
roper technologies          ROP
ross stores                 ROST
royal caribbean group       RCL
s\&p global                SPGI
salesforce                  CRM
sba communications          SBAC
schlumberger                SLB
seagate technology          STX
sempra                      SRE
servicenow                  NOW
sherwin-williams            SHW
simon property group        SPG
skyworks solutions          SWKS
j.m. smucker company (the)  SJM
smurfit westrock            SW
snap-on                     SNA
solventum                   SOLV
southern company            SO
southwest airlines          LUV
stanley black \& decker    SWK
starbucks                   SBUX
state street corporation    STT
steel dynamics              STLD
steris                      STE
stryker corporation         SYK
supermicro                  SMCI
synchrony financial         SYF
synopsys                    SNPS
sysco                       SYY
t-mobile us                 TMUS
t. rowe price               TROW
take-two interactive        TTWO
tapestry,                   TPR
targa resources             TRGP
target corporation          TGT
te connectivity             TEL
teledyne technologies       TDY
teradyne                    TER
tesla,                      TSLA
texas instruments           TXN
texas pacific land corporation TPL
textron                     TXT
thermo fisher scientific    TMO
tjx companies               TJX
tko group holdings          TKO
tractor supply              TSCO
trane technologies          TT
transdigm group             TDG
travelers companies (the)   TRV
trimble                     TRMB
truist financial            TFC
tyler technologies          TYL
tyson foods                 TSN
u.s. bancorp                USB
uber                        UBER
udr,                        UDR
ulta beauty                 ULTA
union pacific corporation   UNP
united airlines holdings    UAL
united parcel service       UPS
united rentals              URI
unitedhealth group          UNH
universal health services   UHS
valero energy               VLO
ventas                      VTR
veralto                     VLTO
verisign                    VRSN
verisk analytics            VRSK
verizon                     VZ
vertex pharmaceuticals      VRTX
viatris                     VTRS
vici properties             VICI
visa                        V
vistra corp.                VST
vulcan materials company    VMC
w. r. berkley corporation   WRB
w. w. grainger              GWW
wabtec                      WAB
walgreens boots alliance    WBA
walmart                     WMT
walt disney company (the)   DIS
warner bros. discovery      WBD
waste management            WM
waters corporation          WAT
wec energy group            WEC
wells fargo                 WFC
welltower                   WELL
west pharmaceutical services WST
western digital             WDC
weyerhaeuser                WY
williams-sonoma,            WSM
williams companies          WMB
willis towers watson        WTW
workday,                    WDAY
wynn resorts                WYNN
xcel energy                 XEL
xylem                       XYL
yum! brands                 YUM
zebra technologies          ZBRA
zimmer biomet               ZBH
zoetis                      ZTS
"""

# Existing functions (unchanged for brevity)
def get_stock_info(query):
    try:
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"
def calculate_indicators(data):
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['EMA_12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14, min_periods=1).mean()
    avg_loss = loss.rolling(window=14, min_periods=1).mean()
    rs = avg_gain / avg_loss
    data['RSI_14'] = 100 - (100 / (1 + rs))
    data['MACD'] = data['EMA_12'] - data['EMA_26']
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
    return data 
def plot_stock_with_indicators(ticker, period):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        if not data.empty:
            data = calculate_indicators(data)
            data = data.dropna()
            fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(12, 10), sharex=True)
            fig.suptitle(f'{ticker} Stock Price and Indicators ({period})')
            axes[0].plot(data.index, data['Close'], label='Close Price', color='blue')
            axes[0].plot(data.index, data['SMA_20'], label='SMA (20)', color='orange', linestyle='--')
            axes[0].plot(data.index, data['EMA_12'], label='EMA (12)', color='green', linestyle='--')
            axes[0].plot(data.index, data['EMA_26'], label='EMA (26)', color='red', linestyle='--')
            axes[0].set_ylabel('Price (USD)')
            axes[0].legend(loc='upper left')
            axes[0].grid(True)
            axes[1].plot(data.index, data['RSI_14'], label='RSI (14)', color='purple')
            axes[1].axhline(70, color='r', linestyle='--', alpha=0.5)
            axes[1].axhline(30, color='g', linestyle='--', alpha=0.5)
            axes[1].set_ylabel('RSI')
            axes[1].legend(loc='upper left')
            axes[1].grid(True)
            axes[2].plot(data.index, data['MACD'], label='MACD', color='black')
            axes[2].plot(data.index, data['Signal_Line'], label='Signal Line', color='cyan')
            axes[2].set_ylabel('MACD')
            axes[2].legend(loc='upper left')
            axes[2].grid(True)
            axes[3].bar(data.index, data['Volume'], color='gray', alpha=0.7)
            axes[3].set_ylabel('Volume')
            axes[3].set_xlabel('Date')
            axes[3].grid(True)
            plt.tight_layout(rect=[0, 0.03, 1, 0.95])
            buf = BytesIO()
            plt.savefig(buf, format="png")
            buf.seek(0)
            plt.close()
            return buf
        else:
            return "Could not retrieve historical data for the ticker."
    except Exception as e:
        return f"An error occurred while plotting: {e}"

def plot_simple_stock_price(ticker, period):
    try:
        data = yf.Ticker(ticker).history(period=period)
        if not data.empty:
            plt.figure(figsize=(10, 5))
            plt.plot(data.index, data['Close'])
            plt.title(f'{ticker} Stock Price Over {period}')
            plt.xlabel('Date')
            plt.ylabel('Stock Price ($)')
            plt.grid(True)
            buf = BytesIO()
            plt.savefig(buf, format="png")
            buf.seek(0)
            plt.close()
            return buf
        else:
            return f"Could not retrieve historical data for {ticker} for the period {period}."
    except Exception as e:
        return f"An error occurred while plotting the simple price: {e}"

def get_mutual_fund_info(query):
    try:
        prompt = f"Provide information about mutual funds based on the following query: '{query}'. Remember, this is for general informational purposes only and should not be considered financial advice. Users should consult with a qualified financial advisor."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"
    
def convert_currency(amount, from_currency, to_currency):
    try:
        amount = float(amount)
        rate = c.get_rate(from_currency.upper(), to_currency.upper())
        converted_amount = amount * rate
        from_currency_name = get_currency_name(from_currency.upper())
        to_currency_name = get_currency_name(to_currency.upper())
        return f"{amount:.2f} {from_currency_name} ({from_currency.upper()}) is equal to {converted_amount:.2f} {to_currency_name} ({to_currency.upper()})"
    except Exception as e:
        return f"Could not convert currency. Please check the currency codes and amount. Error: {e}"

def get_current_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        if 'currentPrice' in info and 'symbol' in info:
            return f"The current stock price of {info['symbol']} is ${info['currentPrice']:.2f}"
        elif 'regularMarketPrice' in info and 'symbol' in info:
            return f"The current stock price of {info['symbol']} is ${info['regularMarketPrice']:.2f}"
        else:
            return f"Could not retrieve the current stock price for {ticker.upper()}."
    except Exception as e:
        return f"An error occurred while fetching the current stock price for {ticker.upper()}: {e}"

def load_company_tickers(document_content):
    try:
        company_ticker_map = {}
        lines = document_content.strip().split('\n')
        skip_header = True
        for line in lines:
            if skip_header:
                skip_header = False
                continue
            parts = re.split(r'\s+', line.strip())
            if len(parts) >= 2:
                ticker = parts[-1].upper()
                company_name = " ".join(parts[:-1]).lower()
                company_name = re.sub(r'[^\w\s]', '', company_name)
                if company_name and ticker:
                    company_ticker_map[company_name] = ticker
        return company_ticker_map
    except Exception as e:
        print(f"Error loading company tickers from document: {e}")
        return {}
    
def search_ticker(company_name):
    company_name_lower = company_name.lower()
    try:
        prompt = f"What is the stock ticker symbol for {company_name}?"
        response = model.generate_content(prompt)
        text = response.text.strip()
        ticker_match = re.search(r'\b[A-Z]{1,5}\b', text)
        if ticker_match:
            ticker = ticker_match.group(0)
            if yf.Ticker(ticker).info.get('symbol'):
                return ticker
    except Exception as e:
        print(f"Gemini API search failed: {e}")
    try:
        stock = yf.Ticker(company_name_lower)
        info = stock.info
        if 'symbol' in info:
            return info['symbol'].upper()
    except Exception:
        pass
    try:
        query = f"{company_name} stock ticker site:*.edu | site:*.org | site:*.gov -inurl:(signup | login)"
        url = f"https://www.google.com/search?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        ticker_match = re.search(r'\b[A-Z]{1,5}\b', text)
        if ticker_match:
            ticker = ticker_match.group(0)
            if yf.Ticker(ticker).info.get('symbol'):
                return ticker
    except Exception as e:
        print(f"Google search failed: {e}")
    return None

def extract_text_from_image(image):
    """Extract text from an uploaded image using Gemini API"""
    try:
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        response = model.generate_content([
            {"mime_type": "image/png", "data": img_byte_arr},
            {"text": "Extract all the text from this image."}
        ])
        return response.text.strip()
    except Exception as e:
        return f"Error extracting text from image using Gemini API: {e}"

def summarize_text_from_image(image):
    """Summarize text from an uploaded image using Gemini API"""
    try:
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        response = model.generate_content([
            {"mime_type": "image/png", "data": img_byte_arr},
            {"text": "Summarize the text in this image."}
        ])
        return response.text.strip()
    except Exception as e:
        return f"Error summarizing text from image using Gemini API: {e}"

def analyze_graph_from_image(image, question):
    """Analyze a graph from an uploaded image and answer stock market-related questions"""
    try:
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Use Gemini API to interpret the graph and answer the question
        prompt = f"""
        You are an expert in stock market analysis. The attached image is a stock market graph.
        Based on the graph, answer the following question: '{question}'.
        If the question is not directly answerable from the graph alone (e.g., requires external data or context),
        provide a general explanation related to the topic and, if possible, infer something from the graph.
        """
        response = model.generate_content([
            {"mime_type": "image/png", "data": img_byte_arr},
            {"text": prompt}
        ])
        return response.text.strip()
    except Exception as e:
        return f"Error analyzing graph with Gemini API: {e}"

def generate_suggested_links(user_input):
    """Generate suggestive and closely related links using Gemini API, returning plain URLs"""
    try:
        prompt = f"""
        Based on the following query: '{user_input}', provide a list of up to 3 suggestive and closely related resources 
        (blogs, websites, or YouTube videos) that could help the user learn more about the topic. 
        Return only the URLs, one per line, without titles or formatting. If no specific resources are found, 
        return a message indicating general suggestions.
        """
        response = model.generate_content(prompt)
        links_text = response.text.strip()
        if not links_text:
            return "\n\n**Suggested Resources:**\nNo specific resources found. Try searching online for more information."
        return f"\n\n**Suggested Resources:**\n{links_text}"
    except Exception as e:
        return f"\n\n**Suggested Resources:**\nError generating links: {e}"

def chatbot(user_input, plot_duration, uploaded_image=None):
    financial_keywords = [
        "stock", "share", "bull market", "bear market", "ipo", "initial public offering", "blue chip stocks", 
        "market capitalization", "dividend", "stock split", "trading volume", "index", "nifty 50", "sensex", 
        "nasdaq", "dow jones", "circuit breaker", "penny stocks", "stop loss", "limit order", "market order",
        "investment", "portfolio", "mutual fund", "sip", "systematic investment plan", "nav", "elss", 
        "equity linked savings scheme", "debt fund", "equity fund", "balanced fund", "ulip", 
        "unit linked insurance plan", "index fund", "expense ratio", "lumpsum investment",
        "fixed deposit", "fd", "recurring deposit", "rd", "certificate of deposit", "cd", "government bonds", 
        "corporate bonds", "sovereign gold bond", "sgb", "nsc", "national savings certificate", "ppf", 
        "public provident fund", "eps", "earnings per share", "p/e ratio", "book value", "roe", 
        "return on equity", "roa", "return on assets", "debt-to-equity ratio", "volatility", "liquidity", 
        "inflation", "interest rate", "risk tolerance", "diversification", "hedging", "futures contract", 
        "options contract", "call option", "leverage", "margin trading", "short selling", "arbitrage",
        "reit", "real estate investment trust", "gold etf", "commodities trading", "cryptocurrency", "nft", 
        "non-fungible token", "ema", "exponential moving average", "sma", "simple moving average", "rsi", 
        "relative strength index", "macd", "moving average convergence divergence", "golden cross", 
        "death cross", "trend indicator", "crossover", "overbought", "oversold", "divergence", "histogram", 
        "signal line", "zero line", "currency", "convert", "exchange rate", "liquidity trap", "sector rotation", 
        "dark pool trading", "market depth", "price discovery", "vwap", "volume weighted average price", 
        "slippage", "spoofing", "flash crash", "tema", "triple exponential moving average", "dema", 
        "double exponential moving average", "hull moving average", "hma", "fibonacci retracement", 
        "pivot points", "supertrend indicator", "keltner channel", "williams %r", "bollinger band width", 
        "chaikin money flow", "cmf", "put-call ratio", "pcr", "vix", "volatility index", "greeks", "delta", 
        "gamma", "theta", "vega", "rho", "fear & greed index", "accumulation/distribution", "a/d line", 
        "on-balance volume", "obv", "short interest ratio", "advance-decline ratio", "adr", "open interest", 
        "oi", "sentiment divergence", "high-frequency trading", "hft", "pairs trading", "mean reversion", 
        "breakout trading", "swing trading", "position sizing", "trailing stop loss", "scalping", 
        "liquidity zones", "capital gain yield", "cgy", "risk-adjusted return", "beta coefficient", 
        "sharpe ratio", "hedge fund strategies", "yield curve inversion", "dollar-cost averaging", "dca", 
        "covered call strategy", "repo", "repurchase agreement", "defensive stocks", "altcoins", "staking", 
        "yield farming", "tokenomics", "nft staking", "smart contracts", "layer 1", "layer 2", 
        "market making bots", "crypto arbitrage", "dao", "decentralized autonomous organization", 
        "current price", "today's price", "stock price now", "what is the price of", "how much is"
    ]

    company_ticker_map = load_company_tickers(DOCUMENT_CONTENT)
    user_input_lower = user_input.lower()

    # Handle uploaded image
    if uploaded_image is not None:
        # Text extraction or summarization
        if "extract text" in user_input_lower or "read text" in user_input_lower:
            extracted_text = extract_text_from_image(uploaded_image)
            if not extracted_text.startswith("Error"):
                response = f"Extracted text from image: '{extracted_text}'"
            else:
                response = extracted_text
        elif "summarize text" in user_input_lower or "summary of text" in user_input_lower:
            summary = summarize_text_from_image(uploaded_image)
            if not summary.startswith("Error"):
                response = f"Summary of text in image: '{summary}'"
            else:
                response = summary
        # Graph-related questions
        elif any(kw in user_input_lower for kw in [
            "graph", "chart", "trend", "highest", "lowest", "peak", "bottom", "stock market", "stocks", 
            "trading", "indicators", "rsi", "macd", "moving average", "bollinger bands", "p/e ratio", 
            "dividends", "roi", "support", "resistance", "candlestick", "intraday", "long-term", 
            "short sell", "margin", "options", "leverage", "risk", "strategy", "prediction", "interest rates", 
            "inflation", "broker", "fees", "tax", "insider trading"
        ]):
            response = analyze_graph_from_image(uploaded_image, user_input)
        # Default image handling
        else:
            extracted_text = extract_text_from_image(uploaded_image)
            if extracted_text and not extracted_text.startswith("Error"):
                ticker_match = re.search(r'\b[A-Z]{1,5}\b', extracted_text)
                if ticker_match:
                    ticker = ticker_match.group(0)
                    if "indicators" in user_input_lower:
                        return plot_stock_with_indicators(ticker, plot_duration)
                    elif "price" in user_input_lower:
                        period = "1y" if len(user_input.split()) <= 2 else user_input.split()[2].lower()
                        return plot_simple_stock_price(ticker, period)
                    elif "current" in user_input_lower:
                        response = get_current_stock_price(ticker)
                    else:
                        response = f"Extracted ticker '{ticker}' from image. Here's some info:\n{get_stock_info(f'Provide a brief overview of {ticker}')}"
                else:
                    response = f"Extracted text from image: '{extracted_text}'\nPlease specify what you'd like to do with this information."
            else:
                response = extracted_text
        # Append suggested links for text/graph responses
        if not isinstance(response, BytesIO):
            response += generate_suggested_links(user_input)
        return response

    # Existing ticker and keyword handling
    if "print company_ticker_map" in user_input_lower or "show company ticker map" in user_input_lower:
        return company_ticker_map

    ticker_match = re.search(r'\b[A-Z]{1,5}\b', user_input)
    if ticker_match:
        ticker = ticker_match.group(0)
        if user_input_lower.startswith("indicators "):
            return plot_stock_with_indicators(ticker, plot_duration)
        elif user_input_lower.startswith("price "):
            parts = user_input.split()
            if len(parts) == 3:
                period = parts[2].lower()
                return plot_simple_stock_price(ticker, period)
            return "Invalid format for price command. Use 'price <ticker> <duration>' (e.g., 'price AAPL 1y')."
        elif any(phrase in user_input_lower for phrase in ["current price of ", "today's price of ", "stock price now of ", "what is the price of ", "how much is the stock of "]):
            response = get_current_stock_price(ticker)
        else:
            response = model.generate_content(user_input).text
        response += generate_suggested_links(user_input)
        return response

    found_keyword = False
    for keyword in financial_keywords:
        if keyword in user_input_lower:
            found_keyword = True
            break

    if not found_keyword:
        try:
            prompt = f"Identify any single investment or financial sector related keywords in the following prompt that are NOT in this list: {', '.join(financial_keywords)}. The prompt is: '{user_input}'. Return only the new keywords, separated by commas, or say 'None' if no new keywords are found."
            response = model.generate_content(prompt)
            new_keywords_str = response.text.strip()
            if new_keywords_str.lower() != "none":
                new_keywords = [keyword.strip() for keyword in new_keywords_str.split(',')]
                for new_keyword in new_keywords:
                    if new_keyword.lower() not in [kw.lower() for kw in financial_keywords]:
                        financial_keywords.append(new_keyword.lower())
                        print(f"New keyword added: {new_keyword}")
                found_keyword = True
        except Exception as e:
            print(f"Error while checking for new keywords: {e}")

    if found_keyword:
        if user_input_lower.startswith("stock info about"):
            ticker = user_input.split("about", 1)[1].strip().upper()
            query = f"Provide a brief overview of the company with the stock ticker {ticker}."
            response = get_stock_info(query)
        elif user_input_lower.startswith("indicators "):
            ticker = user_input.split(' ')[1].upper()
            return plot_stock_with_indicators(ticker, plot_duration)
        elif user_input_lower.startswith("price "):
            parts = user_input.split()
            if len(parts) == 3:
                ticker = parts[1].upper()
                period = parts[2].lower()
                return plot_simple_stock_price(ticker, period)
            return "Invalid format for price command. Use 'price <ticker> <duration>' (e.g., 'price AAPL 1y')."
        elif "show the graph of stock price of" in user_input_lower:
            try:
                parts = user_input_lower.split("show the graph of stock price of")
                if len(parts) > 1:
                    company_duration_part = parts[1].strip()
                    company_parts = company_duration_part.split("for")
                    if len(company_parts) == 2:
                        company_name = company_parts[0].strip()
                        duration_text = company_parts[1].strip()
                        ticker = company_ticker_map.get(company_name.lower())
                        if not ticker:
                            ticker = search_ticker(company_name)
                            if ticker:
                                company_ticker_map[company_name.lower()] = ticker
                            else:
                                return f"The company '{company_name}' is not indexed in the stock market."
                        duration_map = {"1 year": "1y", "one year": "1y", "5 year": "5y", "five year": "5y", "6 months": "6mo", "six months": "6mo", "1 month": "1mo", "one month": "1mo"}
                        period = duration_map.get(duration_text.lower())
                        if ticker and period:
                            return plot_simple_stock_price(ticker, period)
                        return "Could not understand the company name or duration. Please use a format like 'show the graph of stock price of Apple for 1 year'."
                    return "Could not understand the time duration. Please use a format like 'show the graph of stock price of Apple for 1 year'."
            except Exception as e:
                response = f"An error occurred while processing your request: {e}"
        elif user_input_lower.startswith("convert"):
            parts = user_input.split()
            if len(parts) == 5 and parts[2].lower() == "to":
                amount = parts[1]
                from_currency = parts[3]
                to_currency = parts[4]
                response = convert_currency(amount, from_currency, to_currency)
            else:
                response = "Invalid format for currency conversion. Use 'convert <amount> <from_currency> to <to_currency>' (e.g., 'convert 100 USD to INR')."
        elif any(phrase in user_input_lower for phrase in ["current price of ", "today's price of ", "stock price now of ", "what is the price of ", "how much is the stock of "]):
            try:
                company_name_or_ticker_prompt = ""
                extracted_company_name = None
                for phrase in ["current price of ", "today's price of ", "stock price now of ", "what is the price of ", "how much is the stock of "]:
                    if phrase in user_input_lower:
                        company_name_or_ticker_prompt = user_input_lower.split(phrase)[-1].strip()
                        words = company_name_or_ticker_prompt.split()
                        extracted_company_name = words[0]
                        if extracted_company_name.lower() in company_ticker_map:
                            extracted_company_name = extracted_company_name
                        elif len(words) > 1 and " ".join(words[:2]).lower() in company_ticker_map:
                            extracted_company_name = " ".join(words[:2])
                        elif len(words) > 2 and " ".join(words[:3]).lower() in company_ticker_map:
                            extracted_company_name = " ".join(words[:3])
                        else:
                            extracted_company_name = words[0]
                        break
                if extracted_company_name:
                    print(f"Extracted company name: {extracted_company_name}")
                    company_name_lower = extracted_company_name.lower()
                    ticker = company_ticker_map.get(company_name_lower)
                    if not ticker:
                        ticker = search_ticker(extracted_company_name)
                        if ticker:
                            company_ticker_map[company_name_lower] = ticker
                            pattern = r"(?i)\b" + re.escape(extracted_company_name) + r"\b"
                            new_prompt = re.sub(pattern, ticker, user_input)
                            print(f"New prompt: {new_prompt}")
                            return chatbot(new_prompt, plot_duration)
                        response = f"The company '{extracted_company_name}' is not indexed in the stock market."
                    else:
                        response = get_current_stock_price(ticker)
                else:
                    response = "Could not identify the company name in your request."
            except Exception as e:
                response = f"An error occurred while trying to get the current stock price: {e}"
        elif any(keyword in user_input_lower for keyword in ["financial advice", "investment tips", "should i invest", "financial planning"]):
            response = "I am designed to provide information and should not be considered a financial advisor."
        elif any(keyword in user_input_lower for keyword in ["mutual fund", "mutual funds", "mf", "what is a fund", "types of funds", "invest in funds"]):
            response = get_mutual_fund_info(user_input)
        else:
            response = model.generate_content(user_input).text
        # Append suggested links unless the response is a plot
        if not isinstance(response, BytesIO):
            response += generate_suggested_links(user_input)
        return response
    else:
        response = "I can only answer questions related to stock market, investments, and related financial topics."
        response += generate_suggested_links(user_input)
        return response

def main():
    st.title("Financial Stock and Mutual Fund Assistant Chatbot")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{
            "role": "assistant", 
            "content": "Welcome! Ask me about stocks, mutual funds, current prices (e.g., 'What is the current price of Apple?'), charts ('indicators <ticker>' or 'price <ticker> <duration>'), or currencies ('convert <amount> <from> to <to>'). Upload an image to extract text, summarize it, or ask graph-related questions! I'll also provide suggested resources."
        }]

    if "plot_duration" not in st.session_state:
        st.session_state["plot_duration"] = "1y"

    uploaded_file = st.file_uploader("Upload an image (text or stock graph)", type=["jpg", "png", "jpeg"])
    duration_options = ["1d", "1wk", "1mo", "3mo", "6mo", "1y", "5y", "max"]
    st.session_state["plot_duration"] = st.selectbox("Select Graph Duration (for indicators):", duration_options, index=duration_options.index(st.session_state["plot_duration"]))

    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state["messages"].append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        uploaded_image = Image.open(uploaded_file) if uploaded_file else None
        if uploaded_image:
            st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

        response = chatbot(prompt, st.session_state["plot_duration"], uploaded_image)

        if isinstance(response, BytesIO):
            st.session_state["messages"].append({"role": "assistant", "content": "Here is the chart:"})
            st.chat_message("assistant").image(response.getvalue())
        elif isinstance(response, dict):
            st.session_state["messages"].append({"role": "assistant", "content": "Company Ticker Map:"})
            st.chat_message("assistant").write(response)
        else:
            st.session_state["messages"].append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)

if __name__ == "__main__":
    main()
