#!/usr/bin/python3
#!/bin/python3

import sys

def render():
    if len(sys.argv) != 2:
        print("Wrong number of arguments!")
        return
    if ((sys.argv[1].find('.') == -1) or (sys.argv[1].split(".")[1] != "template")):
        print("Invalid file extension")
        return
    settings = {}
    try:
        ftemplate = open(sys.argv[1], "r")
    except FileNotFoundError:
        print("File not found!")
    content = ftemplate.read()
    with open("settings.py", "r") as fsettings:
        for line in fsettings:
            aux = line.split("=")
            try:
                settings[aux[0].strip().strip("'").strip('"')] = aux[1].strip().strip("'").strip('"')
            except IndexError:
                print("Settings file not properly formatted")
                return
        with open(sys.argv[1].split(".")[0]+".html", "w") as fHtml:
            try:
                fHtml.write(content.format(**settings))
            except KeyError as e:
                print("Template file contains attributes not found in Settings file: " + str(e))
    ftemplate.close()
                

if __name__ == '__main__':
    render()

