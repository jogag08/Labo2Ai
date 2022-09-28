# This Python file uses the following encoding: utf-8
from Enemy import Enemy
from Hero import Hero
from ActorInfos import ActorInfos

class Engin:
    __isRunning:bool = False
    __actorInfos:ActorInfos


    def __init__(self):
        self.SetRunning(True)

    def StartGame(self):
        goblin = Enemy("Goblin", 10, 3)
        zombie = Enemy("Zombie", 7, 3)
        troll = Enemy("Troll", 30, 6)
        print("Welcome to Text Adventure!")
        print("Please select a class : ")
        output = self.GetInput("1. Knigth  2. Mage  3. Rogue\n")
        match output:
            case '1':
                player = Hero("Player", 60, 6)
                print("You chose the Knight")
            case '2':
                player = Hero("Player", 50, 5)
                print("You chose the Mage")
            case '3':
                player = Hero("Player", 45, 5)
                print("You chose the Rogue")

    def GetRunning(self):
        return self.__isRunning

    def SetRunning(self, value):
        self.__isRunning = value

    def Update(self):




    def GetInput(self, strValue):
        output = input(strValue)
        return output


