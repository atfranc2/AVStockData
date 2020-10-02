from AVStockData.AVConnections.AVConnection import AVConnection
from AVStockData.CallMeter import CallMeter
from abc import ABC, abstractmethod


class Bundle(ABC):
    def __init__(self, api_key, call_limit_per_minute = 5, call_limit_per_day = 500):
        self.callMeter = CallMeter(call_limit_per_minute, call_limit_per_day)
        self.connection = AVConnection(self.callMeter)
        self.__api_key = api_key
        self.__validateAPIKey(api_key)

    def __isValidApiKey(self, api_key):
        test_params = {'function':'GLOBAL_QUOTE','symbol':'PG', 'datatype':'json', 'apikey':api_key}
        response = self.connection.getResponse(params = test_params)
        response_json = self.connection.decodeJSONReponse(response)
        if self.connection.callHasError(response_json):
            return False

        return True

    @abstractmethod
    def initializeObjectReferences(self):
        pass

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
