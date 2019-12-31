import numpy as np

from zipline.utils.numpy_utils import (
    object_dtype, datetime64ns_dtype, datetime64D_dtype, float64_dtype,
)
from zipline.pipeline.data.dataset import Column, DataSet

from .fundamentals_loader import (
    IEXKeyStatsLoader,
    IEXCompanyLoader,
    IEXFinancialsLoader,
    IEXEarningsLoader,
    IEXAdvancedStatsLoader,
    IEXIncomeLoader,
    IEXBalanceSheetLoader,
)



class IEXEarnings(DataSet):

    '''
        "actualEPS": 2.46,
        "consensusEPS": 2.36,
        "announceTime": "AMC",
        "numberOfEstimates": 34,
        "EPSSurpriseDollar": 0.1,
        "EPSReportDate": "2019-04-30",
        "fiscalPeriod": "Q1 2019",
        "fiscalEndDate": "2019-03-31",
        "yearAgo": 2.73,
        "yearAgoChangePercent": -0.0989
    '''

    announceTime = Column(object_dtype, missing_value='')
    fiscalPeriod = Column(object_dtype, missing_value='')
    EPSReportDate = Column(
        datetime64ns_dtype,
        missing_value=np.datetime64('1970-01-01'))
    fiscalEndDate = Column(
        datetime64ns_dtype,
        missing_value=np.datetime64('1970-01-01'))
    actualEPS = Column(float64_dtype, missing_value=np.nan)
    consensusEPS = Column(float64_dtype, missing_value=np.nan)
    numberOfEstimates = Column(float64_dtype, missing_value=np.nan)
    EPSSurpriseDollar = Column(float64_dtype, missing_value=np.nan)
    yearAgo = Column(float64_dtype, missing_value=np.nan)
    yearAgoChangePercent = Column(float64_dtype, missing_value=np.nan)

    _loader = IEXEarningsLoader()

    @classmethod
    def get_loader(cls):
        return cls._loader

class IEXFinancials(DataSet):

    '''
        "reportDate": "2019-03-31",
        "grossProfit": 21648000000,
        "costOfRevenue": 36270000000,
        "operatingRevenue": 57918000000,
        "totalRevenue": 57918000000,
        "operatingIncome": 13242000000,
        "netIncome": 11561000000,
        "researchAndDevelopment": 3948000000,
        "operatingExpense": 44676000000,
        "currentAssets": 123346000000,
        "totalAssets": 341998000000,
        "totalLiabilities": 236138000000,
        "currentCash": 38329000000,
        "currentDebt": 22429000000,
        "shortTermDebt": 22429000000,
        "longTermDebt": 90201000000,
        "totalCash": 80433000000,
        "totalDebt": 112630000000,
        "shareholderEquity": 105860000000,
        "cashChange": -4954000000,
        "cashFlow": 11155000000
    '''
    reportDate = Column(
        datetime64ns_dtype,
        missing_value=np.datetime64('1970-01-01'))
    grossProfit = Column(float64_dtype, missing_value=np.nan)
    costOfRevenue = Column(float64_dtype, missing_value=np.nan)
    operatingRevenue = Column(float64_dtype, missing_value=np.nan)
    totalRevenue = Column(float64_dtype, missing_value=np.nan)
    operatingIncome = Column(float64_dtype, missing_value=np.nan)
    netIncome = Column(float64_dtype, missing_value=np.nan)
    researchAndDevelopment = Column(float64_dtype, missing_value=np.nan)
    operatingExpense = Column(float64_dtype, missing_value=np.nan)
    currentAssets = Column(float64_dtype, missing_value=np.nan)
    totalAssets = Column(float64_dtype, missing_value=np.nan)
    totalLiabilities = Column(float64_dtype, missing_value=np.nan)
    currentCash = Column(float64_dtype, missing_value=np.nan)
    currentDebt = Column(float64_dtype, missing_value=np.nan)
    shortTermDebt = Column(float64_dtype, missing_value=np.nan)
    longTermDebt = Column(float64_dtype, missing_value=np.nan)
    totalCash = Column(float64_dtype, missing_value=np.nan)
    totalDebt = Column(float64_dtype, missing_value=np.nan)
    shareholderEquity = Column(float64_dtype, missing_value=np.nan)
    cashChange = Column(float64_dtype, missing_value=np.nan)
    cashFlow = Column(float64_dtype, missing_value=np.nan)

    _loader = IEXFinancialsLoader()

    @classmethod
    def get_loader(cls):
        return cls._loader

class IEXAdvancedStats(DataSet):

    '''
    "week52change":0.870585,
	"week52high":304.92,
	"week52low":144,
	"marketcap":1333087376551,
	"employees":143501,
	"day200MovingAvg":226.25,
	"day50MovingAvg":273.6,
	"float":4614185772,
	"avg10Volume":31874487.1,
	"avg30Volume":26891810.8,
	"ttmEPS":12.3654,
	"ttmDividendRate":3,
	"companyName":"Apple,Inc.",
	"sharesOutstanding":4448883703,
	"maxChangePercent":299.8969,
	"year5ChangePercent":1.6145,
	"year2ChangePercent":0.72,
	"year1ChangePercent":0.894531,
	"ytdChangePercent":0.846095,
	"month6ChangePercent":0.482769,
	"month3ChangePercent":0.306137,
	"month1ChangePercent":0.085486,
	"day30ChangePercent":0.105903,
	"day5ChangePercent":0.038741,
	"nextDividendDate":null,
	"dividendYield":0.010613182446004909,
	"nextEarningsDate":"2020-02-11",
	"exDividendDate":"2019-11-12",
	"peRatio":24.85,
	"beta":1.5551090309976225,
	"totalCash":103462991448,
	"currentDebt":16415606112,
	"revenue":272583903431,
	"grossProfit":98986073753,
	"totalRevenue":266317004553,
	"EBITDA":77117950533,
	"revenuePerShare":60.9,
	"revenuePerEmployee":1952669.97,
	"debtToEquity":1.21,
	"profitMargin":0.2198161454228158,
	"enterpriseValue":1333786391541,
	"enterpriseValueToRevenue":5.02,
	"priceToSales":5.19,
	"priceToBook":14.877693008945878,
	"forwardPERatio":null,
	"pegRatio":5.98,
	"peHigh":25.637110644176467,
	"peLow":12.0561976665986,
	"week52highDate":"2020-01-11",
	"week52lowDate":"2019-01-10",
	"putCallRatio":0.578095664092484
    '''

    week52change = Column(float64_dtype, missing_value=np.nan)
    week52high = Column(float64_dtype, missing_value=np.nan)
    week52low = Column(float64_dtype, missing_value=np.nan)
    marketcap = Column(float64_dtype, missing_value=np.nan)
    employees = Column(float64_dtype, missing_value=np.nan)
    day200MovingAvg = Column(float64_dtype, missing_value=np.nan)
    day50MovingAvg = Column(float64_dtype, missing_value=np.nan)
    float = Column(float64_dtype, missing_value=np.nan)
    avg10Volume = Column(float64_dtype, missing_value=np.nan)
    avg30Volume = Column(float64_dtype, missing_value=np.nan)
    ttmEPS = Column(float64_dtype, missing_value=np.nan)
    ttmDividendRate = Column(float64_dtype, missing_value=np.nan)
    companyName = Column(object_dtype, missing_value='')
    sharesOutstanding = Column(float64_dtype, missing_value=np.nan)
    maxChangePercent = Column(float64_dtype, missing_value=np.nan)
    year5ChangePercent = Column(float64_dtype, missing_value=np.nan)
    year2ChangePercent = Column(float64_dtype, missing_value=np.nan)
    year1ChangePercent = Column(float64_dtype, missing_value=np.nan)
    ytdChangePercent = Column(float64_dtype, missing_value=np.nan)
    month6ChangePercent = Column(float64_dtype, missing_value=np.nan)
    month3ChangePercent = Column(float64_dtype, missing_value=np.nan)
    month1ChangePercent = Column(float64_dtype, missing_value=np.nan)
    day30ChangePercent = Column(float64_dtype, missing_value=np.nan)
    day5ChangePercent = Column(float64_dtype, missing_value=np.nan)
    nextDividendDate = Column(
        datetime64ns_dtype,
        missing_value=np.datetime64('1970-01-01'))
    dividendYield = Column(
        datetime64ns_dtype,
        missing_value=np.datetime64('1970-01-01'))
    exDividendDate = Column(
        datetime64ns_dtype,
        missing_value=np.datetime64('1970-01-01'))
    peRatio = Column(float64_dtype, missing_value=np.nan)
    beta = Column(float64_dtype, missing_value=np.nan)
    totalCash = Column(float64_dtype, missing_value=np.nan)
    currentDebt = Column(float64_dtype, missing_value=np.nan)
    revenue = Column(float64_dtype, missing_value=np.nan)
    grossProfit = Column(float64_dtype, missing_value=np.nan)
    totalRevenue = Column(float64_dtype, missing_value=np.nan)
    EBITDA = Column(float64_dtype, missing_value=np.nan)
    revenuePerShare = Column(float64_dtype, missing_value=np.nan)
    revenuePerEmployee = Column(float64_dtype, missing_value=np.nan)
    debtToEquity = Column(float64_dtype, missing_value=np.nan)
    profitMargin = Column(float64_dtype, missing_value=np.nan)
    enterpriseValue = Column(float64_dtype, missing_value=np.nan)
    enterpriseValueToRevenue = Column(float64_dtype, missing_value=np.nan)
    priceToSales = Column(float64_dtype, missing_value=np.nan)
    priceToBook = Column(float64_dtype, missing_value=np.nan)
    forwardPERatio = Column(float64_dtype, missing_value=np.nan)
    pegRatio = Column(float64_dtype, missing_value=np.nan)
    peHigh = Column(float64_dtype, missing_value=np.nan)
    peLow = Column(float64_dtype, missing_value=np.nan)
    week52highDate = Column(
        datetime64ns_dtype,
        missing_value=np.datetime64('1970-01-01'))
    week52lowDate = Column(
        datetime64ns_dtype,
        missing_value=np.datetime64('1970-01-01'))
    putCallRatio = Column(float64_dtype, missing_value=np.nan)

    _loader = IEXAdvancedStatsLoader()

    @classmethod
    def get_loader(cls):
        return cls._loader

class IEXIncome(DataSet):

    '''
    "reportDate":"2019-09-30",
	"totalRevenue":65007314152,
	"costOfRevenue":40298857745,
	"grossProfit":25007419882,
	"researchAndDevelopment":4195678780,
	"sellingGeneralAndAdmin":4759757117,
	"operatingExpense":50874194223,
	"operatingIncome":15807717541,
	"otherIncomeExpenseNet":663505746,
	"ebit":16250845749,
	"interestIncome":816275044,
	"pretaxIncome":16777437134,
	"incomeTax":2539655585,
	"minorityInterest":0,
	"netIncome":13809902052,
	"netIncomeBasic":13713273392
    '''
    reportDate = Column(
        datetime64ns_dtype,
        missing_value=np.datetime64('1970-01-01'))

    totalRevenue = Column(float64_dtype, missing_value=np.nan)
    costOfRevenue = Column(float64_dtype, missing_value=np.nan)
    grossProfit = Column(float64_dtype, missing_value=np.nan)
    researchAndDevelopment = Column(float64_dtype, missing_value=np.nan)
    sellingGeneralAndAdmin = Column(float64_dtype, missing_value=np.nan)
    operatingExpense = Column(float64_dtype, missing_value=np.nan)
    operatingIncome = Column(float64_dtype, missing_value=np.nan)
    otherIncomeExpenseNet = Column(float64_dtype, missing_value=np.nan)
    ebit = Column(float64_dtype, missing_value=np.nan)
    interestIncome = Column(float64_dtype, missing_value=np.nan)
    pretaxIncome = Column(float64_dtype, missing_value=np.nan)
    incomeTax = Column(float64_dtype, missing_value=np.nan)
    minorityInterest = Column(float64_dtype, missing_value=np.nan)
    netIncome = Column(float64_dtype, missing_value=np.nan)
    netIncomeBasic = Column(float64_dtype, missing_value=np.nan)

    _loader = IEXIncomeLoader()

    @classmethod
    def get_loader(cls):
        return cls._loader

class IEXBalanceSheet(DataSet):

    '''
	"reportDate":"2019-09-30",
	"currentCash":28169210327,
	"shortTermInvestments":72825415940,
	"receivables":23861944908,
	"inventory":4139652796,
	"otherCurrentAssets":12722261241,
	"currentAssets":165138453988,
	"longTermInvestments":107709609907,
	"propertyPlantEquipment":39136679454,
	"goodwill":null,
	"intangibleAssets":null,
	"otherAssets":32456693775,
	"totalAssets":342215741120,
	"accountsPayable":48420404262,
	"currentLongTermDebt":10742302697,
	"otherCurrentLiabilities":44762852691,
	"totalCurrentLiabilities":108256707135,
	"longTermDebt":93153734757,
	"otherLiabilities":4092755866,
	"minorityInterest":0,
	"totalLiabilities":258015403130,
	"commonStock":4553279621,
	"retainedEarnings":46579787687,
	"treasuryStock":6698172,
	"capitalSurplus":null,
	"shareholderEquity":92588745652,
	"netTangibleAssets":90767561384
    '''
    reportDate = Column(
        datetime64ns_dtype,
        missing_value=np.datetime64('1970-01-01'))
    currentCash = Column(float64_dtype, missing_value=np.nan)
    shortTermInvestments = Column(float64_dtype, missing_value=np.nan)
    receivables = Column(float64_dtype, missing_value=np.nan)
    inventory = Column(float64_dtype, missing_value=np.nan)
    otherCurrentAssets = Column(float64_dtype, missing_value=np.nan)
    currentAssets = Column(float64_dtype, missing_value=np.nan)
    longTermInvestments = Column(float64_dtype, missing_value=np.nan)
    propertyPlantEquipment = Column(float64_dtype, missing_value=np.nan)
    goodwill = Column(float64_dtype, missing_value=np.nan)
    intangibleAssets = Column(float64_dtype, missing_value=np.nan)
    otherAssets = Column(float64_dtype, missing_value=np.nan)
    totalAssets = Column(float64_dtype, missing_value=np.nan)
    accountsPayable = Column(float64_dtype, missing_value=np.nan)
    currentLongTermDebt = Column(float64_dtype, missing_value=np.nan)
    otherCurrentLiabilities = Column(float64_dtype, missing_value=np.nan)
    totalCurrentLiabilities = Column(float64_dtype, missing_value=np.nan)
    longTermDebt = Column(float64_dtype, missing_value=np.nan)
    otherLiabilities = Column(float64_dtype, missing_value=np.nan)
    minorityInterest = Column(float64_dtype, missing_value=np.nan)
    totalLiabilities = Column(float64_dtype, missing_value=np.nan)
    commonStock = Column(float64_dtype, missing_value=np.nan)
    retainedEarnings = Column(float64_dtype, missing_value=np.nan)
    treasuryStock = Column(float64_dtype, missing_value=np.nan)
    capitalSurplus = Column(float64_dtype, missing_value=np.nan)
    shareholderEquity = Column(float64_dtype, missing_value=np.nan)
    netTangibleAssets = Column(float64_dtype, missing_value=np.nan)

    _loader = IEXBalanceSheetLoader()

    @classmethod
    def get_loader(cls):
        return cls._loader


class IEXKeyStats(DataSet):

    '''
    "week52change":0.891812,
    "week52high":294.85,
    "week52low":148,
    "marketcap":1287722038343,
    "employees":141588,
    "day200MovingAvg":224.82,
    "day50MovingAvg":272.13,
    "float":4591748076,
    "avg10Volume":32008185.1,
    "avg30Volume":26009094.8,
    "ttmEPS":11.9403,
    "ttmDividendRate":3,
    "companyName":"Apple,Inc.",
    "sharesOutstanding":4621785519,
    "maxChangePercent":292.7652,
    "year5ChangePercent":1.6305,
    "year2ChangePercent":0.722,
    "year1ChangePercent":0.879295,
    "ytdChangePercent":0.840802,
    "month6ChangePercent":0.482568,
    "month3ChangePercent":0.305952,
    "month1ChangePercent":0.086811,
    "day30ChangePercent":0.103839,
    "day5ChangePercent":0.037825,
    "nextDividendDate":null,
    "dividendYield":0.010573715641493318,
    "nextEarningsDate":"2020-02-18",
    "exDividendDate":"2019-11-19",
    "peRatio":25.08,
    "beta":1.6117314506008147
     '''

    week52change = Column(float64_dtype, missing_value=np.nan)
    week52high = Column(float64_dtype, missing_value=np.nan)
    week52low = Column(float64_dtype, missing_value=np.nan)
    marketcap = Column(float64_dtype, missing_value=np.nan)
    employees = Column(float64_dtype, missing_value=np.nan)
    day200MovingAvg = Column(float64_dtype, missing_value=np.nan)
    day50MovingAvg = Column(float64_dtype, missing_value=np.nan)
    float = Column(float64_dtype, missing_value=np.nan)
    avg10Volume = Column(float64_dtype, missing_value=np.nan)
    avg30Volume = Column(float64_dtype, missing_value=np.nan)
    ttmEPS = Column(float64_dtype, missing_value=np.nan)
    ttmDividendRate = Column(float64_dtype, missing_value=np.nan)
    companyName = Column(object_dtype, missing_value='')
    sharesOutstanding = Column(float64_dtype, missing_value=np.nan)
    maxChangePercent = Column(float64_dtype, missing_value=np.nan)
    year5ChangePercent = Column(float64_dtype, missing_value=np.nan)
    year2ChangePercent = Column(float64_dtype, missing_value=np.nan)
    year1ChangePercent = Column(float64_dtype, missing_value=np.nan)
    ytdChangePercent = Column(float64_dtype, missing_value=np.nan)
    month6ChangePercent = Column(float64_dtype, missing_value=np.nan)
    month3ChangePercent = Column(float64_dtype, missing_value=np.nan)
    month1ChangePercent = Column(float64_dtype, missing_value=np.nan)
    day30ChangePercent = Column(float64_dtype, missing_value=np.nan)
    day5ChangePercent = Column(float64_dtype, missing_value=np.nan)
    nextDividendDate = Column(
        datetime64ns_dtype,
        missing_value=np.datetime64('1970-01-01'))
    dividendYield = Column(float64_dtype, missing_value=np.nan)
    nextEarningsDate = Column(
        datetime64ns_dtype,
        missing_value=np.datetime64('1970-01-01'))
    exDividendDate = Column(
        datetime64ns_dtype,
        missing_value=np.datetime64('1970-01-01'))
    peRatio = Column(float64_dtype, missing_value=np.nan)
    beta = Column(float64_dtype, missing_value=np.nan)

    _loader = IEXKeyStatsLoader()

    @classmethod
    def get_loader(cls):
        return cls._loader


class IEXCompany(DataSet):

    symbol = Column(object_dtype, missing_value='')
    companyName = Column(object_dtype, missing_value='')
    exchange = Column(object_dtype, missing_value='')
    industry = Column(object_dtype, missing_value='')
    website = Column(object_dtype, missing_value='')
    description = Column(object_dtype, missing_value='')
    CEO = Column(object_dtype, missing_value='')
    issueType = Column(object_dtype, missing_value='')
    sector = Column(object_dtype, missing_value='')
    # tags = Column(object_dtype, missing_value='')

    _loader = IEXCompanyLoader()

    @classmethod
    def get_loader(cls):
        return cls._loader
