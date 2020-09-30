from AVStockData.AVConnections.Containers.AVTimeSeries import AVTimeSeries
import matplotlib.pyplot as plt
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

class ReportMetrics(AVTimeSeries):
    def __init__(self, time_series):
        super().__init__(time_series)

        self.__parseTimeSeries()

    def getSummary(self):
        number_of_fields = len(self.fields)
        summary = [['Field Name', 'Mean', 'Min', 'Max', 'STD'], *[0]*number_of_fields]
        for index in range(0, number_of_fields):
            field = self.fields[index]
            values = self.__getMetricValues(field)
            mean = self.__caculateMean(values)
            std = self.__calculateStd(values)
            min_value = min(values)
            max_value = max(values)
            summary[index+1] = [field, mean, min_value, max_value, std]

        return summary

    def plotMetric(self, metric):
        values = self.__getMetricValues(metric)
        dates = self.timestamps
        plt.plot(dates, values)
        plt.gcf().autofmt_xdate()
        plt.axhline(y=0, color='r', linestyle='--')
        plt.xlabel("Date")
        plt.ylabel(metric)


    def __getValidValues(self, value_list):
        NaN = float('nan')
        return [value for value in value_list if value != NaN]

    def __calculateSSE(self, value_list, mean):
        sse = 0
        for value in value_list:
            sse += (value - mean)**2
        return sse

    def __calculateStd(self, value_list):
        valid_values = self.__getValidValues(value_list)
        n = len(valid_values)
        mean = self.__caculateMean(valid_values)
        sse = self.__calculateSSE(valid_values, mean)

        return (sse / n)**0.5

    def __caculateMean(self, value_list):
        valid_values = self.__getValidValues(value_list)
        value_count = len(valid_values)

        return sum(valid_values) / value_count

    def __getMetricValues(self, metric):
        metric_index = self.fields.index(metric) if self.fields.count(metric) > 0 else -1
        if metric_index < 0:
            return

        return [row[metric_index] for row in self.data_matrix]

    def __parseTimeSeries(self):
        time_series = self.time_series if self.utils.isCSV(self.time_series) else self.jsonToCSV(self.time_series)
        self.data_matrix = [series[1:] for series in time_series[1:]]
        self.fields = time_series[0][1:]
        self.timestamps = [datetime.strptime(timestamp[0], "%Y-%m-%d") for timestamp in time_series[1:]]
