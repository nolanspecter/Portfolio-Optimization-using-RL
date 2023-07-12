TICKERS = ['AMZN', 'WMT', 'XOM', 'BRK-B', 'UNH', 'UPS', 'AAPL', 'LIN', 'PLD', 'GOOG', 'NEE']
FILEPATH = 'preprocessed.csv'
EPISODE_LENGTH = 252*5*3 #5 years. Multiply 3 for indexing each stocks
TA_LIST = ['sma', 'ema', 'rsi', 'macd', 'obv', 'cci', 'adx', 'atr']