from AVStockData.AVConnections.Containers.ReportMetrics import ReportMetrics
from AVStockData.AVConnections.Containers.AVCrossSectional import AVCrossSectional
import json

class FundementalDataIO:
    def __init__(self):
        self.imported_json = None

    def getTickers(self, fundemental_data):
        keys = fundemental_data.keys()
        return list(keys)

    def parseExport(self, fundemental_data):
        tickers = self.getTickers(fundemental_data)
        json_to_export = {}
        for ticker in tickers:
            period = fundemental_data[ticker]['period']
            date = fundemental_data[ticker]['date']
            price = fundemental_data[ticker]['price']
            sector = fundemental_data[ticker]['sector']
            industry = fundemental_data[ticker]['industry']
            balance_sheet = fundemental_data[ticker]['balanceSheet']
            cash_flow = fundemental_data[ticker]['cashFlow']
            income_statement = fundemental_data[ticker]['incomeStatement']
            company_overview = fundemental_data[ticker]['companyOverview']
            json_to_export[ticker] = {
                'period': period,
                'date': date,
                'price': price,
                'sector': sector,
                'industry': industry,
                'balanceSheet': self.convertDatesToString(balance_sheet.time_series),
                'cashFlow': self.convertDatesToString(cash_flow.time_series),
                'incomeStatement': self.convertDatesToString(income_statement.time_series),
                'companyOverview': company_overview.numeric_fields
            }

        return json_to_export

    def parseImport(self, fundemental_data):
        tickers = self.getTickers(fundemental_data)
        json_to_import = {}
        for ticker in tickers:
            period = fundemental_data[ticker]['period']
            date = fundemental_data[ticker]['date']
            price = fundemental_data[ticker]['price']
            sector = fundemental_data[ticker]['sector']
            industry = fundemental_data[ticker]['industry']
            balance_sheet = fundemental_data[ticker]['balanceSheet']
            cash_flow = fundemental_data[ticker]['cashFlow']
            income_statement = fundemental_data[ticker]['incomeStatement']
            company_overview = fundemental_data[ticker]['companyOverview']
            json_to_import[ticker] = {
                'period': period,
                'date': date,
                'price': price,
                'sector': sector,
                'industry': industry,
                'balanceSheet': ReportMetrics(balance_sheet),
                'cashFlow': ReportMetrics(cash_flow),
                'incomeStatement': ReportMetrics(income_statement),
                'companyOverview': AVCrossSectional(company_overview)
            }

        return json_to_import

    def convertDatesToString(self, report):
        dates = list(report.keys())
        new_json = {}
        for date in dates:
            str_date = date.strftime("%Y-%m-%d")
            new_json[str_date] = report[date]

        return new_json

    def convertStringToDates(self, report):
        str_dates = list(report.keys())
        new_json = {}
        for str_date in str_dates:
            date = datetime.strptime(str_date, "%m/%d/%Y")
            new_json[date] = report[str_date]

        return new_json

    def importData(self, path):
        imported_json = {}
        with open(path) as json_file:
            imported_json = json.load(json_file)
        json_file.close()
        self.imported_json = self.parseImport(imported_json)

        return self


    def exportData(self, fundemental_data, path, file_name = None):
        json_to_export = self.parseExport(fundemental_data)
        keys = self.getTickers(fundemental_data)
        period = json_to_export[keys[0]]['period']

        file_name = file_name if file_name != None else "fundemental_data" + f"_{period}_" + "_".join(keys)
        full_path = path + "\\" + file_name + ".txt"

        with open(full_path, 'w') as output_file:
            json.dump(json_to_export, output_file)
        output_file.close()

    def show(self):
        return self.imported_json
