#!/usr/bin/python3

from elements import *

class Page:
    def __init__(self, elem: Elem()) -> None:
        if not isinstance(elem, Elem):
            raise Exception
        self.elem = elem

    def is_valid(self):
        return(self.__check_is_valid(self.elem))
    
    def __check_is_valid(self, elem:Elem()) -> bool:
        tags = (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br)
        if (not(isinstance(elem, tags)) and type(elem) != Text):
            return False
        if(type(elem) == Text or isinstance(elem, Meta)):
            return(True)
        if(isinstance(elem, Html)):
            if(len(self.elem.content) != 2):
                return False 
            try:
                if(type(self.elem.content[0]) is not Head or type(self.elem.content[1]) is not Body):
                    return False
            except IndexError:
                return False
            if(all(self.__check_is_valid(x) for x in elem.content)):
                return True
        return True

if __name__ == '__main__':
    page = Page(Html([Head(Title()),Body()]))
    print(page.is_valid())