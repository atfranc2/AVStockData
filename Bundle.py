from AVStockData.AVConnections.CrossSectionalData.CompanyOverview import CompanyOverview
from AVStockData.AVConnections.CrossSectionalData.Quote import Quote

from AVStockData.AVConnections.TimeSeriesData.FECReports.IncomeStatement import IncomeStatement
from AVStockData.AVConnections.TimeSeriesData.FECReports.CashFlow import CashFlow
from AVStockData.AVConnections.TimeSeriesData.FECReports.BalanceSheet import BalanceSheet


from AVStockData.AVConnections.TimeSeriesData.StockMarket.Intraday import Intraday
from AVStockData.AVConnections.TimeSeriesData.StockMarket.IntradayExtended import IntradayExtended
from AVStockData.AVConnections.TimeSeriesData.StockMarket.Daily import Daily
from AVStockData.AVConnections.TimeSeriesData.StockMarket.DailyAdjusted import DailyAdjusted
from AVStockData.AVConnections.TimeSeriesData.StockMarket.Weekly import Weekly
from AVStockData.AVConnections.TimeSeriesData.StockMarket.WeeklyAdjusted import WeeklyAdjusted
from AVStockData.AVConnections.TimeSeriesData.StockMarket.Monthly import Monthly
from AVStockData.AVConnections.TimeSeriesData.StockMarket.MonthlyAdjusted import MonthlyAdjusted

from AVStockData.AVConnections.AVConnection import AVConnection
from AVStockData.CallMeter import CallMeter


class Bundle(AVConnection):
    def __init__(self, api_key, call_limit_per_minute = 5, call_limit_per_day = 500):
        self.callMeter = CallMeter(call_limit_per_minute, call_limit_per_day)
        super().__init__(self.callMeter)
        self.__api_key = api_key
        self.__validateAPIKey(api_key)
        self.__initializeObjectReferences()

    def __isValidApiKey(self, api_key):
        test_params = {'function':'TIME_SERIES_DAILY', 'symbol':'KMT', 'outputsize':'compact', 'datatype':'json','apikey':api_key}
        response = self.getResponse(params = test_params)
        response_json = self.decodeJSONReponse(response)
        if self.callHasError(response_json):
            return False

        return True

    def __initializeObjectReferences(self):
        self.Intraday = Intraday(self.api_key, callMeter = self.callMeter)
        self.IntradayExtended = IntradayExtended(self.api_key, callMeter = self.callMeter)
        self.Daily = Daily(self.api_key, callMeter = self.callMeter)
        self.DailyAdjusted = DailyAdjusted(self.api_key, callMeter = self.callMeter)
        self.Weekly = Weekly(self.api_key, callMeter = self.callMeter)
        self.WeeklyAdjusted = WeeklyAdjusted(self.api_key, callMeter = self.callMeter)
        self.Monthly = Monthly(self.api_key, callMeter = self.callMeter)
        self.MonthlyAdjusted = MonthlyAdjusted(self.api_key, callMeter = self.callMeter)

        self.BalanceSheet = BalanceSheet(self.api_key, callMeter = self.callMeter)
        self.CashFlow = CashFlow(self.api_key, callMeter = self.callMeter)
        self.IncomeStatement = IncomeStatement(self.api_key, callMeter = self.callMeter)

        self.CompanyOverview = CompanyOverview(self.api_key, callMeter = self.callMeter)
        self.Quote = Quote(self.api_key, callMeter = self.callMeter)

    def __validateAPIKey(self, api_key):
        if not self.__isValidApiKey(api_key):
            return ValueError(api_key + " is not a valid Alpha Vantage API key.")



    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self, api_key):
        self.__validateAPIKey(api_key)
        self.__api_key = api_key
        self.__initializeObjectReferences()
