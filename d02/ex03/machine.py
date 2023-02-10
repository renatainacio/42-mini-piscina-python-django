#!/usr/bin/python3
#!/bin/python3

import random

import beverages as b

class CoffeeMachine:
    def __init__(self, isWorking = True, coffeesServed = 0) -> None:
        self.isWorking = isWorking
        self.coffeesServed = 0

    class EmptyCup(b.HotBeverage):
        def __init__(self) -> None:
            super().__init__("empty cup", 0.9)
        def description(self) -> str:
            return ("An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        def __init__(self, message = "This coffee machine has to be repaired.") -> None:
            self.message = message
            super().__init__(self.message)

    def repair(self) -> None:
        self.isWorking = True
        self.coffeesServed = 0

    def serve(self, beverage) -> None:
        isEmpty= random.randint(0, 1)
        if (self.coffeesServed == 10):
            self.isWorking = False
            raise self.BrokenMachineException()          
        elif (isEmpty == 0):
            self.coffeesServed += 1
            return(beverage())
        elif (isEmpty):
            self.coffeesServed += 1
            return(self.EmptyCup())                       

if __name__ == '__main__':
    coffeeMachine = CoffeeMachine()
    retry = 2
    bevList = (b.Chocolate, b.Capuccino, b.Coffee, b.Tea)
    while (retry > 0):
        try:
            print(coffeeMachine.serve(random.choice(bevList)))
            print()
        except coffeeMachine.BrokenMachineException as e:
            print(e)
            coffeeMachine.repair()
            print()
            retry -= 1

        