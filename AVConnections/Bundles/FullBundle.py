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

from AVStockData.AVConnections.Bundles.Bundle import Bundle

class FullBundle(Bundle):
    def __init__(self, api_key, call_limit_per_minute = 5, call_limit_per_day = 500):
        super().__init__(api_key, call_limit_per_minute, call_limit_per_day)
        self.initializeObjectReferences()

    def initializeObjectReferences(self):
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
