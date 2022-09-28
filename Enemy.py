# This Python file uses the following encoding: utf-8
from Actor import Actor

class Enemy(Actor):
    def __init__(self, name, health, strength):
        super().__init__(name, health, strength)
