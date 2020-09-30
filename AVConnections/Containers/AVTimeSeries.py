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

    def jsonToCSV(self, json_item):
        if self.utils.isCSV(json_item):
            return json_item

        dates = [key for key in json_item.keys()]
        headers = ['timestamp', *[key for key in json_item[dates[1]].keys()]]
        data = [headers, *[0]*len(dates)]

        for index in range(1, len(data)):
            dates_index = index - 1
            date_key = dates[dates_index]
            data_dict = json_item[date_key]
            data[index] = [date_key, *[data_dict[key] for key in data_dict.keys()]]

        return data

    def toJson(self):
        if self.utils.isJson(self.time_series):
            return self

        self.time_series = self.jsonToCSV(self.time_series)

        return self

    def csvToJson(self, csv_item):
        if self.utils.isJson(csv_item):
            return csv_item

        inner_keys = csv_item[0][1:]
        date_keys = [date[0] for date in csv_item[1:]]
        json_series = {}
        for date_index in range(0, len(date_keys)):
            date = date_keys[date_index]
            inner_json = {}
            for key_index in range(0, len(inner_keys)):
                inner_json[inner_keys[key_index]] = csv_item[date_index+1][key_index+1]

            json_series[date] = inner_json

        return json_series
