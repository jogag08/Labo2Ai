# This Python file uses the following encoding: utf-8


class Base:
    name:str
    def __init__(self,name):
        self.name = name
        pass
    def die(self):
        print(self.name)

