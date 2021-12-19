import tkinter as tk
from tkinter import *
import json
import requests


url = 'https://v6.exchangerate-api.com/v6/c8659d6570fb1fa0887c064a/latest/USD'
api = "c8659d6570fb1fa0887c064a"
default_pair = 'https://v6.exchangerate-api.com/v6/c8659d6570fb1fa0887c064a/pair/EUR/GBP/1'


response = requests.get(url)
currency_dict = response.json()

returned_string = json.dumps(currency_dict)

dtest = json.loads(returned_string)
values = currency_dict.get("conversion_rates")

currency_list = values.keys()

def currency_conversion(site):
    data = requests.get(site)
    currency_dictionary = data.json()

    from_currency = currency_dictionary.get("base_code")
    to_currency = currency_dictionary.get("target_code")
    amount = currency_dictionary.get("conversion_result")


    print("This is the base currency: " ,from_currency)
    print("This is the target currency: ", to_currency)
    print("This is the amount: " ,amount)


currency_conversion(default_pair)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x500')
        self.resizable(0,0)
        self.configure(bg = "White")
        self.title("Currency Converter")
 


        self.label = Label(self, text = "This is a test")
        self.label.grid(columnspan = 2, sticky = W)
        
        self.button = Button(self, text = "Test")
        self.button.grid(columnspan = 2, sticky = W)
        

if __name__ == "__main__":
        app = App()
        app.mainloop()
