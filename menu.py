import requests
from bs4 import BeautifulSoup
import lcd
import incremental_codeur

def Pizza_name_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-pizzas')

    bs = BeautifulSoup(menu.text, 'html.parser')
    Pizza_name_list = bs.find_all('span', {'class':'menu-entry'})
    for k in range(0,len(Pizza_name_list)):
        Pizza_name_list[k] = Pizza_name_list[k].get_text()[:-1]
    return(Pizza_name_list)


def Pizza_ID_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-pizzas')

    bs = BeautifulSoup(menu.text, 'html.parser')
    Pizza_ID_list = bs.find_all('img', {'class':'pizza-image'})
    for k in range(0,len(Pizza_ID_list)):
        Pizza_ID_list[k] = Pizza_ID_list[k]['id'][4:]

    return(Pizza_ID_list)



def Calz_name_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-entrees')

    bs = BeautifulSoup(menu.text, 'html.parser')
    calz_name_list = bs.find_all('span', {'class':'menu-entry'})
    for k in range(0,len(calz_name_list)):
        calz_name_list[k] = calz_name_list[k].get_text()[:-1]
    return(calz_name_list)


def Calz_ID_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-entrees')

    bs = BeautifulSoup(menu.text, 'html.parser')
    calz_ID_list = bs.find_all('a', {'class':'order-now'})
    for k in range(0,len(calz_ID_list)):
        calz_ID_list[k] = calz_ID_list[k]['id'][6:]
    return(calz_ID_list)



def Dessert_name_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-desserts')

    bs = BeautifulSoup(menu.text, 'html.parser')
    dessert_name_list = bs.find_all('span', {'class':'menu-entry'})
    for k in range(0,len(dessert_name_list)):
        dessert_name_list[k] = dessert_name_list[k].get_text()[:-1]

    return(dessert_name_list)


def Dessert_ID_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-desserts')

    bs = BeautifulSoup(menu.text, 'html.parser')
    dessert_ID_list = bs.find_all('a', {'class':'order-now'})
    for k in range(0,len(dessert_ID_list)):
        dessert_ID_list[k] = dessert_ID_list[k]['id'][6:]

    return(dessert_ID_list)


def Drink_name_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-boissons')

    bs = BeautifulSoup(menu.text, 'html.parser')
    drink_name_list = bs.find_all('span', {'class':'menu-entry'})
    for k in range(0,len(drink_name_list)):
        drink_name_list[k] = drink_name_list[k].get_text()[:-1]

    return(drink_name_list)


def Drink_ID_list():

    menu = requests.get('https://www.dominos.fr/la-carte/nos-boissons')

    bs = BeautifulSoup(menu.text, 'html.parser')
    drink_ID_list = bs.find_all('img', {'class':'pizza-image'})
    for k in range(0,len(drink_ID_list)):
        drink_ID_list[k] = drink_ID_list[k]['id'][4:]
    
    return(drink_ID_list)

def PrimaryMenu():
    menulist = ["Pizza","Calz","Dessert","Drink","Resume commande"]
    menustatus = 0
    lcd_byte(0x01, LCD_CMD)
    lcd_string(menulist[0], LCD_LINE_1)
    lcd_string(menulist[1], LCD_LINE_2)
    coder = 0
    menunumber = 0
    while(menustatus == 0):
        
        if(menunumber < 4):
            lcd_byte(0x01, LCD_CMD)
            lcd_string(menulist[k], LCD_LINE_1)
            lcd_string(menulist[k+1], LCD_LINE_2)
        else:
            lcd_byte(0x01, LCD_CMD)
            lcd_string(menulist[k], LCD_LINE_1)
        if(coder == 2):
            if(menunumber > 0):
                menunumber -=1
        elif(coder == 3):
            if(menunumber < 4):
                menunumber +=1
        elif(coder == 1):
            menustatus = 1
        coder = codeur()
    return(menunumber)

def ProductSelect(menunumber):
    if(menunumber == 0):
        menucontentname = Pizza_name_list()
        menucontentID = Pizza_ID_list()
    elif(menunumber == 1):
        menucontentname = Calz_name_list()
        menucontentID = Calz_ID_list()
    elif(menunumber == 2):
        menucontentname = Dessert_name_list()
        menucontentID = Dessert_ID_list()
    elif(menunumber == 3):
        menucontentname = Drink_name_list()
        menucontentID = Drink_ID_list()
    elif(menunumber == 0):
        return([0,0])
    

    menustatus = 0
    itemnumber = 0
    menulen = len(menucontentname)
    coder = 0
    while(menustatus == 0):
        if(itemnumber < menulen - 1):
            lcd_byte(0x01, LCD_CMD)
            lcd_string(menulist[k], LCD_LINE_1)
            lcd_string(menulist[k+1], LCD_LINE_2)
        else:
            lcd_byte(0x01, LCD_CMD)
            lcd_string(menulist[k], LCD_LINE_1)
        
        if(coder == 2):
            if(itemnumber > 0):
                itemnumber -=1
        elif(coder == 3):
            if(itemnumber < 4):
                itemnumber +=1
        elif(coder == 1):
            menustatus = 1
        coder = codeur()
    menustatus = 0
    menunumber = 0
    while(menustatus == 0):
        if(menunumber == 0):
            lcd_byte(0x01, LCD_CMD)
            lcd_string("confirmation", LCD_LINE_1)
            lcd_string("oui", LCD_LINE_2)
        else:
            lcd_byte(0x01, LCD_CMD)
            lcd_string("confirmation", LCD_LINE_1)
            lcd_string("non", LCD_LINE_2)
        
        if(coder == 2):
            if(menunumber == 0):
                menunumber =1
        elif(coder == 3):
            if(menunumber == 1):
                menunumber = 0
        elif(coder == 1):
            menustatus = 1
        coder = codeur()
    if(menunumber == 0):        
        return([menucontentname[menunumber],menucontentID[menunumber]])
    else:
        return([1,1])
        
        
    