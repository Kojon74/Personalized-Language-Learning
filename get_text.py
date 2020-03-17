import requests
import bs4
import lxml
import csv

class GetText():
    def __init__(self):
        url = self.get_url()
        text = self.get_url_text(url)
        self.sort_content(text)
    def get_url(self):
        url = input("Enter url:")
        return "https://www.bbc.co.uk/news/uk-51700604"
    def get_url_text(self, url):
        #Reponse object from the GET

        response = requests.get(url)

        #Checks status
        if response:
            print('Success')
        else:
            print('Failed to access')

        #Gets the html file
        x_html = bs4.BeautifulSoup(response.text, 'lxml')
        content = x_html.select('p')

        content_string = ""

        for x in content:
            content_string += x.getText()
        words = content_string.split()
        return words
    def sort_content(self, words):
        unique_set = set(words)
        unique_words = (list(unique_set))
        extract = open('ngsl.csv')
        ngsl_list = csv.reader(extract)
        for text in ngsl_list:
            print(text)
        # print(unique_words)

extractText = GetText()