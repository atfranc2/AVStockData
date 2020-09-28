from AVStockData.AVConnections.AVConnection import AVConnection
from AVStockData.AVConnections.Containers.AVCrossSectional import AVCrossSectional
from AVStockData.AVConnections.Utils import Utils
from AVStockData.AVConnections.Containers.AVCrossSectional import AVCrossSectional

class Quote(AVConnection):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.symbol = None
        self.last_traded = None
        self.numeric_data = None

        self.__Util = Utils()

    def getQuote(self, ticker, data_type = 'json'):
        params = {'function':'GLOBAL_QUOTE','symbol':ticker, 'datatype':data_type, 'apikey':self.api_key}
        response = self.getResponse(params)
        response = self.decodeJSONReponse(response) if data_type == 'json' else self.decodeCSVResponse(response)
        self.parse(response, data_type)

        return self

    def getExcludedFields(self):
        return ['symbol', 'latest trading day']

    def unpackJsonResponse(self, json_response):
        return {key: json_response[key] for key in json_response if key not in self.getExcludedFields()}

    def parseJsonResponse(self, json_response):
        quote = {key[4:]: json_response["Global Quote"][key] for key in json_response["Global Quote"].keys()}
        self.symbol = quote['symbol']
        self.last_traded = quote['latest trading day']

        quote['change percent'] = quote['change percent'].replace("%", "")
        self.numeric_data = AVCrossSectional({key: self.__Util.stringToNumeric(quote[key]) for key in quote.keys() if key not in self.getExcludedFields()})

    def parseCsvResponse(self, csv_response):
        self.symbol = csv_response[1][0]
        self.last_traded = csv_response[1][6]

        headers = [*csv_response[0][1:6], *csv_response[0][7:9]]
        data = [*csv_response[1][1:6], *csv_response[1][7:9]]
        data[-1] = data[-1].replace("%", "")
        self.numeric_data = [headers, [self.__Util.stringToNumeric(value) for value in data]]

    def parse(self, response, data_type):
        if (data_type == 'json'):
            self.parseJsonResponse(response)
        else:
            self.parseCsvResponse(response)
