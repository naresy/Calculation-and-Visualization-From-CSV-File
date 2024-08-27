
import plotly.graph_objects as go

def visualize_candlestick(weekly_df):
    # Create and display a candlestick chart of the weekly stock prices.
    fig = go.Figure(data=[go.Candlestick(
        x=weekly_df.index,
        open=weekly_df['AAPL.Open'],
        high=weekly_df['AAPL.High'],
        low=weekly_df['AAPL.Low'],
        close=weekly_df['AAPL.Close']
    )])

    fig.update_layout(
        title='Weekly Apple Stock Price',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=False
    )

    fig.show()
