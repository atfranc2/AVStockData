


class FundementalData:
    def __init__(self):
        self.tickers = []
        self.balance_sheets = []
        self.cash_flows = []
        self.income_statements = []
        self.company_overviews = []
        self.fundemental_data = {}
        self.period = None

    def __isDict(self, item):
        return isinstance(item, dict)

    def __resultIsDict(self, result):
        if not self.__isDict(result):
            return ValueError("Input must be a dictionary of form: /n \
                             {'balanceSheet': ReportMetrics(), /n \
                              'cashFlow': ReportMetrics(), /n \
                              'incomeStatement': ReportMetrics(), /n \
                              'companyOverview': CompanyOverview()}")

    def __keysAreValid(self, result):
        valid_keys = ['ticker', 'balanceSheet', 'cashFlow', 'incomeStatement', 'companyOverview', 'sector', 'industry', 'price', 'date']
        for key in result.keys():
            if key.lower() not in valid_keys:
                return KeyError("Dictionary contains at least one unknown key")

    def __isValidInput(self, result):
        self.__resultIsDict(result)
        self.__keysAreValid(result)

    def append(self, result):
        self.__isValidInput(result)
        self.period = result['period']
        self.tickers.append(result['ticker'])
        self.fundemental_data[result['ticker'].upper()] = {
            'period': result['period'],
            'date': result['date'],
            'price': result['price'],
            'sector': result['sector'],
            'industry': result['industry'],
            'balanceSheet': result['balanceSheet'],
            'cashFlow': result['cashFlow'],
            'incomeStatement': result['incomeStatement'],
            'companyOverview': result['companyOverview']
        }

    def add(self, fundemental_data):
        tickers = list(fundemental_data.keys())
        for ticker in tickers:
            self.tickers.append(ticker)
            result = fundemental_data[ticker]
            self.fundemental_data[ticker.upper()] = {
            'period': result['period'],
            'date': result['date'],
            'price': result['price'],
            'sector': result['sector'],
            'industry': result['industry'],
            'balanceSheet': result['balanceSheet'],
            'cashFlow': result['cashFlow'],
            'incomeStatement': result['incomeStatement'],
            'companyOverview': result['companyOverview']
        }


    def __getitem__(self, ticker):
        return self.fundemental_data.get(ticker.upper(), 0)
