import random

temp_short = {"f": "fahrenheit", "c": "celsius", "k": "kelvin"}
temp_long = {"fahrenheit": "f", "celsius": "c", "kelvin": "k"}


def celsius_to_kelvin(celsius):
    return celsius + 273


def kelvin_to_celsius(kelvin):
    return kelvin - 273


def celsius_to_fahrenheit(celsius):
    return 1.8 * celsius + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))


def detect_unit(unit):
    if not (unit in temp_short or unit in temp_long):
        print("Invalid Temperature Unit")
        unit = input("Enter a proper unit.....").lower()
        detect_unit(unit)
    else:
        return unit


def validate_value(value, count):
    if not value.isdigit():
        if -1 < count < 2:
            validate_value(input("Invalid input... -> input:"), count + 1)

        elif count >= 2:
            validate_value(input(value_insults[random.randint(0, len(value_insults) - 1)]), count + 1)

    else:
        return int(value)


def temp_lobby(value_in="neg", unit_in="neg", unit_out="neg"):
    if value_in == unit_in == unit_out == "neg":
        value_in = input("Enter the value of the temperature: ")
        unit_in = (input("Enter the unit you are converting from: [f]fahrenheit [c]celsius [k]kelvin ").lower()
                   .replace(" ", ""))
        unit_out = (input("Enter the unit you are converting to: [f]fahrenheit [c]celsius [k]kelvin ").lower()
                    .replace(" ", ""))

    validated_value_in = validate_value(value_in, 0)
    detected_unit_in = detect_unit(unit_in.lower())
    detected_unit_out = detect_unit(unit_out.lower())

    if "f" == detected_unit_in and "c" == detected_unit_out:
        return fahrenheit_to_celsius(validated_value_in), detected_unit_out

    if "f" == detected_unit_in and "k" == detected_unit_out:
        return fahrenheit_to_kelvin(validated_value_in), detected_unit_out

    if "c" == detected_unit_in and "k" == detected_unit_out:
        return celsius_to_kelvin(validated_value_in), detected_unit_out

    if "c" == detected_unit_in and "f" == detected_unit_out:
        return celsius_to_fahrenheit(validated_value_in), detected_unit_out

    if "k" == detected_unit_in and "c" == detected_unit_out:
        return kelvin_to_celsius(validated_value_in), detected_unit_out

    if "k" == detected_unit_in and "f" == detected_unit_out:
        return kelvin_to_fahrenheit(validated_value_in), detected_unit_out

    return value_in, detected_unit_out


fd = open("C:/Users/Andi/PycharmProjects/Hermes_Suite2/Hermes_Converter_Suite/bag_of_value_insults.txt", "r")
value_insults = fd.readlines()
fd.close()

for i in range(len(value_insults)):
    value_insults[i] = value_insults[i][:-1]
