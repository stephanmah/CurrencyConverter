import PySimpleGUI as sg
import currency_converter


sg.theme('Light Purple')
layout = [
    [sg.Text("Currency Converter")],
    [sg.Text("What currency do you have"), sg.Text("What currency do you want"),
     sg.Text("How much of your currency do you want to exchange: ")],
    [sg.Listbox(values = (list(currency_converter.currency_list)), size=(20, 4),
    enable_events=False, key='_FROMLIST_'),
     sg.Listbox(values = (list(currency_converter.currency_list)), size=(20, 4), enable_events=False, key='_TOLIST_'), sg.InputText(key='_INPUTAMOUNT_',size = (20,1))],
     [sg.Text("You will recieve x currency")],
     
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


window.close() 