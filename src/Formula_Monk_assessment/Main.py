import data_processing as dp
import calculate_statistics as da
import data_visualization as dv
import utils

def main():
    url = 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'

    # Creating df on url
    df = dp.load_data(url)
    
    # Calculate statistics
    da.calculate_close_price_statistics(df)

    # Cleaning the data
    df_cleaned = dp.clean_data(df)

    # Filter data by volume and save to CSV
    filtered_df = dp.filter_by_volume(df_cleaned)
    utils.save_to_csv(filtered_df, 'filtered_data.csv')

    # Aggregate data weekly and save to CSV
    weekly_df = dp.aggregate_weekly(df_cleaned)
    utils.save_to_csv(weekly_df, 'weekly_data.csv')

    # Visualize the graph
    dv.visualize_candlestick(weekly_df)

# Run the main function
if __name__ == "__main__":
    main()