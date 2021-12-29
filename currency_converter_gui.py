import PySimpleGUI as sg
import currency_converter


sg.theme('Light Purple')
layout = [
     [sg.Text("Currency Converter")],
     [sg.Text("What currency do you have")],
     [sg.Listbox(list(currency_converter.currency_list), size=(20, 4),
                 enable_events=False, key='_LIST_')],
     [sg.Button("Exit")]
 ]

#create the window
window = sg.Window("Demo", layout)

#create an event loop
while True:
    event, values = window.read()
    #end program if user closes window or pressed ok button

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close() 