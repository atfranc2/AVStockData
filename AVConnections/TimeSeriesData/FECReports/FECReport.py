from AVStockData.AVConnections.AVConnection import AVConnection
from AVStockData.AVConnections.Containers.ReportMetrics import ReportMetrics
from AVStockData.CallMeter import CallMeter

class FECReport(AVConnection):
    def __init__(self, api_key, callMeter = CallMeter(call_limit_per_minute = 5, call_limit_per_day = 500)):
        super().__init__(callMeter)
        self.__api_key = api_key
        self.symbol = None
        self.quarterly_reports = None
        self.annual_reports = None

    def __isNaN(self, number):
        try:
            float(number)
            return False
        except:
            return True

    def __stringToNumeric(self, value):
        numeric_value = float('nan') if self.__isNaN(value) else float(value)

        return numeric_value

    def __getExcludedFields(self):
        return ["fiscalDateEnding", "reportedCurrency"]

    def __unpackJsonListResponse(self, json_list):
        report_json = {}
        for json_item in json_list:
            key = json_item["fiscalDateEnding"]
            report_json[key] = {key: self.__stringToNumeric(json_item[key]) for key in json_item.keys() if key not in self.__getExcludedFields()}

        return report_json

    def __getAnnualReports(self, json_response):
        annual_reports = json_response["annualReports"]

        return self.__unpackJsonListResponse(annual_reports)

    def __getQuarterlyReports(self, json_response):
        quarterly_reports = json_response["quarterlyReports"]

        return self.__unpackJsonListResponse(quarterly_reports)

    def parse(self, json_response):
        self.symbol = json_response['symbol']
        self.currency = json_response["annualReports"][0]["reportedCurrency"]
        self.quarterly_reports = ReportMetrics(self.__getQuarterlyReports(json_response))
        self.annual_reports = ReportMetrics(self.__getAnnualReports(json_response))

    @property
    def api_key(self):
        return self.__api_key

    @api_key.setter
    def api_key(self, api_key):
        self.__api_key = api_key
