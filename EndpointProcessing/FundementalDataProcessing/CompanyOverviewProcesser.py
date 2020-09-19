from AVStockData.EndpointProcessing.BaseProcessor import BaseProcessor
from AVStockData.AVConnections.AVFundementalData import AVFundementalData

class CompanyOverviewProcessor(BaseProcessor):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.getCompanyOverview = AVFundementalData(api_key).getCompanyOverview

    def getData(self, ticker):
        self.currentResult = self.getCompanyOverview(ticker)
        return self

    def toList(self):
        if self.currentResultIsList() | self.currentResultIsNone():
            return

        column_names = list(self.currentResult.keys())
        self.currentResult = [column_names, [self.currentResult[key] for key in column_names]]

        return self

    def toDict(self):
        if self.currentResultIsDict() | self.currentResultIsNone():
            return

        keys = self.currentResult[0]
        values = self.currentResult[1]
        self.currentResult = {keys[i]: values[i] for i in range(0, len(keys))}

        return self

    def show(self):
        return self.currentResult
