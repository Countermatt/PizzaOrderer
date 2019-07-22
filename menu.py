import requests
from bs4 import BeautifulSoup


def Pizza_name_search():

    menu = requests.get('https://www.dominos.fr/la-carte')

    bs = BeautifulSoup(menu.text, 'html.parser')
    Pizza_name_list = bs.find_all(class_='menu-entry')

    return(Pizza_name_list)


def Pizza_ID_search():

    menu = requests.get('https://www.dominos.fr/la-carte')

    bs = BeautifulSoup(menu.text, 'html.parser')
    Pizza_ID_list = bs.find_all(class_='pizza-image')

    return(Pizza_ID_list)