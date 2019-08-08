import requests
import json
import time
import incremental_codeur
import lcd

def StorePrintPostalCode(postalcode):
    lcd_byte(0x01, LCD_CMD)
    lcd_string("enter post code", LCD_LINE_1)
    lcd_string(postalcode, LCD_LINE_2)


def PostalCodeSelect():
    postal_code = []
    lcd_byte(0x01, LCD_CMD)
    lcd_string("enter post code", LCD_LINE_1)
    time.sleep(1)
    postal_code = [0,0,0,0,0]
    k = 0
    while(k<5):
        number = 0
        StorePrintPostalCode(postal_code)
        coder = codeur()
        while(coder != 1):
            if(coder == 2):
                if(number == "R"):
                    number = 9
                elif(number == 0):
                    number = "R"
                else:
                    number -= 1
                postal_code[k] = number
                StorePrintPostalCode(postal_code)
            if(coder == 3):
                if(number == 9):
                    number = "R"
                elif(number == "R"):
                    number = 0
                else:
                    number += 1
                postal_code[k] = number
                StorePrintPostalCode(postal_code)
            coder = codeur()
        if(number == "R" and k>0):
            k -=1
            postal_code[k] = ""
        elif(number != "R"):
            k +=1
    return("".join(postal_code))





def StoreSearch(postal_code):
    """search available store with domino'pizza store api"""
    payload = {'searchkey': postal_code}
    storelist = requests.get('https://commande.dominos.fr/eStore/fr/DominosApi/GetStores', params=payload)
    store_name_list = []
    store_ID_list = []
    for store in storelist.json():
        store = json.dumps(store)
        store = json.loads(store)
        store_name_list += [store["Name"]]
        store_ID_list += [store["Number"]]
    return(store_name_list,store_ID_list)




def StoreSelect():
    while(i == 0):
        store_name_list,store_name_ID = StoreSearch(PostalCodeSelect())
        k = len(store_name_list)
        status = 0
        if(k == 0):
            lcd_byte(0x01, LCD_CMD)
            lcd_string("No store located", LCD_LINE_1)
            lcd_string("click to escape", LCD_LINE_2)
            while(status != 1):    
                status = codeur()
        else:
            number = 0
            lcd_print(store_name_list[0])
            while(status !=1):
                if(status == 2):
                    if(number == 0):
                        number = k-1
                    else:
                        number += 1
                elif(status == 3):
                    if(number == k-1):
                        number = 0
                    else:
                        number -= 1
                lcd_print(store_name_list[number])
            i = 1
    return(store_name_ID[number])