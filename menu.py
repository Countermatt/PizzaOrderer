import requests

#payload = {'searchkey': '33600'}

#storelist = requests.get('https://commande.dominos.fr/eStore/fr/DominosApi/GetStores', params=payload)
#print(storelist.json())

payload = {'pageCode': 'ProductMenu', 'menuCode': 'Menu.Pizza'}
menu = requests.get('https://commande.dominos.fr/eStore/fr/OffersAjax/GetOffersclear', params=payload)
print(menu.text)