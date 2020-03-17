import csv
import requests

class CheckVocab():
    def __init__(self):
        check = self.check_ngsl()
    def check_ngsl(self):
        extract = open('ngsl.csv')
        extracted = csv.reader(extract)
        ngsl_list = []
        for text in extracted:
            if ((text[0] == '') & (text[1] == '')):
                break
            print('"' + text[0] + '": ' + '"' + text[1] + '",\n')
            ngsl_list.append([text[0], text[1]]) #[Word, Frequency]        
        return True

x = CheckVocab()