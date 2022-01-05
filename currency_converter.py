
import json
import requests


url = 'https://v6.exchangerate-api.com/v6/c8659d6570fb1fa0887c064a/latest/USD'
url_response = requests.get(url)
currency_dict = url_response.json()
currency_list = currency_dict.get("conversion_rates")


def choose_currencies():
    
    print("List of available currencies: \n", list(currency_list))

    from_currency = input("What currency do you have: ").upper()
    to_currency = input("What currency do you want: ").upper()
    money_amount = input(f"How much {from_currency} do you want to exchange: ")

    edited_url = f"https://v6.exchangerate-api.com/v6/c8659d6570fb1fa0887c064a/pair/{from_currency}/{to_currency}/{money_amount}"

    response = requests.get(edited_url)
    dictionary = response.json()

    print(f"Your {money_amount} {from_currency} converts to ",dictionary['conversion_result'],to_currency)


def choose_currencies_test(from_amount = "",to_amount = "", given_amount = 1):

    edited_url = f"https://v6.exchangerate-api.com/v6/c8659d6570fb1fa0887c064a/pair/{from_amount}/{to_amount}/{given_amount}"

    response = requests.get(edited_url)
    dictionary = response.json()

    print(f"Your {given_amount} {from_amount} converts to ",
          dictionary['conversion_result'], to_amount)


    




