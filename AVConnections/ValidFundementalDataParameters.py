class ValidFundementalDataParameters:
    def __init__(self):
        self.__valid_listing_statuses = ['active', 'delisted']

    def isValidListingStatus(self, status):
        return status in self.__valid_listing_statuses
