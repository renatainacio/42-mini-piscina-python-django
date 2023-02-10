#!/usr/bin/python3
#!/bin/python3

class HotBeverage:
    def __init__(self, name = "hot beverage", price = 0.3) -> None:
        self.price = price
        self.name = name
    
    def __str__(self) -> str:
        txt = "name : {nm}\nprice : {prc: .2f}\ndescription : {desc}".format(nm = self.name, prc = self.price, desc = self.description())
        return(txt)

    def description(self) -> str:
        return("Just some hot water in a cup.")

class Coffee(HotBeverage):
    def __init__(self) -> None:
         super().__init__("coffee", 0.4)
    def description(self) -> str:
         return ("A coffee, to stay awake.")

class Tea(HotBeverage):
    def __init__(self) -> None:
         super().__init__("tea")

class Chocolate(HotBeverage):
    def __init__(self) -> None:
         super().__init__("chocolate", 0.5)
    def description(self) -> str:
         return ("Chocolate, sweet chocolate...")

class Capuccino(HotBeverage):
    def __init__(self) -> None:
         super().__init__("capuccino", 0.45)
    def description(self) -> str:
         return ("Un po’ di Italia nella sua tazza!")