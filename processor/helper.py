import yfinance as yf

## STOCK HELPERS
# gets the current stock price
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    latest_data = ticker.history(period='1s')
    return latest_data['Close'][0]

# gets the history df based on period and interval
def get_history(symbol, period, interval):
    ticker = yf.Ticker(symbol)
    hist_data = ticker.history(period=period, interval=interval)
    return hist_data

# gets the difference on the same day
def get_open_close_diff(symbol, period, interval):
    hist_df = get_history(symbol, period, interval)
    df = hist_df['Close'] - hist_df['Open']
    return df
