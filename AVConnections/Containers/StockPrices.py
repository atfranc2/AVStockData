from AVStockData.AVConnections.Containers.AVTimeSeries import AVTimeSeries

class StockPriceSeries(AVTimeSeries):
    def __init__(self, time_series):
        super().__init__(time_series)
