from AVStockData.AVConnections.CrossSectionalData.CompanyOverview import CompanyOverview
from AVStockData.AVConnections.TimeSeriesData.FECReports.IncomeStatement import IncomeStatement
from AVStockData.AVConnections.TimeSeriesData.FECReports.CashFlow import CashFlow
from AVStockData.AVConnections.TimeSeriesData.FECReports.BalanceSheet import BalanceSheet
from AVStockData.AVConnections.Containers.FundementalData import FundementalData
from AVStockData.AVConnections.Bundles.Bundle import Bundle

class FundementalBundle(Bundle):
    def __init__(self, api_key, call_limit_per_minute = 5, call_limit_per_day = 500):
        super().__init__(api_key, call_limit_per_minute, call_limit_per_day)
        self.initializeObjectReferences()

    def initializeObjectReferences(self):
        self.BalanceSheet = BalanceSheet(self.api_key, callMeter = self.callMeter)
        self.CashFlow = CashFlow(self.api_key, callMeter = self.callMeter)
        self.IncomeStatement = IncomeStatement(self.api_key, callMeter = self.callMeter)
        self.CompanyOverview = CompanyOverview(self.api_key, callMeter = self.callMeter)

    def getFundementalData(self, *tickers, annual_report = True):
        result = FundementalData()
        period = 'Year' if annual_report else 'Quarter'
        for ticker in tickers:
            balance_sheet = self.BalanceSheet.getBalanceSheet(ticker)
            balance_sheet_reports = balance_sheet.annual_reports if annual_report else balance_sheet.quarterly_reports

            cash_flow = self.CashFlow.getCashFlow(ticker)
            cash_flow_reports = cash_flow.annual_reports if annual_report else cash_flow.quarterly_reports

            income_statement = self.IncomeStatement.getIncomeStatement(ticker)
            income_statement_reports = income_statement.annual_reports if annual_report else income_statement.quarterly_reports

            company_overview = self.CompanyOverview.getCompanyOverview(ticker)
            company_overview_report = company_overview.numeric_data

            result.append({'ticker': ticker,
                           'period': period,
                           'balanceSheet': balance_sheet_reports,
                           'cashFlow': cash_flow_reports,
                           'incomeStatement': income_statement_reports,
                           'companyOverview': company_overview_report
                           })

        return result
