from AVStockData.AVConnections.AVConnection import AVConnection

class Daily(AVConnection):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.time_series = None
        self.__time_series_name = 'Time Series (Daily)'

    def getDaily(self, ticker, output_size = 'compact', data_type = 'json'):
        params = {'function':'TIME_SERIES_DAILY', 'symbol':ticker, 'outputsize':output_size, 'datatype':data_type, 'apikey':self.api_key}
        response = self.getResponse(params)
        response = self.decodeJSONReponse(response) if data_type == 'json' else self.decodeCSVResponse(response)
        self.parse(response)

        return self

    def isValidOutputSize(self, output_size):
        valid_output_sizes = ['compact', 'full']
        return output_size in valid_output_sizes

    def isValidDataType(self, data_type):
        valid_data_types = ['json', 'csv']
        return data_type in valid_data_types

    def unpackCsvResponse(self, csv_response):
        number_of_rows = len(csv_response)
        number_of_columns = len(csv_response[0])

        for row in range(1, number_of_rows):
            for column in range(1, number_of_columns):
                csv_response[row][column] = self.__stringToNumeric(csv_response[row][column])

        return csv_response

    def parseCSV(self, csv_response):
        self.symbol = None
        self.last_refreshed = None
        self.output_size = None
        self.time_zone = None

        self.time_series = self.unpackCsvResponse(csv_response)

    def __isNaN(self, value):
        try:
            float(value)
            return False
        except:
            return True

    def __stringToNumeric(self, value):
        numeric_value = float('nan') if self.__isNaN(value) else float(value)

        return numeric_value

    def unpackJsonResponse(self, json_response):
        time_series = json_response[self.__time_series_name]
        times = time_series.keys()
        return {time: {key[3:]: self.__stringToNumeric(time_series[time][key]) for key in time_series[time]} for time in times}

    def parseJSON(self, json_response):
        self.symbol = json_response["Meta Data"]["2. Symbol"]
        self.last_refreshed = json_response["Meta Data"]["3. Last Refreshed"]
        self.output_size = json_response["Meta Data"]["4. Output Size"]
        self.time_zone = json_response["Meta Data"]["5. Time Zone"]

        self.time_series = unpackJsonResponse(json_response)
