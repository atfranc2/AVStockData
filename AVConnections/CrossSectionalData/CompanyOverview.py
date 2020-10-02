from AVStockData.AVConnections.AVConnection import AVConnection
from AVStockData.AVConnections.Containers.AVCrossSectional import AVCrossSectional
from AVStockData.CallMeter import CallMeter

class CompanyOverview(AVConnection):
    def __init__(self, api_key, callMeter = CallMeter(call_limit_per_minute = 5, call_limit_per_day = 500)):
        super().__init__(callMeter)
        self.symbol = None
        self.asset_type = None
        self.name = None
        self.description = None
        self.descriptive_data = None
        self.datetime_data = None
        self.numeric_data = None

    def getCompanyOverview(self, ticker):
        params = {'function':'OVERVIEW','symbol':ticker,'apikey':self.api_key}
        response = self.getResponse(params)
        json_response = self.decodeJSONReponse(response)
        self.parse(json_response)

        return self

    def parse(self, json_response):
        self.symbol = json_response['Symbol']
        self.asset_type = json_response['AssetType']
        self.name = json_response['Name']
        self.description = json_response['Description']

        self.descriptive_data = self.getStockInformationFields(json_response)
        self.datetime_data = self.getDatetimeFields(json_response)
        self.numeric_data = AVCrossSectional(self.getNumericFields(json_response))

    def unpackJsonResponse(self, json_response, json_fields):
        return {key:json_response[key] for key in json_response if key in json_fields}

    def companyInformationFields(self, json_response):
        fields = ['Symbol', 'AssetType', 'Name', 'Description', 'FiscalYearEnd']

        return self.unpackJsonResponse(json_response, fields)

    def getStockInformationFields(self, json_response):
        fields = ['Exchange','Currency','Country','Sector','Industry','Address']

        return self.unpackJsonResponse(json_response, fields)

    def getDatetimeFields(self, json_response):
        fields = ['LatestQuarter', 'DividendDate','ExDividendDate','LastSplitDate']

        return self.unpackJsonResponse(json_response, fields)

    def splitFactorToNumeric(self, string_split_factor):
        split_factor_parts = [float(numeral) for numeral in string_split_factor.split(":")]

        return split_factor_parts[0] / split_factor_parts[1]

    def covertStringsToNumeric(self, numeric_strings_json):
        excluded_fields = []
        for key in numeric_strings_json.keys():
            value = numeric_strings_json[key]
            numeric_strings_json[key] = float(numeric_strings_json[key]) if key != 'LastSplitFactor' else self.splitFactorToNumeric(value)

        return numeric_strings_json

    def getNumericFields(self, json_response):
        fields = ['MarketCapitalization','EBITDA','PERatio','PEGRatio','BookValue','DividendPerShare','DividendYield','EPS',
                  'RevenuePerShareTTM','ProfitMargin','OperatingMarginTTM','ReturnOnAssetsTTM','ReturnOnEquityTTM','RevenueTTM',
                  'GrossProfitTTM','DilutedEPSTTM','QuarterlyEarningsGrowthYOY','QuarterlyRevenueGrowthYOY','AnalystTargetPrice',
                  'TrailingPE','ForwardPE','PriceToSalesRatioTTM','PriceToBookRatio','EVToRevenue','EVToEBITDA','Beta','52WeekHigh',
                  '52WeekLow','50DayMovingAverage','200DayMovingAverage','SharesOutstanding','SharesFloat','SharesShort',
                  'SharesShortPriorMonth','ShortRatio','ShortPercentOutstanding','ShortPercentFloat','PercentInsiders',
                  'PercentInstitutions','ForwardAnnualDividendRate','ForwardAnnualDividendYield','PayoutRatio','LastSplitFactor']

        unpacked_response = self.unpackJsonResponse(json_response, fields)

        return self.covertStringsToNumeric(unpacked_response)

    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self, api_key):
        self.__api_key = api_key
