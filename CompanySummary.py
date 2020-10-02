from AVStockData.AVConnections.Containers.FundementalData import FundementalData

class CompanyComparer:
    def __init__(self, *fundemental_data):
        self.areValidInputs()
        self.fundemental_data = fundemental_data

    def areValidInputs(self):
        for data in self.fundemental_data:
            if not isinstance(data, FundementalData):
                return ValueError('One of the arguments entered is not an instance of the CrossSectionalBundle Class')
