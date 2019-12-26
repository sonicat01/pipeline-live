import numpy as np

from zipline.pipeline.loaders.base import PipelineLoader

from pipeline_live.data.sources import polygon


class PolygonCompanyLoader(PipelineLoader):

    def load_adjusted_array(self, domain, columns, dates, sids, mask):

        company = polygon.company()
        out = {}
        for c in columns:
            data = [
                company.get(symbol, {}).get(c.name, c.missing_value)
                for symbol in sids
            ]
            out[c] = np.tile(np.array(data, dtype=c.dtype), (len(dates), 1))

        return out

class PolygonFinancialsLoader(PipelineLoader):

    def load_adjusted_array(self, domain, columns, dates, sids, mask):

        financials = polygon.financials()
        out = {}
        for c in columns:
            data = [
                financials.get(symbol, {}).get(c.name, c.missing_value)
                for symbol in sids
            ]
            out[c] = np.tile(np.array(data, dtype=c.dtype), (len(dates), 1))

        return out