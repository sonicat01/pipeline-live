import numpy as np
from zipline.utils.numpy_utils import (
    object_dtype, datetime64D_dtype, float64_dtype,
)
from zipline.pipeline.data.dataset import Column, DataSet

from .fundamentals_loader import PolygonCompanyLoader, PolygonFinancialsLoader


class PolygonCompany(DataSet):

    '''
    "logo": "https://s3.polygon.io/logos/aapl/logo.png",
    "exchange": "Nasdaq Global Select",
    "name": "Apple Inc.",
    "symbol": "AAPL",
    "listdate": "2018-08-15",
    "cik": "0000320193",
    "bloomberg": "EQ0010169500001000",
    "figi": "string",
    "lei": "HWUPKR0MPOU8FGXBT394",
    "sic": 3571,
    "country": "us",
    "industry": "Computer Hardware",
    "sector": "Technology",
    "marketcap": 815604985500,
    "employees": 116000,
    "phone": "(408) 996-1010",
    "ceo": "Tim Cook",
    "url": "http://www.apple.com",
    "description": "Apple Inc. designs, manufactures, and markets mobile communication and media devices, personal computers, and portable digital music players to consumers...\n",
    '''  # noqa

    exchange = Column(object_dtype, missing_value='')
    name = Column(object_dtype, missing_value='')
    symbol = Column(object_dtype, missing_value='')
    listdate = Column(
        datetime64D_dtype,
        missing_value=np.datetime64('1970-01-01'))
    cik = Column(object_dtype, missing_value='')
    bloomberg = Column(object_dtype, missing_value='')
    figi = Column(object_dtype, missing_value='')
    lei = Column(object_dtype, missing_value='')
    sic = Column(float64_dtype, missing_value=np.nan)
    country = Column(object_dtype, missing_value='')
    industry = Column(object_dtype, missing_value='')
    sector = Column(object_dtype, missing_value='')
    marketcap = Column(float64_dtype, missing_value=np.nan)
    employees = Column(float64_dtype, missing_value=np.nan)
    phone = Column(object_dtype, missing_value='')
    ceo = Column(object_dtype, missing_value='')
    tags = Column(object_dtype, missing_value='')

    _loader = PolygonCompanyLoader()

    @classmethod
    def get_loader(cls):
        return cls._loader

class PolygonFinancials(DataSet):

    '''
     "ticker": "AAPL",
      "period": "Q",
      "calendarDate": "2019-03-31",
      "reportPeriod": "2019-03-31",
      "updated": "1999-03-28",
      "accumulatedOtherComprehensiveIncome": 0,
      "assets": 0,
      "assetsAverage": 0,
      "assetsCurrent": 0,
      "assetTurnover": 0,
      "assetsNonCurrent": 0,
      "bookValuePerShare": 0,
      "capitalExpenditure": 0,
      "cashAndEquivalents": 0,
      "cashAndEquivalentsUSD": 0,
      "costOfRevenue": 0,
      "consolidatedIncome": 0,
      "currentRatio": 0,
      "debtToEquityRatio": 0,
      "debt": 0,
      "debtCurrent": 0,
      "debtNonCurrent": 0,
      "debtUSD": 0,
      "deferredRevenue": 0,
      "depreciationAmortizationAndAccretion": 0,
      "deposits": 0,
      "dividendYield": 0,
      "dividendsPerBasicCommonShare": 0,
      "earningBeforeInterestTaxes": 0,
      "earningsBeforeInterestTaxesDepreciationAmortization": 0,
      "EBITDAMargin": 0,
      "earningsBeforeInterestTaxesDepreciationAmortizationUSD": 0,
      "earningBeforeInterestTaxesUSD": 0,
      "earningsBeforeTax": 0,
      "earningsPerBasicShare": 0,
      "earningsPerDilutedShare": 0,
      "earningsPerBasicShareUSD": 0,
      "shareholdersEquity": 0,
      "averageEquity": 0,
      "shareholdersEquityUSD": 0,
      "enterpriseValue": 0,
      "enterpriseValueOverEBIT": 0,
      "enterpriseValueOverEBITDA": 0,
      "freeCashFlow": 0,
      "freeCashFlowPerShare": 0,
      "foreignCurrencyUSDExchangeRate": 0,
      "grossProfit": 0,
      "grossMargin": 0,
      "goodwillAndIntangibleAssets": 0,
      "interestExpense": 0,
      "investedCapital": 0,
      "investedCapitalAverage": 0,
      "inventory": 0,
      "investments": 0,
      "investmentsCurrent": 0,
      "investmentsNonCurrent": 0,
      "totalLiabilities": 0,
      "currentLiabilities": 0,
      "liabilitiesNonCurrent": 0,
      "marketCapitalization": 0,
      "netCashFlow": 0,
      "netCashFlowBusinessAcquisitionsDisposals": 0,
      "issuanceEquityShares": 0,
      "issuanceDebtSecurities": 0,
      "paymentDividendsOtherCashDistributions": 0,
      "netCashFlowFromFinancing": 0,
      "netCashFlowFromInvesting": 0,
      "netCashFlowInvestmentAcquisitionsDisposals": 0,
      "netCashFlowFromOperations": 0,
      "effectOfExchangeRateChangesOnCash": 0,
      "netIncome": 0,
      "netIncomeCommonStock": 0,
      "netIncomeCommonStockUSD": 0,
      "netLossIncomeFromDiscontinuedOperations": 0,
      "netIncomeToNonControllingInterests": 0,
      "profitMargin": 0,
      "operatingExpenses": 0,
      "operatingIncome": 0,
      "tradeAndNonTradePayables": 0,
      "payoutRatio": 0,
      "priceToBookValue": 0,
      "priceEarnings": 0,
      "priceToEarningsRatio": 0,
      "propertyPlantEquipmentNet": 0,
      "preferredDividendsIncomeStatementImpact": 0,
      "sharePriceAdjustedClose": 0,
      "priceSales": 0,
      "priceToSalesRatio": 0,
      "tradeAndNonTradeReceivables": 0,
      "accumulatedRetainedEarningsDeficit": 0,
      "revenues": 0,
      "revenuesUSD": 0,
      "researchAndDevelopmentExpense": 0,
      "returnOnAverageAssets": 0,
      "returnOnAverageEquity": 0,
      "returnOnInvestedCapital": 0,
      "returnOnSales": 0,
      "shareBasedCompensation": 0,
      "sellingGeneralAndAdministrativeExpense": 0,
      "shareFactor": 0,
      "shares": 0,
      "weightedAverageShares": 0,
      "weightedAverageSharesDiluted": 0,
      "salesPerShare": 0,
      "tangibleAssetValue": 0,
      "taxAssets": 0,
      "incomeTaxExpense": 0,
      "taxLiabilities": 0,
      "tangibleAssetsBookValuePerShare": 0,
      "workingCapital": 0
    '''  # noqa

    ticker = Column(object_dtype, missing_value='')
    period = Column(object_dtype, missing_value='')
    calendarDate = Column(object_dtype, missing_value='')
    reportPeriod = Column(object_dtype, missing_value='')
    updated = Column(object_dtype, missing_value='')
    accumulatedOtherComprehensiveIncome = Column(float64_dtype, missing_value=np.nan)
    assets = Column(float64_dtype, missing_value=np.nan)
    assetsAverage = Column(float64_dtype, missing_value=np.nan)
    assetsCurrent = Column(float64_dtype, missing_value=np.nan)
    assetTurnover = Column(float64_dtype, missing_value=np.nan)
    assetsNonCurrent = Column(float64_dtype, missing_value=np.nan)
    bookValuePerShare = Column(float64_dtype, missing_value=np.nan)
    capitalExpenditure = Column(float64_dtype, missing_value=np.nan)
    cashAndEquivalents = Column(float64_dtype, missing_value=np.nan)
    cashAndEquivalentsUSD = Column(float64_dtype, missing_value=np.nan)
    costOfRevenue = Column(float64_dtype, missing_value=np.nan)
    consolidatedIncome = Column(float64_dtype, missing_value=np.nan)
    currentRatio = Column(float64_dtype, missing_value=np.nan)
    debtToEquityRatio = Column(float64_dtype, missing_value=np.nan)
    debt = Column(float64_dtype, missing_value=np.nan)
    debtCurrent = Column(float64_dtype, missing_value=np.nan)
    debtNonCurrent = Column(float64_dtype, missing_value=np.nan)
    debtUSD = Column(float64_dtype, missing_value=np.nan)
    deferredRevenue = Column(float64_dtype, missing_value=np.nan)
    depreciationAmortizationAndAccretion = Column(float64_dtype, missing_value=np.nan)
    deposits = Column(float64_dtype, missing_value=np.nan)
    dividendYield = Column(float64_dtype, missing_value=np.nan)
    dividendsPerBasicCommonShare = Column(float64_dtype, missing_value=np.nan)
    earningBeforeInterestTaxes = Column(float64_dtype, missing_value=np.nan)
    earningsBeforeInterestTaxesDepreciationAmortization = Column(float64_dtype, missing_value=np.nan)
    EBITDAMargin = Column(float64_dtype, missing_value=np.nan)
    earningsBeforeInterestTaxesDepreciationAmortizationUSD = Column(float64_dtype, missing_value=np.nan)
    earningBeforeInterestTaxesUSD = Column(float64_dtype, missing_value=np.nan)
    earningsBeforeTax = Column(float64_dtype, missing_value=np.nan)
    earningsPerBasicShare = Column(float64_dtype, missing_value=np.nan)
    earningsPerDilutedShare = Column(float64_dtype, missing_value=np.nan)
    earningsPerBasicShareUSD = Column(float64_dtype, missing_value=np.nan)
    shareholdersEquity = Column(float64_dtype, missing_value=np.nan)
    averageEquity = Column(float64_dtype, missing_value=np.nan)
    shareholdersEquityUSD = Column(float64_dtype, missing_value=np.nan)
    enterpriseValue = Column(float64_dtype, missing_value=np.nan)
    enterpriseValueOverEBIT = Column(float64_dtype, missing_value=np.nan)
    enterpriseValueOverEBITDA = Column(float64_dtype, missing_value=np.nan)
    freeCashFlow = Column(float64_dtype, missing_value=np.nan)
    freeCashFlowPerShare = Column(float64_dtype, missing_value=np.nan)
    foreignCurrencyUSDExchangeRate = Column(float64_dtype, missing_value=np.nan)
    grossProfit = Column(float64_dtype, missing_value=np.nan)
    grossMargin = Column(float64_dtype, missing_value=np.nan)
    goodwillAndIntangibleAssets = Column(float64_dtype, missing_value=np.nan)
    interestExpense = Column(float64_dtype, missing_value=np.nan)
    investedCapital = Column(float64_dtype, missing_value=np.nan)
    investedCapitalAverage = Column(float64_dtype, missing_value=np.nan)
    inventory = Column(float64_dtype, missing_value=np.nan)
    investments = Column(float64_dtype, missing_value=np.nan)
    investmentsCurrent = Column(float64_dtype, missing_value=np.nan)
    investmentsNonCurrent = Column(float64_dtype, missing_value=np.nan)
    totalLiabilities = Column(float64_dtype, missing_value=np.nan)
    currentLiabilities = Column(float64_dtype, missing_value=np.nan)
    liabilitiesNonCurrent = Column(float64_dtype, missing_value=np.nan)
    marketCapitalization = Column(float64_dtype, missing_value=np.nan)
    netCashFlow = Column(float64_dtype, missing_value=np.nan)
    netCashFlowBusinessAcquisitionsDisposals = Column(float64_dtype, missing_value=np.nan)
    issuanceEquityShares = Column(float64_dtype, missing_value=np.nan)
    issuanceDebtSecurities = Column(float64_dtype, missing_value=np.nan)
    paymentDividendsOtherCashDistributions = Column(float64_dtype, missing_value=np.nan)
    netCashFlowFromFinancing = Column(float64_dtype, missing_value=np.nan)
    netCashFlowFromInvesting = Column(float64_dtype, missing_value=np.nan)
    netCashFlowInvestmentAcquisitionsDisposals = Column(float64_dtype, missing_value=np.nan)
    netCashFlowFromOperations = Column(float64_dtype, missing_value=np.nan)
    effectOfExchangeRateChangesOnCash = Column(float64_dtype, missing_value=np.nan)
    netIncome = Column(float64_dtype, missing_value=np.nan)
    netIncomeCommonStock = Column(float64_dtype, missing_value=np.nan)
    netIncomeCommonStockUSD = Column(float64_dtype, missing_value=np.nan)
    netLossIncomeFromDiscontinuedOperations = Column(float64_dtype, missing_value=np.nan)
    netIncomeToNonControllingInterests = Column(float64_dtype, missing_value=np.nan)
    profitMargin = Column(float64_dtype, missing_value=np.nan)
    operatingExpenses = Column(float64_dtype, missing_value=np.nan)
    operatingIncome = Column(float64_dtype, missing_value=np.nan)
    tradeAndNonTradePayables = Column(float64_dtype, missing_value=np.nan)
    payoutRatio = Column(float64_dtype, missing_value=np.nan)
    priceToBookValue = Column(float64_dtype, missing_value=np.nan)
    priceEarnings = Column(float64_dtype, missing_value=np.nan)
    priceToEarningsRatio = Column(float64_dtype, missing_value=np.nan)
    propertyPlantEquipmentNet = Column(float64_dtype, missing_value=np.nan)
    preferredDividendsIncomeStatementImpact = Column(float64_dtype, missing_value=np.nan)
    sharePriceAdjustedClose = Column(float64_dtype, missing_value=np.nan)
    priceSales = Column(float64_dtype, missing_value=np.nan)
    priceToSalesRatio = Column(float64_dtype, missing_value=np.nan)
    tradeAndNonTradeReceivables = Column(float64_dtype, missing_value=np.nan)
    accumulatedRetainedEarningsDeficit = Column(float64_dtype, missing_value=np.nan)
    revenues = Column(float64_dtype, missing_value=np.nan)
    revenuesUSD = Column(float64_dtype, missing_value=np.nan)
    researchAndDevelopmentExpense = Column(float64_dtype, missing_value=np.nan)
    returnOnAverageAssets = Column(float64_dtype, missing_value=np.nan)
    returnOnAverageEquity = Column(float64_dtype, missing_value=np.nan)
    returnOnInvestedCapital = Column(float64_dtype, missing_value=np.nan)
    returnOnSales = Column(float64_dtype, missing_value=np.nan)
    shareBasedCompensation = Column(float64_dtype, missing_value=np.nan)
    sellingGeneralAndAdministrativeExpense = Column(float64_dtype, missing_value=np.nan)
    shareFactor = Column(float64_dtype, missing_value=np.nan)
    shares = Column(float64_dtype, missing_value=np.nan)
    weightedAverageShares = Column(float64_dtype, missing_value=np.nan)
    weightedAverageSharesDiluted = Column(float64_dtype, missing_value=np.nan)
    salesPerShare = Column(float64_dtype, missing_value=np.nan)
    tangibleAssetValue = Column(float64_dtype, missing_value=np.nan)
    taxAssets = Column(float64_dtype, missing_value=np.nan)
    incomeTaxExpense = Column(float64_dtype, missing_value=np.nan)
    taxLiabilities = Column(float64_dtype, missing_value=np.nan)
    tangibleAssetsBookValuePerShare = Column(float64_dtype, missing_value=np.nan)
    workingCapital = Column(float64_dtype, missing_value=np.nan)

    _loader = PolygonFinancialsLoader()

    @classmethod
    def get_loader(cls):
        return cls._loader
