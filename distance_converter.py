systemic_distance_graph = {"foot": {"inch": 12, "yard": (1 / 3), "mile": (1 / 5280)},
                           "inch": {"yard": 4, "mile": (12 / 5280), "foot": (1 / 12)},
                           "yard": {"mile": (1 / 1760), "foot": 3, "inch": 36},
                           "mile": {"yard": 1760, "foot": 5280, "inch": (12 * 5280)}}

metric_distance_graph = {"m": {"cm": 100, "mm": 1000, "km": 1 / 1000},
                         "km": {"cm": 10 ** 4, "mm": 10 ** 5, "m": 1000},
                         "cm": {"m": 1 / 100, "km": 1 / (10 ** 4), "mm": 10},
                         "mm": {"cm": 1 / 10, "km": 1 / (10 ** 5), "m": 1 / 1000}}

metric_systemic_distance_graph = {"km": {"mile": 0.62}, "mile": {"km": 1.609344}}


def convert_within_systemic(value_in="neg", unit_in="neg", unit_out="neg"):
    if value_in == unit_out == unit_in == "neg":
        value_in = int(input("Enter the value of the distance: "))
        unit_in = input("Convert from: foot | inch | yard | mile ")
        unit_out = input("Convert to: foot | inch | yard | mile ")

    if unit_in == unit_out:
        return value_in, unit_out

    return value_in * systemic_distance_graph[unit_in][unit_out], unit_out


def convert_within_metric(value_in="neg", unit_in="neg", unit_out="neg"):
    if value_in == unit_out == unit_in == "neg":
        value_in = int(input("Enter the value of the distance: "))
        unit_in = input("Convert from: km | m | cm | mm ")
        unit_out = input("Convert to: km | m | cm | mm ")

    if unit_in == unit_out:
        return value_in, unit_out

    return value_in * metric_distance_graph[unit_in][unit_out], unit_out


def metric_to_systemic(value_in="neg", unit_in="neg", unit_out="neg"):
    if value_in == unit_out == unit_in == "neg":
        value_in = int(input("Enter the value of the distance: "))
        unit_in = input("Convert from: km | m | cm | mm ")
        unit_out = input("Convert to: foot | inch | yard | mile ")

    if unit_in == "km" and unit_out == "mile":
        return value_in * metric_systemic_distance_graph["km"]["mile"], unit_out

    elif unit_in == "km":
        return value_in * metric_systemic_distance_graph["km"]["mile"] * systemic_distance_graph["mile"][
            unit_out], unit_out

    elif unit_out == "mile":
        return value_in * metric_distance_graph[unit_in]["km"] * metric_systemic_distance_graph["km"]["mile"], unit_out

    return value_in * metric_distance_graph[unit_in]["km"] * metric_systemic_distance_graph["km"]["mile"] * \
           systemic_distance_graph["mile"][unit_out], unit_out


def systemic_to_metric(value_in="neg", unit_in="neg", unit_out="neg"):
    if value_in == unit_out == unit_in == "neg":
        value_in = int(input("Enter the value of the distance: "))
        unit_in = input("Convert to: foot | inch | yard | mile ")
        unit_out = input("Convert from: km | m | cm | mm ")

    if unit_in == "mile" and unit_out == "km":
        return value_in * metric_systemic_distance_graph["mile"]["km"], unit_out

    elif unit_in == "mile":
        return value_in * metric_systemic_distance_graph["mile"]["km"] * metric_distance_graph["km"][unit_out], unit_out

    elif unit_out == "km":
        return value_in * systemic_distance_graph[unit_in]["mile"] * metric_systemic_distance_graph["mile"][
            "km"], unit_out

    return value_in * systemic_distance_graph[unit_in]["mile"] * metric_systemic_distance_graph["mile"]["km"] * \
           metric_distance_graph["km"][unit_out], unit_out


def distance_lobby():
    decision = int(input("[1]metric [2]systemic [3]metric to systemic [4]systemic to metric\n"))

    match decision:
        case 1:
            return convert_within_metric()
        case 2:
            return convert_within_systemic()
        case 3:
            return metric_to_systemic()
        case 4:
            return systemic_to_metric()

    distance_lobby()
