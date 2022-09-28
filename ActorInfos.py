# This Python file uses the following encoding: utf-8

from Hero import Hero

class ActorInfos:
    #Attributs classes
    Knight_Name:str ="Player"
    Knight_HP:int = 60
    Knight_Strength:int = 6

    Mage_Name:str ="Player"
    Mage_HP:int = 50
    Mage_Strength:int = 5

    Rogue_Name:str ="Player"
    Rogue_HP:int = 45
    Rogue_Strength:int = 5

    #Attributs ennemis
    Gobelin_Name:str ="Gobelin"
    Gobelin_HP:int = 10
    Gobelin_Strength:int = 2

    Zombie_Name:str ="Zombie"
    Zombie_HP:int = 15
    Zombie_Strength:int = 3

    Troll_Name:str ="Troll"
    Troll_HP:int = 20
    Troll_Strength:int = 4

    def InitPlayer(self, player:Hero, choice:str):
        match choice:
            case '1':
                player.
