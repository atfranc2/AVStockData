from AVStockData.AVConnections.Containers.AVTimeSeries import AVTimeSeries
from AVStockData.AVConnections.Utils import Utils
import matplotlib.pyplot as plt
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

class ReportMetrics(AVTimeSeries):
    def __init__(self, time_series):
        super().__init__(time_series)
        self.utils = Utils()
        self.__parseTimeSeries()

    def getSummary(self):
        fields = self.__getFields()
        number_of_fields = len(fields)
        summary = {}
        for index in range(0, number_of_fields):
            field = fields[index]
            values = self.__getMetricValues(field)
            valid_values = self.__getValidValues(values)
            valid_value_count = len(valid_values)

            summary[field] = {
                'mean': self.__caculateMean(valid_values),
                'std': self.__caculateMean(valid_values),
                'min': min(valid_values) if valid_value_count > 0 else float('nan'),
                'max': max(valid_values)if valid_value_count > 0 else float('nan'),
                'N': valid_value_count
            }

        return summary

    def getMetric(self, metric):
        return {date: self.time_series[date][metric] for date in self.__getDates()}

    def plotMetric(self, metric):
        values = self.__getMetricValues(metric)
        dates = self.__getDates()
        plt.plot(dates, values)
        plt.gcf().autofmt_xdate()
        plt.axhline(y=0, color='r', linestyle='--')
        plt.xlabel("Date")
        plt.ylabel(metric)

    def __getDates(self):
        date_list = list(self.time_series.keys())

        return date_list

    def __getFields(self):
        dates = self.__getDates()
        field_list = list(self.time_series[dates[0]].keys())

        return field_list

    def __getValidValues(self, value_list):
        return [value for value in value_list if str(value) != 'nan']

    def __calculateSSE(self, value_list, mean):
        sse = 0
        for value in value_list:
            sse += (value - mean)**2
        return sse

    def __calculateStd(self, value_list):
        n = len(value_list)
        mean = self.__caculateMean(value_list)
        sse = self.__calculateSSE(value_list, mean)

        return (sse / n)**0.5 if n != 0 else float('nan')

    def __caculateMean(self, value_list):
        value_count = len(value_list)

        return sum(value_list) / value_count if value_count != 0 else float('nan')

    def __getMetricValues(self, metric):
        dates = self.__getDates()
        valid_metrics = self.__getFields()
        is_valid_metric = metric in valid_metrics

        if not is_valid_metric:
            return

        return [value[metric] for value in [self.time_series[date] for date in dates]]

    def __parseTimeSeries(self):
        raw_time_series = self.time_series if self.utils.isJson(self.time_series) else self.csvToJson(self.time_series)
        self.time_series = {datetime.strptime(date, '%Y-%m-%d'): raw_time_series[date] for date in raw_time_series.keys()}
