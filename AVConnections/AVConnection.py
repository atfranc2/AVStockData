import requests
import csv

class AVConnection():

    def __init__(self, api_key):
        self.__base_query_string = 'https://www.alphavantage.co/query?'
        self.api_key = api_key
        self.is_json = False
        self.is_csv = False

    def __isValidApiKey(self, api_key):
        test_params = {'function':'TIME_SERIES_DAILY','symbol':'PG','apikey':api_key}
        response = self.getResponse(params = test_params)
        response_json = self.decodeJSONReponse(response)

        if self.callHasError(response_json):
            return False

        return True

    def callHasError(self, response, is_json_response = True):
        if is_json_response:
            return True if response.get('Error Message', False) else False

        return True

    def callLimitExceeded(self, response, is_json_response = True):
        if is_json_response:
            return True if response.get('Note', False) else False

        return True

    def serverResultIsDict(self):
        if type(self.resultFromServer) == dict:
            return True

        return False

    def serverResultIsList(self):
        if type(self.resultFromServer) == list:
            return True

        return False

    def serverResultIsNone(self):
        return type(self.resultFromServer) == None

    def setDataTypeToJson(self):
        self.is_json = True
        self.is_csv = False

    def setDataTypeToCSV(self):
        self.is_json = False
        self.is_csv = True

    def decodeCSVResponse(self, response):
        decoded_content = response.content.decode('utf-8')
        decoded_content = csv.reader(decoded_content.splitlines(), delimiter=',')
        self.setDataTypeToCSV()

        return list(decoded_content)

    def decodeJSONReponse(self, response):
        self.setDataTypeToJson()

        return response.json()

    def getResponse(self, params):
        return requests.get(self.__base_query_string, params = params)

    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self, api_key):
        self.__api_key = api_key
