import yahoofinancials as yf
import pandas as pd
import numpy as np


def download_data_and_format(option, dates):
    ticker = format_option(option)
    yahoo_f = yf.YahooFinancials(ticker)

    data = yahoo_f.get_historical_price_data(
        dates['start_date'], dates['end_date'], 'daily')
    df = pd.DataFrame(data[ticker]['prices'])
    df = df.drop('date', axis=1).set_index('formatted_date')
    df.head()

    return add_returns_columns(df)


def format_option(option):
    if option == 'a' or option == 'A':
        return 'QQQ'
    elif option == 'b' or option == 'B':
        return 'SPY'
    else:
        return 'IWM'


def add_returns_columns(df):
    df['returns'] = (df['adjclose'] / df['adjclose'].shift(1)) - 1
    df.head()

    df['pos_returns'] = np.where(df['returns'] > 0.0, 1, 0)
    df.head()

    df['lag_ret'] = df['returns'].shift(1)
    df.head()

    return df
