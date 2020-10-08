from AVStockData.AVConnections.Containers.FundementalData import FundementalData
import matplotlib.pyplot as plt


class CompanySummary:
    def __init__(self, fundemental_data):
        self.__isValidInput(fundemental_data)
        self.fundemental_data = fundemental_data

    def __isValidInput(self, fundemental_data):
        if not isinstance(fundemental_data, FundementalData):
            return ValueError('One of the arguments entered is not an instance of the FundementalData class.')

    def getTickers(self):
        return self.fundemental_data.tickers

    def getPeriod(self, ticker):
        return self.fundemental_data[ticker]['period']

    def getCompanyOverview(self, ticker):
        return self.fundemental_data[ticker]['companyOverview']

    def getCashFlow(self, ticker):
        return self.fundemental_data[ticker]['cashFlow']

    def getBalanceSheet(self, ticker):
        return self.fundemental_data[ticker]['balanceSheet']

    def getIncomeStatement(self, ticker):
        return self.fundemental_data[ticker]['incomeStatement']

    def getIncomeStatementMetric(self, ticker, metric):
        income_statement = self.getIncomeStatement(ticker)
        return income_statement.getMetric(metric)

    def getIncomeStatementSummaryMetric(self, ticker, metric):
        summary = self.getIncomeStatement(ticker).getSummary()
        return summary[metric]

    def getCompanyOverviewMetric(self, ticker, metric):
        numeric_data = self.fundemental_data[ticker]['companyOverview'].numeric_fields
        return numeric_data[metric]

    def show(self):
        return_item = {}
        for ticker in self.getTickers():
            return_item[ticker] = {
                'period': self.getPeriod(ticker),
                'balanceSheet': self.getBalanceSheet(ticker).time_series,
                'cashFlow': self.getCashFlow(ticker),
                'incomeStatement': self.getIncomeStatement(ticker),
                'companyOverview': self.getCompanyOverview(ticker)
            }

        return return_item
