from AVStockData.AVConnections.AVConnection import AVConnection
from AVStockData.AVConnections.TimeSeriesData.StockMarket.StockMarket import StockMarket

class DailyAdjusted(StockMarket):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.setTimeSeriesName()

    def setTimeSeriesName(self):
        self.time_series_name = "Time Series (Daily)"

    def getDailyAdjusted(self, ticker, output_size = 'compact', data_type = 'json'):
        params = {'function':'TIME_SERIES_DAILY_ADJUSTED', 'symbol':ticker, 'outputsize':output_size, 'datatype':data_type, 'apikey':self.api_key}
        response = self.getResponse(params)
        response = self.decodeJSONReponse(response) if data_type == 'json' else self.decodeCSVResponse(response)
        self.parse(response, self.time_series_name)

        return self
