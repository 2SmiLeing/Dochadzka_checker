import time
from employees import *

width = 140
def print_with_delay(text, delay=0.02):
        for char in text:
            time.sleep(delay)
            print(char, end='', flush=True)

def start():
    welcome = ("*" * 25 + "  Vitajte v aplikaci Dochadzka  " + "*" * 25)
    centered_welcome = welcome.center(width)
    welcome_text = ("*" * 25 + "  Aplikacia Vam umozni zistit dochadzku zamestnancov v danom roku a mesiaci  " + "*" * 25)
    centered_welcome_text = welcome_text.center(width)
                    

    print_with_delay(centered_welcome)
    print("\n")
    print_with_delay(centered_welcome_text)
    print("\n")
    
start()
new_employee()

from workersData import *
databaze()
combine_data()
from hours_checker import *





