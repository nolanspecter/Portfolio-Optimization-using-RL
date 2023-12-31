import pandas as pd
import numpy as np
import ta

def get_ta(df):
    df['sma'] = ta.trend.sma_indicator(df['close'], window=9)
    df['ema'] = ta.trend.ema_indicator(df['close'], window=9)
    # df['adx'] = ta.trend.adx(df['high'], df['low'], df['close']).replace(0,np.nan)
    df['obv'] = ta.volume.on_balance_volume(df['close'], df['volume'])
    df.fillna('bfill')

    return df

def preprocessing(df):
    ta_df = pd.DataFrame()

    for ticker in df['ticker'].unique():
        temp_df = get_ta(df[df['ticker'] == ticker])
        ta_df = pd.concat([ta_df,temp_df])

    ta_df = ta_df.sort_values(['date', 'ticker']).reset_index(drop=True)
    ta_df.index = ta_df.date.factorize()[0]

    cov_list = []
    lookback = 252

    for i in range(lookback, len(ta_df.index.unique())):
        data_lookback = ta_df.loc[i-lookback:i,:]
        price_lookback = data_lookback.pivot_table(index='date', columns='ticker', values='close')
        return_lookback = price_lookback.pct_change().dropna()
        cov = return_lookback.cov().values
        cov_list.append(cov)
    
    df_cov = pd.DataFrame({'date':ta_df.date.unique()[lookback:], 'cov_list':cov_list})
    ta_df = ta_df.merge(df_cov, on='date')
    ta_df = ta_df.sort_values(['date', 'ticker']).reset_index(drop=True)

    ta_df.index = ta_df.date.factorize()[0]
    return ta_df
