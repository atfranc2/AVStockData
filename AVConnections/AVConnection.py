import requests
from abc import ABC, abstractmethod

class AVConnection(ABC):

    def __init__(self, api_key):
        self.__base_query_string = 'https://www.alphavantage.co/query?'
        self.api_key = api_key

    def __callHasError(self, response_dict):
        return True if response_dict.get('Error Message', False) else False

    def __callLimitExceeded(self, repsonse_dict):
        return True if response_dict.get('Note', False) else False

    def __getResponse(self, params):
        return requests.get(self.__base_query_string, params = params)

    def __isValidApiKey(self, api_key):
        test_params = {'function':'TIME_SERIES_DAILY','symbol':'PG','apikey':api_key}
        response = self.__getResponse(params = test_params)
        response_json = response.json()

        if self.__callHasError(response_json):
            return False

        return True

    @abstractmethod
    def __isValidTicker(self, ticker):
        pass

    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self, api_key):
        if not self.__isValidApiKey(api_key):
            raise ValueError("The API key entered is not a valid Alpha Vantage API key")

        self.__api_key = api_key
