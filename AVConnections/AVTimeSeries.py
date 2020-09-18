from AVStockData.AVConnections.AVConnection import AVConnection
from AVStockData.AVConnections.ValidTimeSeriesParameters import ValidTimeSeriesParameters

class AVTimeSeries(AVConnection):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.validate = ValidTimeSeriesParameters()

    def isValidTicker(self, ticker):
        return True

    def getIntraday(self, ticker, interval, output_size='compact'):
        if not self.validate.isValidIntradayInterval(interval):
            return ValueError(interval + " is not a valid Intraday time interval.")

        if not self.validate.isValidOutputSize(output_size):
            return ValueError(output_size + " is not a valid output size.")

        params = {'function':'TIME_SERIES_INTRADAY','symbol':ticker, 'interval':interval, 'outputsize':output_size, 'apikey':self.api_key}
        response = self.getResponse(params)

        return self.decodeJSONRepsponse(response)

    def getIntradayExtended(self, ticker, interval, slice_val):
        if not self.validate.isValidIntradayInterval(interval):
            return ValueError(interval + " is not a valid Intraday time interval.")

        if not self.validate.isValidIntradaySlice(slice_val):
            return Warning("Invalid slice value entered for getIntradayExtended(...). Default value will be used.")

        if not self.validate.isValidOutputSize(output_size):
            return ValueError(output_size + " is not a valid output size.")

        params = {'function':'TIME_SERIES_INTRADAY_EXTENDED','symbol':ticker, 'interval':interval, 'slice':slice_val, 'apikey':self.api_key}
        response = self.getResponse(params)

        return self.decodeJSONReponse(response)
