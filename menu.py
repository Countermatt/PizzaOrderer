import requests
from bs4 import BeautifulSoup

menu = requests.get('https://www.dominos.fr/la-carte')

bs = BeautifulSoup(menu.text, 'html.parser')
Pizza_name_list = bs.find_all(class_='menu-entry')
Pizza_ID_list = bs.find_all(class_='pizza-image')

k = len(Pizza_name_list)
i = 0
while(i<k):
    print(Pizza_name_list[i].get_text(),'--',Pizza_ID_list[i]['id'][4:])
    i+=1