#!/usr/bin/python3

from elem import *

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="html", content=content)

class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="head", content=content)

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="body", content=content)

class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr= attr, tag="title", content=content)

class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="meta", content=content, tag_type="simple")

class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="img", content=content, tag_type="simple")

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="table", content=content)

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="th", content=content)

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="tr", content=content)

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="td", content=content)

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="ul", content=content)

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="ol", content=content)

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="li", content=content)

class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="h1", content=content)

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="h2", content=content)

class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="p", content=content)

class Div(Elem):
    def __init__(self, content=None, attr={}) -> None:
        super().__init__(content=content, attr=attr)

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="span", content=content)

class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="hr", content=content, tag_type="simple")

class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, tag="br", content=content, tag_type="simple")

if __name__ == '__main__':
    print( Html( [Head(), Body()] ) )

    print("\n")

    print( Html( [Head(Title(Text("'Hello Ground!'"))), Body([H1(Text("'Oh no, not again!'")), Img(attr={"src":"http://i.imgur.com/pfp3T.jpg"})])] ) )

    print("\n")

    print(Html(
            [Head([
                Meta(attr={"charset":"UTF-8"}),
                Title(Text("My CV"))]), 
                    Body([
                        H1(Text("Renata Vazgauska Inacio")),
                        Hr(),
                        P(Text("Welcome to my CV Draft!")),
                        Div([
                            Img(attr={"src":"https://www.humanresourcesonline.net/images/hr-sg/content-images/priya-june-2020-patrick-tay-work-from-home-lead-istock.jpg", "alt":"computer and coffee image"}),
                            H2(Text("Skills:")),
                            Table(
                                [Tr([Th(Text("Language")),Th(Text("Level"))]),Tr([Td(Text("English")),Td(Text("Advanced"))])])]),
                        Ul([Li(Text("first experience")),Li(Text("second experience"))]),
                        Br(),
                        Ol([Li(Text("hi")),Li(Text("bye"))])
                        ])], attr={"lang":"en"} ) )