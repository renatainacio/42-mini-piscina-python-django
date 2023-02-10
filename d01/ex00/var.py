
#!/usr/bin/python3
#!/bin/python3


def myvar():
    intgr = int(42)
    str42 = str("42")
    qd = str("quarante-deux")
    flt42 = float(42)
    boolean = True
    lst = [42]
    dictionary = {42: 42}
    tupla = (42,)
    conjunto = set()
    print(
            str(intgr) + " has a type " + str(type(intgr)) + "\n" +
            str42 + " has a type " + str(type(str42)) + "\n" +
            qd + " has a type " + str(type(qd)) + "\n" +
            str(flt42) + " has a type " + str(type(flt42)) + "\n" +
            str(boolean) + " has a type " + str(type(boolean)) + "\n" +
            str(lst) + " has a type " + str(type(lst)) + "\n" +
            str(dictionary) + " has a type " + str(type(dictionary)) + "\n" +
            str(tupla) + " has a type " + str(type(tupla)) + "\n" +
            str(conjunto) + " has a type " + str(type(conjunto))
        )

if __name__ == '__main__':
    myvar()
