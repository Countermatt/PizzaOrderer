import requests
import json

def Store_Search(postal_code):
    """search available store with domino'pizza store api"""
    payload = {'searchkey': postal_code}
    storelist = requests.get('https://commande.dominos.fr/eStore/fr/DominosApi/GetStores', params=payload)
    store_list = []
    for store in storelist.json():
        store = json.dumps(store)
        store = json.loads(store)
        store_list += [store["Name"],store["Number"]]

    return(store_list)
