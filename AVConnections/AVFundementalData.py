from AVConnection import AVConnection

class AVFundementalData(AVConnection):
    def __init__(self, api_key):
        super().__init__(api_key)


    def __isValidTicker(self, ticker):
        return True

    def getCompanyOverview(self, ticker):
        params = {'function':'OVERVIEW','symbol':ticker,'apikey':api_key}
        response = self.__getResponse(params)
        return response.json()

    def getIncomeStatement(self, ticker):
        params = {'function':'INCOME_STATEMENT','symbol':ticker,'apikey':api_key}
        response = self.__getResponse(params)
        return response.json()

    def getBalanceSheet(self, ticker):
        params = {'function':'BALANCE_SHEET','symbol':ticker,'apikey':api_key}
        response = self.__getResponse(params)
        return response.json()

    def getCashFlow(self, ticker):
        params = {'function':'CASH_FLOW','symbol':ticker,'apikey':api_key}
        response = self.__getResponse(params)
        return response.json()

    def getListingStatus(self, ticker, status = 'active'):
        params = {'function':'LISTING_STATUS','symbol':ticker, 'status':status, 'apikey':api_key}
        response = self.__getResponse(params)
        return response.json()
