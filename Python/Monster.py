import random 
from abc import ABCMeta, abstractmethod
import Weapon
'''
Created on Nov 2, 2017

@author: User
'''

class Monster(object):
    '''
    classdocs
    '''

    def __init__(self, name, attack, health, observer):
        '''
        Constructor
        '''
        self.name = name
        self.health = health
        self.attack = attack
        self.observers = []
        self.observers.append(observer)
    
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
    def attacked(self, personAttPow, weapon):
        self.health = self.health - (personAttPow * weapon.getAttMod())
        if (self.health <= 0):
            self.update()
        return self.attack
    
class Person(Monster):

    def __init__(self,observer):
        #Persons have -1 attack because they restore 1 hp
        Monster.__init__(self, "Person", 100, observer)
    def attacked(self, personAtt, weapon):
        return -1
class Zombie(Monster):

    def __init__(self,observer):
        Monster.__init__(self, "Zombie", random.randint(50, 100), observer)
    def attacked(self, personAtt, weapon):
        if(weapon.getName() == "SourStraws"):
            return random.randint(0,10)
        self.health = self.health - (personAtt * weapon.getAttMod())
        #call a check health method which will call update if dead and switch to a person(might need
        #the monsterlist from game in order to do that)
        return random.randint(0,10)
class Vampire(Monster):

    def __init__(self, observer):
        Monster.__init__(self, random.randint(0, 100) + 100, observer)
    def attacked(self, personAtt, weapon):
        if(weapon.getName() == "ChocolateBars"):
            return random.randint(10,20)
        self.health = self.health - (personAtt * weapon.getAttMod())
        #call a check health method which will call update if dead and switch to a person(might need
        #the monsterlist from game in order to do that)
        return random.randint(10,20)
class Ghoul(Monster):
    
    def __init__(self, observer):
        Monster.__init__(self, random.randint(0, 40) + 40)
    def attacked(self, personAtt, weapon):
        if(weapon.getName() == "NerdBombs"):
            self.health = self.health - (personAtt * weapon.getAttMod() * 5)
            #call a check health method which will call update if dead and switch to a person(might need
            #the monsterlist from game in order to do that)
            return random.randint(15,30)
        self.health = self.health - (personAtt * weapon.getAttMod())
        #call a check health method which will call update if dead and switch to a person(might need
        #the monsterlist from game in order to do that)
        return random.randint(15,30)
class Werewolf(Monster):
    
    def __init__(self, observer):
        Monster.__init__(self, 200)
    def attacked(self, personAtt, weapon):
        if(weapon.getName() == "ChocolateBars" or weapon.getName() == "SourStraws"):
            return random.randint(0,40)
        self.health = self.health - (personAtt * weapon.getAttMod())
        #call a check health method which will call update if dead and switch to a person(might need
        #the monsterlist from game in order to do that)
        return random.randint(0,40)