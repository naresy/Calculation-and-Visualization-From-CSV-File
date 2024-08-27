
import pandas as pd
# load data from the url 
def load_data(url):
    
    df = pd.read_csv(url)
    return df
# clean data remove the duplicates an 
def clean_data(df):
    
    df_cleaned = df.drop_duplicates().sort_values(by='Date').reset_index(drop=True)
    if len(df) != len(df_cleaned):
        print(f"Removed {len(df) - len(df_cleaned)} duplicates or unordered rows.")
    return df_cleaned

def filter_by_volume(df):
   
    avg_volume = df['AAPL.Volume'].mean()
    filtered_df = df[df['AAPL.Volume'] >= avg_volume].copy()  
    filtered_df.loc[:, 'Day'] = pd.to_datetime(filtered_df['Date']).dt.day_name() 
    return filtered_df

def aggregate_weekly(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    weekly_df = df.resample('W').agg({
        'AAPL.Open': 'first',
        'AAPL.High': 'max',
        'AAPL.Low': 'min',
        'AAPL.Close': 'last',
        'AAPL.Volume': 'sum'
    })
    return weekly_df
