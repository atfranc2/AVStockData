import requests
import csv

class Utils():

    def callHasError(self, response, is_json_response = True):
        if is_json_response:
            return True if response.get('Error Message', False) else False

        return True

    def callLimitExceeded(self, response, is_json_response = True):
        if is_json_response:
            return True if response.get('Note', False) else False

        return True

    def decodeCSVResponse(self, response):
        decoded_content = response.content.decode('utf-8')
        decoded_content = csv.reader(decoded_content.splitlines(), delimiter=',')

        return list(decoded_content)

    def decodeJSONReponse(self, response):
        return response.json()
