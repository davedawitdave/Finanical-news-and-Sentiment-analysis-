import pandas as pd
import os


# Load Data Function
def load_data(file_name):
    """
    Load CSV data from the data folder.

    Args:
        file_name (str): The name of the CSV file to load.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    data_path = os.path.join("../data", file_name)
    return pd.read_csv(data_path)


# Calculate Headline Length Function
def calculate_headline_length(df):
    """
    Calculate the length of each headline in the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing the 'headline' column.

    Returns:
        pd.Series: Series containing the length of each headline.
    """
    return df["headline"].apply(len)


# Count Articles Per Publisher Function
def count_articles_per_publisher(df):
    """
    Count the number of articles per publisher.

    Args:
        df (pd.DataFrame): DataFrame containing the 'publisher' column.

    Returns:
        pd.Series: Series containing the count of articles per publisher.
    """
    return df["publisher"].value_counts()


# Analyze Publication Trends Function
def analyze_publication_trends(df):
    """
    Analyze trends in publication dates.

    Args:
        df (pd.DataFrame): DataFrame containing the 'date' column.

    Returns:
        pd.Series: Series containing the count of articles per date.
    """
    df["date"] = pd.to_datetime(df["date"])
    return df["date"].dt.date.value_counts().sort_index()


# If you want to add a class
class EDAFunctions:
    def __init__(self, df):
        self.df = df

    def load_data(self, file_name):
        return load_data(file_name)

    def calculate_headline_length(self):
        return calculate_headline_length(self.df)

    def count_articles_per_publisher(self):
        return count_articles_per_publisher(self.df)

    def analyze_publication_trends(self):
        return analyze_publication_trends(self.df)
