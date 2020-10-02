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

    def getFundementalData(self, *tickers):
        result = FundementalData()
        for ticker in tickers:
            balanceSheetData = self.BalanceSheet.getBalanceSheet(ticker)
            cashFlowdata = self.CashFlow.getCashFlow(ticker)
            incomeStatementData = self.IncomeStatement.getIncomeStatement(ticker)
            companyOverviewData = self.CompanyOverview.getCompanyOverview(ticker)

            result.append({'ticker': ticker,
                           'balanceSheet': balanceSheetData.annual_reports,
                           'cashFlow': cashFlowdata.annual_reports,
                           'incomeStatement': incomeStatementData.annual_reports,
                           'companyOverview': companyOverviewData.numeric_data
                           })

        return result
