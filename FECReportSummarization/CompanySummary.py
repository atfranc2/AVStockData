from AVStockData.AVConnections.Containers.FundementalData import FundementalData
from AVStockData.FECReportSummarization.ReportMetricCalculator import ReportMetricCalculator
import matplotlib.pyplot as plt


class CompanySummary:
    def __init__(self, fundemental_data):
        self.__isValidInput(fundemental_data)
        self.fundemental_data = fundemental_data
        self.__calculator = ReportMetricCalculator()

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

    def getBalanceSheetMetric(self, ticker, metric):
        balance_sheet = self.getBalanceSheet(ticker)
        return balance_sheet.getMetric(metric)

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

    def getEarningsGrowth(self, ticker):
        income_statement = self.getIncomeStatementMetric(ticker, 'netIncome')
        dates = [date for date in income_statement.keys()]
        len_dates = len(dates)

        past_earnings = [income_statement[date] for date in dates[1:]]
        current_earnings = [income_statement[date] for date in dates[:-1]]
        len_earnings = len(current_earnings)

        earnings_growth = [self.__calculator.calculateEarningsGrowth(current_earnings[index], past_earnings[index]) for index in range(0, len_earnings)]
        earnings_growth = [float('nan'), *earnings_growth]

        return {dates[index]: earnings_growth[index] for index in range(0, len_dates)}

    def getDebtToEquity(self, ticker):
        total_liabilities = self.getBalanceSheetMetric(ticker, 'totalLiabilities')
        total_shareholder_equities = self.getBalanceSheetMetric(ticker, 'totalShareholderEquity')
        dates = total_liabilities.keys()
        debt_to_equities = {date: self.__calculator.calculateDebtToEquity(total_liabilities[date], total_shareholder_equities[date]) for date in dates}

        return debt_to_equities


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
