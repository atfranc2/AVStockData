from AVStockData.EndpointProcessing.FundementalDataProcessing.CompanyOverviewProcesser import CompanyOverviewProcessor

var = CompanyOverviewProcessor("DBRSXJ1PRMHXHO4M")

print(var.getData("PG").toList().show())
