import pandas as pd

def load_and_merge_data(sentiment_path, trader_path):
    sentiment = pd.read_csv(sentiment_path)
    trader = pd.read_csv(trader_path, compression='gzip')

    sentiment['Date'] = pd.to_datetime(sentiment['Date'])
    trader['time'] = pd.to_datetime(trader['time'])

    trader['date'] = trader['time'].dt.date
    sentiment['date'] = sentiment['Date'].dt.date

    merged = pd.merge(trader, sentiment[['date', 'Classification']], on='date', how='left')
    return merged
