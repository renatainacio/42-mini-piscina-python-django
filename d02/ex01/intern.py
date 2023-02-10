#!/usr/bin/python3
#!/bin/python3

class Intern:
    class Coffee:
        def __init__(self) -> None:
            pass
        def __str__(self) -> str:
            return ("This is the worst coffee you ever tasted.")
    
    def __init__(self, name = "My name? I’m nobody, an intern, I have no name.") -> None:
        self.name = name
    
    def __str__(self) -> str:
        return self.name
    
    def work(self) -> None:
        raise Exception("I’m just an intern, I can’t do that...")
    
    def make_coffee(self) -> Coffee:
        return(self.Coffee())


if __name__ == '__main__':
    intern1 = Intern()
    internMark = Intern("Mark")
    print(intern1)
    print(internMark)
    print(internMark.make_coffee())
    try:
        intern1.work()
    except Exception as e:
        print(e)


