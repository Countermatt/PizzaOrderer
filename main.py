import time
import menu
import store
import lcd
import incremental_codeur

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


