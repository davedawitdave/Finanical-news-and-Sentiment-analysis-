# **Stock Performance and News Sentiment Analysis Project**

## **Project Overview**
This project analyzes the correlation between daily stock performance and news sentiment. We use financial data and sentiment analysis to determine how news impacts stock market behavior.

## **Objectives**
- Perform **Descriptive Statistics** and **Time Series Analysis** on stock data.
- Conduct **News Sentiment Analysis** to quantify the tone of articles (positive, negative, neutral).
- Perform **Technical Analysis** using tools like **TA-Lib**.
- Calculate **Correlation** between sentiment and stock returns.

## **Tasks**

### **Task 1: Descriptive and Time Series Analysis**
- **Data Loading**: Process stock and news datasets.
- **Descriptive Statistics**: Use Python functions (`describe()`, `info()`, `head()`) to summarize stock data.
- **Time Series Analysis**: Calculate daily percentage changes for `Adj Close` and volume. Aggregate data by daily, weekly, monthly, and yearly intervals.
- **Technical Indicators**: Use **TA-Lib** to calculate RSI, MACD, Bollinger Bands, and more.

### **Task 2: News Sentiment Analysis**
- **Sentiment Scoring**: Use **NLTK** and **TextBlob** to analyze the sentiment of news headlines.
- **Daily Sentiment Aggregation**: Compute the average daily sentiment for each stock.

### **Task 3: Correlation Between News and Stock Movement**
- **Date Alignment**: Normalize timestamps for news and stock data.
- **Daily Returns Calculation**: Compute daily returns from the stock prices.
- **Correlation Analysis**: Measure correlation between daily sentiment and stock returns using the Pearson correlation coefficient.
- **Visualization**: Plot stock performance against sentiment and provide heatmaps of correlations.

## **Datasets**
1. **Stock Data**: Includes daily `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume`, `Dividends`, and `Stock Splits`.
2. **News Sentiment Data**: Contains over 1.4 million news headlines and their associated `sentiment`, `publisher`, `date`, and `stock`.

## **Methods**

### **1. Descriptive Analysis**
- Summarize stock price data using basic statistics.
- **Time Series Plotting**: Plot stock prices and volume trends over time.

### **2. Sentiment Analysis**
- Analyze sentiment using NLP libraries. Aggregate sentiments on a daily basis.
- Create **word clouds** and **bar charts** for sentiment distribution.

### **3. Technical Analysis**
- Calculate **RSI**, **MACD**, **Bollinger Bands**, and other indicators using **TA-Lib**.
- Generate performance metrics from stock data (e.g., moving averages).

### **4. Correlation Analysis**
- Merge stock data with sentiment scores on a daily basis.
- Perform correlation analysis between stock performance metrics (returns) and sentiment.
- Plot correlation heatmaps and visualize stock movement with overlaid sentiment scores.

## **Key Performance Indicators**
- **Sentiment Analysis Accuracy**
- **Daily Returns Calculation**
- **Correlation Strength** between stock movement and sentiment.

## **Tools and Libraries**
- **Python**, **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn** (for visualization)
- **TA-Lib and yfinance** (for technical analysis)
- **NLTK**, **TextBlob** (for sentiment analysis)
- **Git/GitHub** (for version control)

## **Project Structure**
```bash
├── data/                           # Stock and news CSV files
├── notebooks/
│   ├── descriptive_eda.ipynb        # Descriptive stats and EDA
│   ├── sentiment_analysis.ipynb     # Sentiment analysis 
│   ├── technical_analysis.ipynb     # using ta-lib and finance libraries 
│   ├── time_series_analysis.ipynb   # time series analysis of
├── scripts/
│   ├── eda_functions.py             # EDA and visualization functions
│   ├── calculate_performance.py     # Stock performance calculations
├── README.md                        # Project overview and details
└── requirements.txt                 # Python dependencies
# How to Run

## Clone the Repository:
```bash
git clone https://github.com/davedawitdave/Finanical-news-and-Sentiment-analysis-.git
```

## Install Dependencies:
```bash
pip install -r requirements.txt
```
