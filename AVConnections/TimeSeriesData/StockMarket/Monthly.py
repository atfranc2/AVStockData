from AVStockData.AVConnections.AVConnection import AVConnection
from AVStockData.AVConnections.TimeSeriesData.StockMarket.StockMarket import StockMarket
from AVStockData.CallMeter import CallMeter

class Monthly(StockMarket):
    def __init__(self, api_key, callMeter = CallMeter(call_limit_per_minute = 5, call_limit_per_day = 500)):
        super().__init__(api_key, callMeter)
        self.setTimeSeriesName()

    def setTimeSeriesName(self):
        self.time_series_name = "Monthly Time Series"

    def getMonthly(self, ticker, data_type = 'json'):
        params = {'function':'TIME_SERIES_MONTHLY', 'symbol':ticker, 'datatype':data_type, 'apikey':self.api_key}
        response = self.getResponse(params)
        response = self.decodeJSONReponse(response) if data_type == 'json' else self.decodeCSVResponse(response)
        self.parse(response, self.time_series_name)

        return self
