
class ReportMetricCalculator:
    def __init__(self):
        pass

    def calculateDebtToEquity(self, total_liability, total_shareholder_equity):
        return total_liability / total_shareholder_equity

    def calculateMarketCapitalization(self, shares_outstanding, share_price):
        return shares_outstanding * share_price

    def calculatePERatio(self, net_income, shares_outstanding, share_price):
        market_capitalization = self.calculateMarketCapitalization(shares_outstanding, share_price)
        return market_capitalization / net_income

    def calculateEarningsGrowth(self, current_income, past_income):
        return (current_income - past_income) / past_income
