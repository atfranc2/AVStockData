from AVStockData.AVConnections.Containers.FundementalData import FundementalData
import matplotlib.pyplot as plt


class CompanyComparer:
    def __init__(self, fundemental_data):
        self.__isValidInput(fundemental_data)
        self.fundemental_data = fundemental_data

    def __isValidInput(self, fundemental_data):
        if not isinstance(fundemental_data, FundementalData):
            return ValueError('One of the arguments entered is not an instance of the FundementalData class.')

    def __drawSubPlot(rows, columns, plot_number, x_values, y_values):
        plot_id = int(str(rows) + str(columns) + str(plot_number))

        plt.subplot(plot_id)
        plt.plot(x_values, y_values)

    def getSummaryPlot(self, ticker):
        plt.figure(figsize=(8,8))
        total_revenue = self.getIncomeStatementMetric(ticker, 'totalRevenue')
        total_revenue_dates = list(total_revenue.keys())
        total_revenue_values = [total_revenue[key] for key in total_revenue_dates]

        net_income = self.getIncomeStatementMetric(ticker, 'netIncome')
        net_income_dates = list(net_income.keys())
        net_income_values = [net_income[key] for key in net_income_dates]

        plt.subplot(211)
        plt.plot(total_revenue_dates, total_revenue_values)
        plt.xlabel('Date')
        plt.ylabel('Total Revenue')

        plt.subplot(212)
        plt.plot(net_income_dates, net_income_values)
        plt.xlabel('Date')
        plt.ylabel('Net Income')

    def getSummaryPlots(self):
        tickers = self.getTickers()

        plt.figure(figsize=(8,8))
        for ticker in tickers:
            total_revenue = self.getIncomeStatementMetric(ticker, 'totalRevenue')
            total_revenue_dates = list(total_revenue.keys())
            total_revenue_values = [total_revenue[key] for key in total_revenue_dates]

            net_income = self.getIncomeStatementMetric(ticker, 'netIncome')
            net_income_dates = list(net_income.keys())
            net_income_values = [net_income[key] for key in net_income_dates]

            plt.subplot(211)
            plt.plot(total_revenue_dates, total_revenue_values)
            plt.xlabel('Date')
            plt.ylabel('Total Revenue')
            plt.legend(tickers)

            plt.subplot(212)
            plt.plot(net_income_dates, net_income_values)
            plt.xlabel('Date')
            plt.ylabel('Net Income')
            plt.legend(tickers)

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

    def summary(self, ticker):
        net_income = self.getIncomeStatementSummaryMetric(ticker, 'netIncome')
        total_revenue = self.getIncomeStatementSummaryMetric(ticker, 'totalRevenue')
        pe_ratio = self.getCompanyOverviewMetric(ticker, 'PERatio')
        peg_ratio = self.getCompanyOverviewMetric(ticker, 'PEGRatio')
        pb_ratio = self.getCompanyOverviewMetric(ticker, 'PriceToBookRatio')
        ps_ratio_ttm = self.getCompanyOverviewMetric(ticker, 'PriceToSalesRatioTTM')
        dividend_yield = self.getCompanyOverviewMetric(ticker, 'DividendYield')
        period = self.getPeriod(ticker)

        summary = {
            'date': self.fundemental_data[ticker]['date'],
            'price': self.fundemental_data[ticker]['price'],
            'sector': self.fundemental_data[ticker]['sector'],
            'industry': self.fundemental_data[ticker]['industry'],
            'net_income': {'value': net_income['mean'], 'type': 'mean', 'sample_size': net_income['N'], 'period': period},
            'total_revenue': {'value': total_revenue['mean'], 'type': 'mean', 'sample_size': total_revenue['N'], 'period': period},
            'pe_ratio': {'value': pe_ratio, 'type': 'point', 'sample_size': 1, 'period': period},
            'peg_ratio': {'value': peg_ratio, 'type': 'point', 'sample_size': 1, 'period': period},
            'pb_ratio': {'value': pb_ratio, 'type': 'point', 'sample_size': 1, 'period': period},
            'ps_ratio_ttm': {'value': ps_ratio_ttm, 'type': 'mean', 'sample_size': 12, 'period': 'Month'},
            'dividend_yield': {'value': dividend_yield, 'type': 'point', 'sample_size': 1, 'period': self.getPeriod(ticker)}
        }

        return summary


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
