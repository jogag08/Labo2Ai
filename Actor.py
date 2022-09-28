# This Python file uses the following encoding: utf-8

class Actor:
    __name:str
    __health:int
    __strength:int
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        pass

    def MeleeAttack(self):
        pass

    def RangeAttack(self):
        pass

    def SetName(self, n:str):
        self.__name = n

    def GetName(self)
        return __name

    def SetHealth(self, hp:int):
        self.__health = hp

    def GetHealth(self)
        return __health

    def SetStrength(self, hp:int):
        self.__health = hp

    def GetStrength(self)
        return __health


