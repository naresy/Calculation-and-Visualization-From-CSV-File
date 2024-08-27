def calculate_close_price_statistics(df):
    # Calculating the min, max and avg close price
    # AAPL.Close is the close price
    max_close = df['AAPL.Close'].max()
    min_close = df['AAPL.Close'].min()
    avg_close = df['AAPL.Close'].mean()
    print(f"Max Close: {max_close}, Min Close: {min_close}, Avg Close: {avg_close}")
    return max_close, min_close, avg_close