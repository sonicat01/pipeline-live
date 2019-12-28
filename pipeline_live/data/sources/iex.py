from iexfinance import refdata
from iexfinance.stocks import Stock
import pandas as pd
import requests
import os
from .util import (
    daily_cache, parallelize, quarterly_cache, monthly_cache
)


class REST(object):

    def __init__(self, api_token, staging=False):
        self._api_token = get_credentials(api_token)
        self._staging = staging
        self._session = requests.Session()

    def _request(self, method, path, params=None):
        url = 'https://cloud.iexapis.com/stable/stock'+ path
        params = params or {}
        params['token'] = self._api_token
        resp = self._session.request(method, url, params=params)
        resp.raise_for_status()
        return resp.json()

    def get(self, path, params=None):
        return self._request('GET', path, params=params)

rest = REST()

def list_symbols():
    return [
        symbol['symbol'] for symbol in refdata.get_symbols()
    ]

def get_credentials(token=None):

    token = token or os.environ.get('IEX_TOKEN')
    if token is None :
        raise ValueError('token must be given to access IEX API',
                         ' (env: IEX_TOKEN)')

def _ensure_dict(result, symbols):
    if len(symbols) == 1:
        return {symbols[0]: result}
    return result


class IEXGetter(object):

    def __init__(self, method):
        self._method = method

    def __call__(self):
        method_name = 'get_{}'.format(self._method)

        @quarterly_cache(filename='iex_{}.pkl'.format(self._method))
        def _get(all_symbols):
            def fetch(symbols):
                return _ensure_dict(
                    getattr(Stock(symbols), method_name)(),
                    symbols
                )

            return parallelize(fetch, splitlen=99)(all_symbols)

        all_symbols = list_symbols()
        return _get(all_symbols)


key_stats = IEXGetter('key_stats')
company = IEXGetter('company')
financials = IEXGetter('financials')
earnings = IEXGetter('earnings')


def get_stockprices(chart_range='1y'):
    '''
    This is a proxy to the main fetch function to cache
    the result based on the chart range parameter.
    '''

    all_symbols = list_symbols()

    @daily_cache(filename='iex_chart_{}'.format(chart_range))
    def get_stockprices_cached(all_symbols):
        return _get_stockprices(all_symbols, chart_range)

    return get_stockprices_cached(all_symbols)


def _get_stockprices(symbols, chart_range='1y'):
    '''Get stock data (key stats and previous) from IEX.
    Just deal with IEX's 100 stocks limit per request.
    '''

    def fetch(symbols):
        charts = _ensure_dict(
            Stock(symbols).get_chart(range=chart_range),
            symbols
        )
        result = {}
        for symbol, obj in charts.items():
            df = pd.DataFrame(
                obj,
                columns=('date', 'open', 'high', 'low', 'close', 'volume'),
            ).set_index('date')
            df.index = pd.to_datetime(df.index, utc=True)
            result[symbol] = df
        return result

    return parallelize(fetch, splitlen=99)(symbols)

def advancedstats():
    all_symbols = list_symbols()
    return _advancedstats(all_symbols)


@quarterly_cache(filename='iex_advanced-stats.pkl')
def _advancedstats(all_symbols):
    def fetch(symbol):
        path = '/{}/advanced-stats'.format(symbol[0])
        res = rest.get(path)
        if len(res) == 1:
            return {symbol[0]: res}
        else:
            return {"NORESULT": {}}
    return parallelize(fetch, workers=50, splitlen=1)(all_symbols)


def income():
    all_symbols = list_symbols()
    return _income(all_symbols)


@quarterly_cache(filename='iex_income.pkl')
def _income(all_symbols):
    def fetch(symbol):
        path = '/{}/income'.format(symbol[0])
        params = {
            'period': 'quarter',
            'last': 12,
        }
        res = rest.get(path, params)
        if len(res) == 1:
            return {symbol[0]: res['income'][0]}
        else:
            return {"NORESULT": {}}
    return parallelize(fetch, workers=50, splitlen=1)(all_symbols)


def balancesheet():
    all_symbols = list_symbols()
    return _balancesheet(all_symbols)


@quarterly_cache(filename='iex_balancesheet.pkl')
def _balancesheet(all_symbols):
    def fetch(symbol):
        path = '/{}/balance-sheet'.format(symbol[0])
        params = {
            'period': 'quarter',
            'last': 12,
        }
        res = rest.get(path, params)
        if len(res) == 1:
            return {symbol[0]: res['balancesheet'][0]}
        else:
            return {"NORESULT": {}}
    return parallelize(fetch, workers=50, splitlen=1)(all_symbols)