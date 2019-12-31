import logging

import numpy as np

from pipeline_live.data.sources import quandl
from zipline.pipeline.loaders.base import PipelineLoader

log = logging.getLogger(__name__)

class QUANDLFinancialsLoader(PipelineLoader):

    def load_adjusted_array(self, domain, columns, dates, sids, mask):

        fundamentials = quandl.fundamentials()

        out = {}

        def getdata(symbol, name, missing_value):
            out = fundamentials.get(symbol, {})
            if out == {}:
                return missing_value
            else:
                return out.get(name, missing_value)

        for c in columns:
            data = [
                getdata(symbol, c.name, c.missing_value) for symbol in sids
            ]
            out[c] = np.tile(np.array(data, dtype=c.dtype), (len(dates), 1))

        return out