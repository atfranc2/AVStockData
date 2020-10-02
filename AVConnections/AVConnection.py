import requests
import csv
from time import time, sleep
from abc import ABC, abstractmethod
from AVStockData.CallMeter import CallMeter

class AVConnection(ABC):

    def __init__(self, callMeter = CallMeter(call_limit_per_minute = 5, call_limit_per_day = 500)):
        self.__base_query_string = 'https://www.alphavantage.co/query?'
        self.is_json = False
        self.is_csv = False
        self.callMeter = callMeter

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
        self.callMeter.incrementCalls()
        return requests.get(self.__base_query_string, params = params)

    def callHasError(self, response):
        if self.is_json:
            return True if response.get('Error Message', False) else False

        return True if response[1][0].count("Error Message") else False

    def callLimitExceeded(self, response):
        if self.is_json:
            return True if response.get('Note', False) else False

        return True if response[1][0].count("Note") > 0 else False
