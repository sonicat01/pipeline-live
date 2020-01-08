from iexfinance import refdata
from iexfinance.stocks import Stock
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os
import alpaca_trade_api as tradeapi
from .util import (
    daily_cache, parallelize, quarterly_cache, monthly_cache
)
error_log = {}

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

def get_credentials(token=None):

    token = token or os.environ.get('QUANDL_TOKEN')
    if token is None :
        raise ValueError('token must be given to access QUANDL API',
                         ' (env: QUANDL_TOKEN)')
class REST(object):

    def __init__(self, api_token, staging=False):
        self._api_token = get_credentials(api_token)
        self._staging = staging
        self._session = requests.Session()

    def _request(self, method, path, params=None):
        url = 'https://www.quandl.com/api/v3'+ path
        params = params or {}
        params['api_key'] = os.environ.get('QUANDL_TOKEN')
        print(url, params)
        retry = Retry(connect=3, backoff_factor=2)
        adapter = HTTPAdapter(max_retries=retry)
        self._session.mount('http://', adapter)
        self._session.mount('https://', adapter)
        resp = self._session.request(method, url, params=params)
        resp.raise_for_status()
        return resp.json()

    def get(self, path, params=None):
        return self._request('GET', path, params=params)

rest = REST(api_token=os.environ.get('QUANDL_TOKEN'))


def fundamentials():
    all_symbols = list_symbols()
    return _fundamentials(all_symbols)

#https://www.quandl.com/api/v3/datatables/SHARADAR/SF1?dimension=MRY&ticker=AAPL&api_key=Vy9HqmyJLWYUFMGt31E8
@monthly_cache(filename='quandl_fundamentials.pkl')
def _fundamentials(all_symbols):
    def fetch(symbol):
        try:
            path = '/datatables/SHARADAR/SF1'
            params = {}
            params['dimension'] = 'MRQ'
            params['ticker']=symbol[0]
            res = rest.get(path, params=params)
            if len(res) >0 and len(res['datatable']['data']) > 0:
                data =res['datatable']['data'][0]
                columns = res['datatable']['columns']
                dict = {}
                i=0
                for key in columns:
                    dict[key['name']] = data[i]
                    i += 1
                ans = {}
                ans[symbol[0]] = dict
                return ans
            else:
                return {"NORESULT": {}}
        except Exception as e:
            print(symbol,'cache error {}'.format(e))
            return {"NORESULT": {}}
    return parallelize(fetch, workers=2, splitlen=1)(all_symbols)
