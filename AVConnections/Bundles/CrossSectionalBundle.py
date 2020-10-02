from AVStockData.AVConnections.CrossSectionalData.CompanyOverview import CompanyOverview
from AVStockData.AVConnections.CrossSectionalData.Quote import Quote
from AVStockData.AVConnections.Bundles.Bundle import Bundle

class CrossSectionalBundle(Bundle):
    def __init__(self, api_key, call_limit_per_minute = 5, call_limit_per_day = 500):
        super().__init__(api_key, call_limit_per_minute, call_limit_per_day)
        self.initializeObjectReferences()

    def initializeObjectReferences(self):
        self.CompanyOverview = CompanyOverview(self.api_key, callMeter = self.callMeter)
        self.Quote = Quote(self.api_key, callMeter = self.callMeter)
