# This Python file uses the following encoding: utf-8
from Engine import Engin

#class c(Base):
#       def __init__(self):
#           super().__init__("Joe")
#           pass
#       def rename(self, newname):
#           self.name = newname
#text = ["Yolo", "Julien", "Rebecca"]
#dict = {"Chat": 16, "Chien" : "lol", "Souris" : 666}



def main():
    eng = Engin()
    eng.StartGame()
    while(eng.GetRunning()):
        eng.Update()

if __name__ == "__main__":
    main()
