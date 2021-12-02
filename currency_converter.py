import tkinter as tk
from tkinter import *
import json
import requests


url = 'https://v6.exchangerate-api.com/v6/c8659d6570fb1fa0887c064a/latest/USD'
api = "c8659d6570fb1fa0887c064a"

default_pair = 'https://v6.exchangerate-api.com/v6/c8659d6570fb1fa0887c064a/pair/EUR/GBP/1'

response = requests.get(default_pair)
data = response.json()

diction = {'Hello': 60}
string_returned = json.dumps(data)
print(string_returned)

dtest = json.loads(string_returned)
print(type(string_returned))

def currency_conversion():
    return



root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x500")
root.resizable(0,0)
root.configure(bg = "White")


heading = Label(root, text = "Realtime Currency Converter", font = ("Comic    Sans MS", 18)).place(x=100)





root.update()
root.mainloop()