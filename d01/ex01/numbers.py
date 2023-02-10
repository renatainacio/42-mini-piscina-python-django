#!/usr/bin/python3
#!/bin/python3


def numbers():
    f = open("numbers.txt", "r")
    content = f.read()
    numbers = content.split(",")
    for nbr in numbers:
        print(nbr)
    f.close()

if __name__ == '__main__':
    numbers()