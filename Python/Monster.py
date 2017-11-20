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

    def __init__(self, name, health, observer):
        '''
        Constructor
        '''
        self.name = name
        self.health = health
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
    def attacked(self, personAtt, weapon):
        pass
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
class Person(Monster):

    def __init__(self,observer):
        #Persons have -1 attack because they restore 1 hp
        Monster.__init__(self, "Person", 100, observer)
    def attacked(self, personAtt, weapon):
        print(self.name)
        return -1
class Zombie(Monster):

    def __init__(self,observer):
        Monster.__init__(self,"Zombie", random.randint(50, 100), observer)
    def attacked(self, personAtt, weapon):
        if(weapon.getName() == "SourStraws"):
            return random.randint(0,10)
        else:
            self.health = self.health - (personAtt * weapon.getAttMod())
        #call a check health method which will call update if dead and switch to a person(might need
        #the monsterlist from game in order to do that)
        print(self.name + " " + str(self.health))
        if(self.health < 0):
            self.update()
        return random.randint(0,10)
class Vampire(Monster):

    def __init__(self, observer):
        Monster.__init__(self,"Vampire",random.randint(0, 100) + 100, observer)
    def attacked(self, personAtt, weapon):
        if(weapon.getName() == "ChocolateBars"):
            print(self.name + " " + str(self.health))
            return random.randint(10,20)
        else:
            self.health = self.health - (personAtt * weapon.getAttMod())
        #call a check health method which will call update if dead and switch to a person(might need
        #the monsterlist from game in order to do that)
        if(self.health < 0):
            self.update()
        print(self.name + " " + str(self.health))
        return random.randint(10,20)
class Ghoul(Monster):
    
    def __init__(self, observer):
        Monster.__init__(self,"Ghoul", random.randint(0, 40) + 40, observer)
    def attacked(self, personAtt, weapon):
        if(weapon.getName() == "NerdBombs"):
            self.health = self.health - (personAtt * weapon.getAttMod() * 5)
            if(self.health < 0):
                self.update()
            #call a check health method which will call update if dead and switch to a person(might need
            #the monsterlist from game in order to do that)
            print(self.name + " " + str(self.health))
            return random.randint(15,30)
        else:
            self.health = self.health - (personAtt * weapon.getAttMod())
            if(self.health < 0):
                self.update()
        #call a check health method which will call update if dead and switch to a person(might need
        #the monsterlist from game in order to do that)
        print(self.name + " " + str(self.health))
        return random.randint(15,30)
class Werewolf(Monster):
    
    def __init__(self, observer):
        Monster.__init__(self,"Werewolf", 200, observer)
    def attacked(self, personAtt, weapon):
        if(weapon.getName() == "ChocolateBars" or weapon.getName() == "SourStraws"):
            print(self.name + " " + str(self.health))
            return random.randint(0,40)
        else:
            self.health = self.health - (personAtt * weapon.getAttMod())
            if(self.health < 0):
                self.update()
        #call a check health method which will call update if dead and switch to a person(might need
        #the monsterlist from game in order to do that)
        print(self.name + " " + str(self.health))
        return random.randint(0,40)