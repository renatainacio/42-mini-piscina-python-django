#!/usr/bin/python3
#!/bin/python3

import antigravity, sys

def geohashing():
    if len(sys.argv) == 4:
        try:
            dateDow = bytes(sys.argv[3], "UTF-8")
            antigravity.geohash(latitude=float(sys.argv[1]), longitude=float(sys.argv[2]), datedow=dateDow)
        except ValueError as e:
            print(e)
        except Exception as e:
            print("Sorry this program is not smart enough to calculate this...")
    else:
        print("Invalid number of arguments")

if __name__ == '__main__':
    geohashing()