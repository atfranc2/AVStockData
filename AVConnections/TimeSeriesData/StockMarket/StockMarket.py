from AVStockData.AVConnections.AVConnection import AVConnection
from AVStockData.AVConnections.Containers.StockPrices import StockPriceSeries
from abc import ABC, abstractmethod

class StockMarket(AVConnection, ABC):
    def __init__(self, api_key):
        super().__init__(api_key)

        self.time_series = None
        self.symbol = None
        self.last_refreshed = None
        self.time_zone = None

    @abstractmethod
    def setTimeSeriesName(self):
        pass

    def __unpackCsvResponse(self, csv_response):
        number_of_rows = len(csv_response)
        number_of_columns = len(csv_response[0])

        for row in range(1, number_of_rows):
            for column in range(1, number_of_columns):
                csv_response[row][column] = self.__stringToNumeric(csv_response[row][column])

        return csv_response

    def __parseCSV(self, csv_response):
        self.symbol = None
        self.last_refreshed = None
        self.time_zone = None

        self.time_series = StockPriceSeries(self.__unpackCsvResponse(csv_response))

    def __isNaN(self, value):
        try:
            float(value)
            return False
        except:
            return True

    def __stringToNumeric(self, value):
        numeric_value = float('nan') if self.__isNaN(value) else float(value)

        return numeric_value

    def __unpackJsonResponse(self, json_response, time_series_name):
        time_series = json_response[time_series_name]
        times = time_series.keys()
        return {time: {key[3:]: self.__stringToNumeric(time_series[time][key]) for key in time_series[time]} for time in times}

    def __parseJSON(self, json_response, time_series_name):
        meta_data = {key[3:]: json_response["Meta Data"][key] for key in json_response["Meta Data"].keys()}
        self.symbol = meta_data["Symbol"]
        self.last_refreshed = meta_data["Last Refreshed"]
        self.time_zone = meta_data["Time Zone"]

        self.time_series = StockPriceSeries(self.__unpackJsonResponse(json_response, time_series_name))

    def parse(self, response, time_series_name):
        if self.is_csv:
            self.__parseCSV(response)
        else:
            self.__parseJSON(response, time_series_name)
