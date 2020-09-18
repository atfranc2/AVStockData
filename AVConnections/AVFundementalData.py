from AVStockData.AVConnections.AVConnection import AVConnection
from AVStockData.AVConnections.ValidFundementalDataParameters import ValidFundementalDataParameters

class AVFundementalData(AVConnection):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.validate = ValidFundementalDataParameters()

    def getCompanyOverview(self, ticker):
        params = {'function':'OVERVIEW','symbol':ticker,'apikey':self.api_key}
        response = self.getResponse(params)
        return self.decodeJSONReponse(response)

    def getIncomeStatement(self, ticker):
        params = {'function':'INCOME_STATEMENT','symbol':ticker,'apikey':self.api_key}
        response = self.getResponse(params)
        return self.decodeJSONReponse(response)

    def getBalanceSheet(self, ticker):
        params = {'function':'BALANCE_SHEET','symbol':ticker,'apikey':self.api_key}
        response = self.getResponse(params)
        return self.decodeJSONReponse(response)

    def getCashFlow(self, ticker):
        params = {'function':'CASH_FLOW','symbol':ticker,'apikey':self.api_key}
        response = self.getResponse(params)

        return self.decodeJSONReponse(response)

    def getListingStatus(self, status = 'active', date = None):
        if not self.validate.isValidListingStatus(status):
            status = 'active'
            return Warning("An invalid value for status was passed in getListingStatus(...). Status of active will be used for stock with symbol = {ticker}.")

        params = {'function':'LISTING_STATUS','status':status, 'date':date, 'apikey':self.api_key}
        response = self.getResponse(params)

        return self.decodeCSVResponse(response)
