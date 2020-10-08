from AVStockData.AVConnections.Containers.FundementalData import FundementalData
from AVStockData.FECReportSummarization.CompanySummary import CompanySummary
import matplotlib.pyplot as plt
from pandas import DataFrame

class CompanyComparer(CompanySummary):
    def __init__(self, fundemental_data):
        super().__init__(fundemental_data)

    def getSummaryPlot(self, ticker):
        total_revenue = self.getIncomeStatementMetric(ticker, 'totalRevenue')
        total_revenue_dates = list(total_revenue.keys())
        total_revenue_values = [total_revenue[key] for key in total_revenue_dates]

        net_income = self.getIncomeStatementMetric(ticker, 'netIncome')
        net_income_dates = list(net_income.keys())
        net_income_values = [net_income[key] for key in net_income_dates]

        plt.figure(figsize=(8,8))
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

        fig, (ax1, ax2) = plt.subplots(2, figsize=(8,8))
        ax1.set(xlabel='Date', ylabel='Total Revenue')
        ax2.set(xlabel='Date', ylabel='Net Income')

        for ticker in tickers:
            total_revenue = self.getIncomeStatementMetric(ticker, 'totalRevenue')
            total_revenue_dates = list(total_revenue.keys())
            total_revenue_values = [total_revenue[key] for key in total_revenue_dates]

            net_income = self.getIncomeStatementMetric(ticker, 'netIncome')
            net_income_dates = list(net_income.keys())
            net_income_values = [net_income[key] for key in net_income_dates]

            ax1.plot(total_revenue_dates, total_revenue_values)
            ax2.plot(net_income_dates, net_income_values)

        ax1.legend(tickers)
        ax2.legend(tickers)

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
            'date': {'value': self.fundemental_data[ticker]['date'], 'type': 'attribute', 'sample_size': None, 'period': period},
            'price': {'value': self.fundemental_data[ticker]['price'], 'type': 'attribute', 'sample_size': None, 'period': period},
            'sector': {'value': self.fundemental_data[ticker]['sector'], 'type': 'attribute', 'sample_size': None, 'period': period},
            'industry': {'value': self.fundemental_data[ticker]['industry'], 'type': 'attribute', 'sample_size': None, 'period': period},
            'net_income': {'value': net_income['mean'], 'type': 'mean', 'sample_size': net_income['N'], 'period': period},
            'total_revenue': {'value': total_revenue['mean'], 'type': 'mean', 'sample_size': total_revenue['N'], 'period': period},
            'pe_ratio': {'value': pe_ratio, 'type': 'point', 'sample_size': 1, 'period': period},
            'peg_ratio': {'value': peg_ratio, 'type': 'point', 'sample_size': 1, 'period': period},
            'pb_ratio': {'value': pb_ratio, 'type': 'point', 'sample_size': 1, 'period': period},
            'ps_ratio_ttm': {'value': ps_ratio_ttm, 'type': 'mean', 'sample_size': 12, 'period': 'Month'},
            'dividend_yield': {'value': dividend_yield, 'type': 'point', 'sample_size': 1, 'period': self.getPeriod(ticker)}
        }

        return summary

    def compare(self):
        comparison_table = []
        tickers = self.getTickers()
        for ticker in tickers:
            company_summary = self.summary(ticker)
            column_names = list(company_summary.keys())
            comparison_table.append([company_summary[key]['value'] for key in column_names])

        return DataFrame(comparison_table, index = tickers, columns = column_names)
