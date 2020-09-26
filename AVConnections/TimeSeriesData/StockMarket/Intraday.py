from AVStockData.AVConnections.AVConnection import AVConnection
from AVStockData.AVConnections.TimeSeriesData.StockMarket.StockMarket import StockMarket

class Intraday(StockMarket):
    def __init__(self, api_key):
        super().__init__(api_key)

    def setTimeSeriesName(self, interval):
        interval = interval if self.isValidInterval(interval) else '60min'
        self.time_series_name = "Time Series (" + interval + ')'

    def getIntraday(self, ticker, interval, adjusted = True, output_size = 'compact', data_type = 'json'):
        self.setTimeSeriesName(interval)
        params = {'function':'TIME_SERIES_INTRADAY', 'interval':interval, 'adjusted':adjusted, 'outputsize':output_size,  'symbol':ticker, 'datatype':data_type, 'apikey':self.api_key}
        response = self.getResponse(params)
        response = self.decodeJSONReponse(response) if data_type == 'json' else self.decodeCSVResponse(response)
        self.parse(response, self.time_series_name)

        return self

    def isValidInterval(self, interval):
        valid_intervals = ['1min', '5min', '15min', '30min', '60min']
        return interval in valid_intervals
