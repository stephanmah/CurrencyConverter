import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Multiline
import currency_converter


sg.theme('Light Purple')
layout = [
    [sg.Text("Currency Converter")],
    [sg.Text("What currency do you have"), sg.Text("What currency do you want"),
     sg.Text("How much of your currency do you want to exchange: ")],
    [sg.Listbox(values = (list(currency_converter.currency_list)), size=(20, 4),
    enable_events=True, key='_FROMLIST_'),
     sg.Listbox(values=(list(currency_converter.currency_list)), size=(20, 4), enable_events=True, key='_TOLIST_'), sg.InputText(key='_INPUTAMOUNT_', size=(20, 1), enable_events=True), ],
     [sg.Text("You will recieve x currency"),Multiline(size = (15,1), key = "_OUTPUTAMOUNT_") ],
     
    [sg.Submit()],
    [sg.Button("Exit")]
 ]

#create the window
window = sg.Window("Currency Converter", layout, size = (700,500))

#create an event loop
while True:
    event, values = window.read()
    #end program if user closes window or pressed ok button

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if event == "_FROMLIST_":
        currency_converter.from_currency = (f'get = {window["_FROMLIST_"].get()}')
        print(currency_converter.from_currency)


    if event == "_TOLIST_":
        currency_converter.to_currency = (f'get = {window["_TOLIST_"].get()}')
        print(currency_converter.to_currency)

    if event == "_OUTPUTAMOUNT_":
        currency_converter.given_amount = (f'get = {window["_TOLIST_"].get()}')
        print(currency_converter.given_amount)



window.close() 