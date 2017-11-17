import random 
from abc import ABCMeta, abstractmethod

'''
Created on Nov 2, 2017

@author: User
'''

class Monster(object):
    '''
    classdocs
    '''

    def __init__(self, name, health, attack, observer):
        '''
        Constructor
        '''
        self.name = name
        self.health = health
        self.attack = attack
        self.observers = []
    
    def addObserver(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)
    
    def removeObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def removeAllObservers(self):
        self.observers = []
    def update(self):
        for observer in self.observers:
            observer.update()
    @abstractmethod
    def attacked(self, player, attackPower):
        self.health = self.health - attackPower
        if (self.health <= 0):
            self.update()
        player.
class Person(Monster):

    def __init__(self):
        #Persons have -1 attack because they restore 1 hp
        Monster.__init__(self, "Person", 100, -1)
        
class Zombie(Monster):

    def __init__(self):
        Monster.__init__(self, "Zombie", random.randint(50, 100), )

class Vampire(Monster):

    def __init__(self):
        Monster.__init__(self, random.randint(0, 100) + 100)

class Ghoul(Monster):
    
    def __init__(self):
        Monster.__init__(self, random.randint(0, 40) + 40)

class Werewolf(Monster):
    
    def __init__(self):
        Monster.__init__(self, 200)