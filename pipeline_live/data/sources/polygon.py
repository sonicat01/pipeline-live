import os
import alpaca_trade_api as tradeapi

alpaca = tradeapi.REST(key_id=os.environ.get('PAPER_APCA_API_KEY_ID'),
                       secret_key=os.environ.get('PAPER_APCA_API_SECRET_KEY'),
                       base_url=os.environ.get('PAPER_APCA_API_BASE_URL'),
                       api_version='v2')

alpaca_live = tradeapi.REST(key_id=os.environ.get('APCA_API_KEY_ID'),
                            secret_key=os.environ.get('APCA_API_SECRET_KEY'),
                            base_url=os.environ.get('APCA_API_BASE_URL'),
                            api_version='v2')

from .util import (
    daily_cache, monthly_cache, parallelize
)


def list_symbols():
    return [
        a.symbol for a in alpaca_live.list_assets()
        if a.tradable and a.status == 'active'
    ]


def company():
    all_symbols = list_symbols()
    return _company(all_symbols)


@daily_cache(filename='polygon_company.pkl')
def _company(all_symbols):
    def fetch(symbols):
        api = alpaca_live
        params = {
            'symbols': ','.join(symbols),
        }
        response = api.polygon.get('/meta/symbols/company', params=params)
        return {
            o['symbol']: o for o in response
        }

    return parallelize(fetch, workers=25, splitlen=50)(all_symbols)


def financials():
    all_symbols = list_symbols()
    return _financials(all_symbols)


@daily_cache(filename='polygon_financials.pkl')
def _financials(all_symbols):
    def fetch(symbols):
        api = alpaca_live
        params = {
            'symbols': ','.join(symbols),
        }
        return api.polygon.get('/meta/symbols/financials', params=params)

    return parallelize(fetch, workers=25, splitlen=50)(all_symbols)

def financialsv2():
    all_symbols = list_symbols()
    return _financialsv2(all_symbols)


@monthly_cache(filename='polygon_financialsv2.pkl')
def _financialsv2(all_symbols):
    def fetch(symbol):
        path = '/reference/financials/{}'.format(symbol[0])
        api = alpaca_live
        params = {
            'limit': 1,
            'type': 'Q',
        }
        res = api.polygon.get(path, params=params, version='v2')
        if len(res['results']) == 1:
            return {symbol[0]: res['results'][0]}
        else:
            return {"NORESULT": {}}
    return parallelize(fetch, workers=50, splitlen=1)(all_symbols)