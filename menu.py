import requests
from bs4 import BeautifulSoup


def Pizza_name_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-pizzas')

    bs = BeautifulSoup(menu.text, 'html.parser')
    Pizza_name_list = bs.find_all(class_='menu-entry')

    return(Pizza_name_list)


def Pizza_ID_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-pizzas')

    bs = BeautifulSoup(menu.text, 'html.parser')
    Pizza_ID_list = bs.find_all(class_='pizza-image')
    for k in range(0,len(Pizza_ID_list)):
        Pizza_ID_list[k] = Pizza_ID_list[k][4:]
    
    return(Pizza_ID_list)



def Calz_name_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-entrees')

    bs = BeautifulSoup(menu.text, 'html.parser')
    calz_name_list = bs.find_all(class_='menu-entry')

    return(calz_name_list)


def Calz_ID_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-entrees')

    bs = BeautifulSoup(menu.text, 'html.parser')
    Calz_ID_list = bs.find_all(class_='order-now')
    for k in range(0,len(Calz_ID_list)):
        Calz_ID_list[k] = Calz_ID_list[k][6:]

    return(Calz_ID_list)



def Dessert_name_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-desserts')

    bs = BeautifulSoup(menu.text, 'html.parser')
    dessert_name_list = bs.find_all(class_='menu-entry')

    return(dessert_name_list)


def Dessert_ID_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-desserts')

    bs = BeautifulSoup(menu.text, 'html.parser')
    dessert_ID_list = bs.find_all(class_='order-now')
    for k in range(0,len(Calz_ID_list)):
        dessert_ID_list[k] = dessert_ID_list[k][6:]

    return(dessert_ID_list)


def Drink_name_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-boissons')

    bs = BeautifulSoup(menu.text, 'html.parser')
    drink_name_list = bs.find_all(class_='menu-entry')

    return(drink_name_list)


def Drink_ID_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-boissons')

    bs = BeautifulSoup(menu.text, 'html.parser')
    drink_ID_list = bs.find_all(class_='pizza-image')
    for k in range(0,len(drink_ID_list)):
        drink_ID_list[k] = drink_ID_list[k][4:]
    
    return(drink_ID_list)

