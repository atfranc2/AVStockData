from AVStockData.AVConnections.TimeSeriesData.FECReports.FECReport import FECReport
from AVStockData.AVConnections.Containers.AVTimeSeries import AVTimeSeries
from AVStockData.CallMeter import CallMeter

class IncomeStatement(FECReport):
    def __init__(self, api_key, callMeter = CallMeter(call_limit_per_minute = 5, call_limit_per_day = 500)):
        super().__init__(api_key, callMeter)
        self.symbol = None
        self.quarterly_reports = None
        self.annual_reports = None

    def getIncomeStatement(self, ticker):
        params = {'function':'INCOME_STATEMENT', 'symbol':ticker, 'apikey':self.api_key}
        response = self.getResponse(params)
        json_response = self.decodeJSONReponse(response)
        self.parse(json_response)

        return self
