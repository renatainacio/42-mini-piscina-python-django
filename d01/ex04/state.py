#!/usr/bin/python3
#!/bin/python3

import sys

def get_state():
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
    if sys.argv[1] in capital_cities.values():
        state_code = (list(capital_cities.keys())[list(capital_cities.values()).index(sys.argv[1])])
        print(list(states.keys())[list(states.values()).index(state_code)])
    else:
        print("Unknown capital city")

if __name__ == '__main__':
    get_state()