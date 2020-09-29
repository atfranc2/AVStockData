
class Utils:

    def isNaN(self, value):
        try:
            float(value)
            return False
        except:
            return True

    def stringToNumeric(self, value):
        numeric_value = float('nan') if self.isNaN(value) else float(value)

        return numeric_value

    def isCSV(self, item):
        return type(item) == list

    def isJson(self, item):
        return type(item) == dict
