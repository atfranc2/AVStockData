from AVStockData.AVConnections.Containers.AVTimeSeries import AVTimeSeries
import matplotlib.pyplot as plt
import math
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

class StockPriceSeries(AVTimeSeries):
    def __init__(self, time_series):
        super().__init__(time_series)
        self.__parseTimeSeries()

    def plotReturnHist(self, return_time = 'close', return_type = 'geometric', bins = 30):
        return_time = self.__getReturnTime(return_time)
        return_type = self.__getReturnType(return_type)
        returns = self.calculateReturns(return_time, return_type)
        plt.hist(returns["Returns"][1:], bins = bins)
        plt.xlabel('Bin')
        plt.ylabel('Bin Count')

    def plotReturns(self, return_time = 'close', return_type = 'geometric'):
        return_time = self.__getReturnTime(return_time)
        return_type = self.__getReturnType(return_type)
        returns = self.calculateReturns(return_time, return_type)
        plt.plot(returns["Dates"][1:], returns["Returns"][1:])
        plt.axhline(y=0, color='r', linestyle='--')
        plt.xlabel('Date')
        plt.ylabel(return_type + ' return on ' + return_time + ' price')

    def calculateReturns(self, return_time = 'close', return_type = 'geometric'):
        return_time = self.__getReturnTime(return_time)
        return_type = self.__getReturnType(return_type)

        if return_time == 'close' and return_type == 'geometric':
            return self.calculateGeometricReturnsOnClose()

        if return_time == 'open' and return_type == 'geometric':
            return self.calculateArithmeticReturnsOnClose()

        if return_time == 'close' and return_type == 'arithmetic':
            return self.calculateArithmeticReturnsOnClose()

        if return_time == 'open' and return_type == 'arithmetic':
            return self.calculaterithmeticReturnsOnOpen()

    def calculateGeometricReturnsOnClose(self):
        dates = self.timestamps
        prices = self.closing_prices
        shifted_prices = [float('nan'), *self.closing_prices[:-1]]

        trading_days = len(prices)
        geometric_returns = [0]*trading_days

        for index in range(0, trading_days):
            geometric_returns[index] = math.log(prices[index]) - math.log(shifted_prices[index])

        return {"Dates": dates, "Returns": geometric_returns}

    def calculateArithmeticReturnsOnClose(self):
        dates = self.timestamps[1:]
        prices = self.closing_prices[1:]
        shifted_prices = self.closing_prices[:-1]

        trading_days = len(prices)
        arithmetic_returns = [0]*trading_days

        for index in range(0, trading_days):
            arithmetic_returns[index] = (prices[index] - shifted_prices[index]) / shifted_prices[index]

        return {"Dates": dates, "Returns": arithmetic_returns}

    def calculateGeometricReturnsOnOpen(self):
        dates = self.timestamps[1:]
        prices = self.opening_prices[1:]
        shifted_prices = self.opening_prices[:-1]

        trading_days = len(prices)
        geometric_returns = [0]*trading_days

        for index in range(0, trading_days):
            geometric_returns[index] = math.log(prices[index]) - math.log(shifted_prices[index])

        return {"Dates": dates, "Return": geometric_returns}

    def calculaterithmeticReturnsOnOpen(self):
        dates = self.timestamps[1:]
        prices = self.opening_prices[1:]
        shifted_prices = self.opening_prices[:-1]

        trading_days = len(prices)
        arithmetic_returns = [0]*trading_days

        for index in range(0, trading_days):
            arithmetic_returns[index] = (prices[index] - shifted_prices[index]) / shifted_prices[index]

        return {"Dates": dates, "Returns": arithmetic_returns}

    def plotLow(self):
        plt.plot(self.timestamps, self.low_prices)
        plt.gcf().autofmt_xdate()
        plt.xlabel("Date")
        plt.ylabel("Stock Price")

    def plotHigh(self):
        plt.plot(self.timestamps, self.high_prices)
        plt.gcf().autofmt_xdate()
        plt.xlabel("Date")
        plt.ylabel("Stock Price")

    def plotOpen(self):
        plt.plot(self.timestamps, self.opening_prices)
        plt.gcf().autofmt_xdate()
        plt.xlabel("Date")
        plt.ylabel("Stock Price")

    def plotClose(self):
        plt.plot(self.timestamps, self.closing_prices)
        plt.gcf().autofmt_xdate()
        plt.xlabel("Date")
        plt.ylabel("Stock Price")

    def plotVolume(self):
        plt.plot(self.timestamps, self.volumes)
        plt.gcf().autofmt_xdate()
        plt.xlabel("Date")
        plt.ylabel("Volume")

    def __parseTimeSeries(self):
        time_series = self.time_series if self.utils.isCSV(self.time_series) else self.jsonToCSV(self.time_series)
        self.timestamps = [datetime.strptime(row[0], "%Y-%m-%d") for row in time_series[1:]]
        self.opening_prices = [row[1] for row in time_series[1:]]
        self.high_prices = [row[2] for row in time_series[1:]]
        self.low_prices = [row[3] for row in time_series[1:]]
        self.closing_prices = [row[4] for row in time_series[1:]]
        self.volumes = [row[5] for row in time_series[1:]]

    def __getReturnTime(self, return_time):
        valid_return_times = ['open', 'close']
        return 'close' if return_time.lower() not in valid_return_times else return_time.lower()

    def __getReturnType(self, return_type):
        valid_return_types = ['geometric', 'arithmetic']
        return 'geometric' if return_type.lower() not in valid_return_types else return_type.lower()
