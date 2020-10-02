
class FundementalData:
    def __init__(self):
        self.tickers = []
        self.balance_sheets = []
        self.cash_flows = []
        self.income_statements = []
        self.company_overviews = []

    def isValidInput(self, result):
        if not isinstance(result, dict):
            return ValueError("Input must be a dictionary of form: /n \
                             {'balanceSheet': ReportMetrics(), /n \
                              'cashFlow': ReportMetrics(), /n \
                              'incomeStatement': ReportMetrics(), /n \
                              'companyOverview': CompanyOverview()}")

        valid_keys = ['ticker', 'balanceSheet', 'cashFlow', 'incomeStatement', 'companyOverview']
        for key in result.keys():
            if key.lower() not in valid_keys:
                return KeyError("Dictionary contains at least one unknown key")

    def append(self, result):
        self.isValidInput(result)
        self.tickers.append(result['ticker'])
        self.balance_sheets.append(result['balanceSheet'])
        self.cash_flows.append(result['cashFlow'])
        self.income_statements.append(result['incomeStatement'])
        self.company_overviews.append(result['companyOverview'])
