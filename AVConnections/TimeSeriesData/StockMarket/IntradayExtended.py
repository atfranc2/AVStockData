from AVStockData.AVConnections.AVConnection import AVConnection
from AVStockData.AVConnections.TimeSeriesData.StockMarket.StockMarket import StockMarket
from AVStockData.CallMeter import CallMeter

class IntradayExtended(StockMarket):
    def __init__(self, api_key, callMeter = CallMeter(call_limit_per_minute = 5, call_limit_per_day = 500)):
        super().__init__(api_key, callMeter)
        self.setTimeSeriesName()

    def setTimeSeriesName(self):
        self.time_series_name = None

    def getIntradayExtended(self, ticker, interval, slice_value, adjusted = True):
        params = {'function':'TIME_SERIES_INTRADAY_EXTENDED', 'interval':interval, 'slice':slice_value, 'adjusted':adjusted, 'symbol':ticker, 'apikey':self.api_key}
        response = self.getResponse(params)
        response = self.decodeCSVResponse(response)
        self.parse(response, self.time_series_name)

        return self

    def isValidInterval(self, interval):
        valid_intervals = ['1min', '5min', '15min', '30min', '60min']
        return interval in valid_intervals

    def isValidSlice(self, slice_value):
        validSlices = []
        for year in range(1, 3):
            for month in range(1, 13):
                validSlices.append("year" + str(year) + "month" + str(month))

        return slice_value in valid_slices
