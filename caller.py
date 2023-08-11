import time
from tqdm import tqdm
import temperature_converter
import distance_converter
import currency_converter
import random


def lobby(hermes_quotes):
    select_hermes_quote(hermes_quotes)

    menu_option = int(input("select a menu: [1]Temperature [2]Distance [3]Currency\n"))

    match menu_option:
        case 1:
            temp, unit = temperature_converter.temp_lobby()
            print(f"Your temperature in {unit} is {temp}")
        case 2:
            dist, unit = distance_converter.distance_lobby()
            print(f"Your equivalent distance in {unit} is {dist} ")
        case 3:
            cur, unit = currency_converter.currency_lobby()
            print(f"You have {cur} in {unit}")

    print(" ")
    return lobby(hermes_quotes)


def load_hermes_file():
    hermes_file = open("C:/Users/Andi/PycharmProjects/Hermes_Suite2/Hermes_Converter_Suite/hermes_quotes.txt", "r")

    hermes_quotes = hermes_file.readlines()
    # print("hermes_quotes: 0%", end="=====")
    for i in tqdm(range(len(hermes_quotes)), colour="WHITE"):
        time.sleep(0.1)
        # if i == len(hermes_quotes) - 1:
        #     print(str(int((i + 1) / len(hermes_quotes) * 100)) + "%")
        # else:
        #     print(str(int((i + 1)/len(hermes_quotes) * 100)) + "%", end="=====")
        hermes_quotes[i] = hermes_quotes[i][:-1]

    hermes_file.close()

    return hermes_quotes


def select_hermes_quote(hermes_quotes):
    print(" ")
    print(hermes_quotes[random.randint(0, len(hermes_quotes)) - 1])
    return


def start():
    lobby(load_hermes_file())


start()
