
import json
import requests


url = 'https://v6.exchangerate-api.com/v6/c8659d6570fb1fa0887c064a/latest/USD'
api = "c8659d6570fb1fa0887c064a"
default_pair = 'https://v6.exchangerate-api.com/v6/c8659d6570fb1fa0887c064a/pair/EUR/GBP/1'


response = requests.get(url)
currency_dict = response.json()

print(currency_dict)

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

    print("This is the base currency: ", from_currency)
    print("This is the target currency: ", to_currency)
    print("This is the amount: ", amount)


currency_conversion(default_pair)
