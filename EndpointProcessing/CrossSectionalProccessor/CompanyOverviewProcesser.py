from AVStockData.EndpointProcessing.CrossSectionalProccessor.CrossSectionalBase import CrossSectionalBaseProcessor
from AVStockData.AVConnections.AVFundementalData import AVFundementalData

class CompanyOverviewProcessor(CrossSectionalBaseProcessor):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.getCompanyOverview = AVFundementalData(api_key).getCompanyOverview

    def getData(self, ticker):
        self.currentResult = self.getCompanyOverview(ticker)
        return self
