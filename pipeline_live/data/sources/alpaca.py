import alpaca_trade_api as tradeapi
import os
from .util import (
    daily_cache, parallelize
)

alpaca = tradeapi.REST(key_id=os.environ.get('PAPER_APCA_API_KEY_ID'),
                       secret_key=os.environ.get('PAPER_APCA_API_SECRET_KEY'),
                       base_url=os.environ.get('PAPER_APCA_API_BASE_URL'),
                       api_version='v2')

alpaca_live = tradeapi.REST(key_id=os.environ.get('APCA_API_KEY_ID'),
                            secret_key=os.environ.get('APCA_API_SECRET_KEY'),
                            base_url=os.environ.get('APCA_API_BASE_URL'),
                            api_version='v2')

def list_symbols():
    return [
        a.symbol for a in alpaca.list_assets()
        if a.tradable and a.status == 'active'
    ]


def get_stockprices(limit=365, timespan='day'):
    all_symbols = list_symbols()

    @daily_cache(filename='alpaca_chart_{}'.format(limit))
    def get_stockprices_cached(all_symbols):
        return _get_stockprices(all_symbols, limit, timespan)

    return get_stockprices_cached(all_symbols)


def _get_stockprices(symbols, limit=365, timespan='day'):
    '''Get stock data (key stats and previous) from Alpaca.
    Just deal with Alpaca's 200 stocks per request limit.
    '''

    def fetch(symbols):
        barset = alpaca.get_barset(symbols, timespan, limit)
        data = {}
        for symbol in barset:
            df = barset[symbol].df
            # Update the index format for comparison with the trading calendar
            df.index = df.index.tz_convert('UTC').normalize()
            data[symbol] = df.asfreq('C')

        return data

    return parallelize(fetch, splitlen=199)(symbols)
