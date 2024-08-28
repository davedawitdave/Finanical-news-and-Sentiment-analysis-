import pandas as pd

def main():
    # Sample DataFrame creation
    data = {
        "Stock": ["AAPL", "GOOGL", "AMZN"],
        "Price": [150.75, 2730.20, 3300.50],
        "Change": [1.2, -0.5, 2.3]
    }
    df = pd.DataFrame(data)
    
    # Print the DataFrame
    print("Sample DataFrame:")
    print(df)

    # Basic analysis example: calculate mean price
    mean_price = df["Price"].mean()
    print(f"\nThe mean stock price is: {mean_price}")

if __name__ == "__main__":
    main()
