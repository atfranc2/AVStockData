from AVStockData.AVConnections.Utils import Utils

class AVTimeSeries:
    def __init__(self, time_series):
        self.time_series = time_series
        self.utils = Utils()

    def show(self):
        return self.time_series

    def toCSV(self):
        if self.utils.isCSV(self.time_series):
            return self

        dates = [key for key in self.time_series.keys()]
        headers = ['timestamp', *[key for key in self.time_series[dates[1]].keys()]]
        data = [headers, *[0]*len(dates)]

        for index in range(1, len(data)):
            dates_index = index - 1
            date_key = dates[dates_index]
            data_dict = self.time_series[date_key]
            data[index] = [date_key, *[data_dict[key] for key in data_dict.keys()]]

        self.time_series = data

        return self

    def toJson(self):
        if self.utils.isJson(self.time_series):
            return self

        inner_keys = self.time_series[0][1:]
        date_keys = [date[0] for date in self.time_series[1:]]
        json_series = {}
        for date_index in range(0, len(date_keys)):
            date = date_keys[date_index]
            inner_json = {}
            for key_index in range(0, len(inner_keys)):
                inner_json[inner_keys[key_index]] = self.time_series[date_index+1][key_index+1]

            json_series[date] = inner_json

        self.time_series = json_series

        return self
