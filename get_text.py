#Used for Webscraping
import requests
import bs4
import lxml

class GetText():
    def __init__(self):
        url = self.get_url()
        self.get_url_text(url)

    def get_url(self):
        url = input("Enter url:")
        return url

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

        print(content_string)