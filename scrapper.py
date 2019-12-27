import requests
from bs4 import BeautifulSoup


def find_cord(town, link='https://pl.wikipedia.org/wiki/'):
    try:
        data = requests.get(link + town)
        soup = BeautifulSoup(data.text, "html.parser")

        width = soup.find('span', {'class': 'latitude'}).extract().text
        lenght = soup.find('span', {'class': 'longitude'}).extract().text
        return width, lenght

    except AttributeError:
        print('nieprawidlowa nazwa miasta')
