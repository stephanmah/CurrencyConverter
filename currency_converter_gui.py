import PySimpleGUI as sg
import currency_converter


sg.theme('Light Purple')
layout = [
    [sg.Text("Currency Converter")],
    [sg.Text("What currency do you have"), sg.Text("What currency do you want"),
     sg.Text("How much of your currency do you want to exchange: ")],
    [sg.Listbox(list(currency_converter.currency_list), size=(20, 4),
    enable_events=False, key='_FROMLIST_'),
     sg.Listbox(list(currency_converter.currency_list), size=(20, 4), enable_events=False, key='_TOLIST_'), sg.Multiline(size=(20, 4), key='textbox')],
     [sg.Text("You will recieve x currency")],
    [sg.Multiline(size=(20, 4), key='textbox')],
     
    [sg.Button("Convert"),sg.Button("Reset")],
    [sg.Button("Exit")]
 ]

#create the window
window = sg.Window("Demo", layout, size = (700,500))

#create an event loop
while True:
    event, values = window.read()
    #end program if user closes window or pressed ok button

    if event == "Exit" or event == sg.WIN_CLOSED:
        break


window.close() 