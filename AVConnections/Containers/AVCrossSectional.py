
class AVCrossSectional:
    def __init__(self, numeric_data):
        self.numeric_fields = numeric_data

    def toCSV(self):
        if self.__isCSV():
            return self

        headers = [header for header in self.numeric_fields.keys()]
        data = [self.numeric_fields[key] for key in headers]

        self.numeric_fields = [headers, data]

        return self

    def toJson(self):
        if self.__isJson():
            return self

        number_of_fields = len(self.numeric_fields[0])
        self.numeric_fields = {self.numeric_fields[0][i]: self.numeric_fields[1][i] for i in range(0, number_of_fields)}

        return self

    def __isCSV(self):
        return type(self.numeric_fields) == list

    def __isJson(self):
        return type(self.numeric_fields) == dict

    def show(self):
        return self.numeric_fields

    def __printJson(self):
        string = '{'
        for key in self.numeric_fields.keys():
            string += str(key) + ': ' + str(self.numeric_fields[key]) + ', \n'

        string += '}'

        return string

    def __printCSV(self):
        return str(self.numeric_fields[0]) + "\n" + str(self.numeric_fields[1])


    def __str__(self):
        if self.__isJson():
            return self.__printJson()

        return self.__printCSV()
