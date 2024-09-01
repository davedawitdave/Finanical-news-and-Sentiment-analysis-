import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def top_publishers(df, n=5):
    """
    Plot the top N publishers based on the number of articles.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        n (int): The number of top publishers to display.

    Returns:
        None
    """
    top_publishers = df["publisher"].value_counts().head(n)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_publishers.values, y=top_publishers.index)
    plt.title(f"Top {n} Publishers by Number of Articles")
    plt.xlabel("Number of Articles")
    plt.ylabel("Publisher")
    plt.show()


def headline_length_distribution(df):
    """
    Plot the distribution of headline lengths.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    df["headline_length"] = df["headline"].apply(len)
    plt.figure(figsize=(10, 6))
    sns.histplot(df["headline_length"], kde=True)
    plt.title("Distribution of Headline Lengths")
    plt.xlabel("Headline Length")
    plt.ylabel("Frequency")
    plt.show()


def publication_trends_over_time(df):
    """
    Plot the number of articles published over time.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])  # Drop rows where 'date' could not be parsed
    df.set_index("date", inplace=True)
    df.resample("M").size().plot(figsize=(12, 6))
    plt.title("Publication Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.show()


def top_stock_mentions(df, n=5):
    """
    Plot the top N mentioned stocks in articles.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        n (int): The number of top stocks to display.

    Returns:
        None
    """
    top_stocks = df["stock"].value_counts().head(n)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_stocks.values, y=top_stocks.index)
    plt.title(f"Top {n} Mentioned Stocks")
    plt.xlabel("Number of Mentions")
    plt.ylabel("Stock")
    plt.show()
