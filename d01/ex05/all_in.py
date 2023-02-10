#!/usr/bin/python3
#!/bin/python3

import sys

def get_capital_or_state():
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    if len(sys.argv) != 2:
        return;
    list_args = sys.argv[1].split(",")
    for item in list_args:
        argument = item.strip()
        argument_cap = argument.title()
        if (argument):
            if argument_cap in states:
                print(capital_cities[states[argument_cap]] + " is the capital of " + argument_cap)
            elif argument_cap in capital_cities.values():
                state_code = (list(capital_cities.keys())[list(capital_cities.values()).index(argument_cap)])
                print(argument_cap + " is the capital of " + list(states.keys())[list(states.values()).index(state_code)])         
            else:
                print(argument + " is neither a capital city nor a state")


if __name__ == '__main__':
    get_capital_or_state()