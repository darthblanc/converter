import pandas as pd


def create_dictionary_for_data():
    major_table = pd.read_html("https://www.xe.com/currencytables/?from=USD")
    naira_dollar_table = pd.read_html("https://www.xe.com/currencyconverter/convert/?Amount=1&From=NGN&To=USD")
    naira = naira_dollar_table[1].iloc[0][1].split(" ")
    dollar = naira_dollar_table[1].iloc[0][0].split(" ")
    currency_dict = {naira[1]: {dollar[1]: 1 / float(naira[0])}, dollar[1]: {naira[1]: float(naira[0])}}
    major_exchange_table = major_table[1]
    major_exchanges = major_exchange_table.iloc[0:]
    # print(major_exchange_table)

    for i in range(8):
        currencies = major_exchanges["Currency"][i].split(" / ")
        if currency_dict.__contains__(currencies[0]):
            currency_dict[currencies[0]].update({currencies[1]: major_exchanges["Rate"][i]})
        else:
            currency_dict[currencies[0]] = {currencies[1]: major_exchanges["Rate"][i]}

        if currency_dict.__contains__(currencies[1]):
            currency_dict[currencies[1]].update({currencies[0]: 1 / major_exchanges["Rate"][i]})
        else:
            currency_dict[currencies[1]] = {currencies[0]: 1 / major_exchanges["Rate"][i]}

    return currency_dict


def convert_currency(value_in="neg", unit_in="neg", unit_out="neg"):
    currency_dict = create_dictionary_for_data()
    prompt_piece = ""
    for k in currency_dict:
        prompt_piece += (k + "| ")
    prompt_piece = prompt_piece[:-2]

    if value_in == unit_out == unit_in == "neg":
        value_in = int(input("Enter a value of the currency :"))
        unit_in = input(f"Convert from: {prompt_piece}: ")
        unit_out = input(f"Convert to: {prompt_piece}: ")

    if unit_in == unit_out:
        return value_in, unit_out

    if (unit_in == "NGN" and unit_out == "USD") or (unit_in == "USD" and unit_out == "NGN"):
        return round(value_in * currency_dict[unit_in][unit_out], 2), unit_out

    elif unit_in == "NGN":
        return round(value_in * currency_dict[unit_in]["USD"] * currency_dict["USD"][unit_out], 2), unit_out

    elif unit_out == "NGN":
        return round(value_in * currency_dict[unit_in]["USD"] * currency_dict["USD"]["NGN"], 2), unit_out

    return round(value_in * currency_dict[unit_in][unit_out], 2), unit_out


def currency_lobby():
    return convert_currency()
