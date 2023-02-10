#!/usr/bin/python3
#!/bin/python3

import sys

def periodic_table():
    periodicTable = {}
    with open("periodic_table.txt", "r") as f:
        for line in f:
            elements = line.split(" = ")
            elements[1] = elements[1].split(", ")
            for i, item in enumerate(elements[1]):
                elements[1][i] = elements[1][i].split(":")
            periodicTable[elements[0]] = elements[1]
        with open("periodic_table.html", "w") as f_html:        
            content_html = '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Periodic Table</title>
        <style>
            td {
                border-width: 1px;
                border-style:solid;
                border-collapse: collapse;
                width: 100px;
            }
            li {
                font-size: 12px;
                text-align: left;
            }
            h4{
                font-size: 14px;
                text-align: center;
            }
            p{
                width: 100px;
            }
            .blank {
                border-style: none;
                width: 100px;
            }
            table {
                width: 2160px;
            }
            h1 {
                width: 2160px;
                text-align: center;
                margin: 40px 0 40px 0;
            }
        </style>
    </head>
    <body>
        <h1>Periodic Table</h1>
        <table>
            <tr>'''
            i = 1;
            f_html.write(content_html)
            for key, value in periodicTable.items():
                f_html.write('''
                <td>
                    <h4>''' + key +'''</h4>
                    <ul>
                        <li>No '''+ periodicTable[key][1][1] + '''</li>
                        <li>''' + periodicTable[key][2][1] + '''</li> 
                        <li>''' + periodicTable[key][3][1] + '''</li>
                    </ul> 
                </td>''')

                if(i == 1):
                    count = 0
                    while (count < 16):
                        f_html.write('''
                <td class="blank"></td>''')
                        count = count + 1
                if((i == 4) or (i == 12)):
                    count = 0
                    while (count < 10):
                        f_html.write('''
                <td class="blank"></td>''')
                        count = count + 1
                if((i == 56) or (i == 73)):
                        f_html.write('''
                <td class="blank"></td>''')
                if ((i == 2) or (i == 10) or (i == 71) or ((i%18 == 0) and (i < 55))):
                    f_html.write('''
            </tr><tr>''')                           
                i = i + 1
            final_html = '''
            </tr>
        </table>
    </body>
</html>
            '''
            f_html.write(final_html)

if __name__ == '__main__':
    periodic_table()