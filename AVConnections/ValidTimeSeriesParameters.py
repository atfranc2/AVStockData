class ValidTimeSeriesParameters:
    def __init__(self):
        self.__valid_intraday_intervals = ['1min', '5min', '15min', '30min', '60min']
        self.__valid_output_sizes = ['compact', 'full']
        self.__valid_intraday_extented_slices = self.__getValidIntradaySlices()

    def __getValidIntradaySlices(self):
        validSlices = []
        for year in range(1, 3):
            for month in range(1, 13):
                validSlices.append("year" + str(year) + "month" + str(month))


    def isValidIntradaySlice(self, slice):
        return slice in self.__valid_intraday_extented_slices

    def isValidIntradayInterval(self, interval):
        return interval in self.__valid_intraday_intervals

    def isValidOutputSize(self, output_size):
        return output_size in self.__valid_output_sizes
