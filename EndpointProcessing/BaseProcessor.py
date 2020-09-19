from abc import ABC, abstractmethod

class BaseProcessor(ABC):
    def __init__(self, api_key):
        self.api_key = api_key
        self.currentResult = None
        self.compiledData = None

    @abstractmethod
    def toDict(self):
        pass

    @abstractmethod
    def toList(self):
        pass

    def currentResultIsDict(self):
        if type(self.currentResult) == dict:
            return True

        return False

    def currentResultIsList(self):
        if type(self.currentResult) == list:
            return True

        return False

    def currentResultIsNone(self):
        return type(self.currentResult) == None
