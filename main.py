import time
import menu
import store
import lcd
import incremental_codeur


def setup():
        BUTTON = 16
        codersetup()
        lcd_set_up()
        GPIO.setup(BUTTON, GPIO.IN)

def lcd_print(text):
    if(len(text)<=16):
        lcd_byte(0x01, LCD_CMD)
        lcd_string(text, LCD_LINE_1)
    else:
        lcd_byte(0x01, LCD_CMD)
        lcd_string(text[:16], LCD_LINE_1)
        lcd_string(text[16:32], LCD_LINE_2)

def main():

    lcd_set_up()

    while True:
            
        storeID = StoreSelect()
        commande = []
        
        while(commande[-1][0] != 0):
                commande +=ProductSelect(PrimaryMenu())
        commandefinal = []
        
        for item in commande:
                if(item[0] != 1 or item[0] != 0):
                        commandefinal += item
        confirmation = CommandeConfirm(command)
        
        if(not(confirmation)):
                continue

