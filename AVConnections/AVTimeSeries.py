from AVConnection import AVConnection

class AVTimeSeries(AVConnection):
    def __init__(self, api_key):
        super().__init__(api_key)

    def getIntraDay(self, ticker):
        params = {'function':'TIME_SERIES_INTRADAY','symbol':ticker,'apikey':api_key}
        response = self.__getResponse(params)
        return response.json()
