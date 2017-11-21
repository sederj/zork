import random 
from abc import ABCMeta, abstractmethod
from Observable import Observable
'''
Created on Nov 2, 2017

@author: Joseph Seder, Daniel Gritters
'''

class Monster(Observable):
    '''
    Class to store monster information
    '''

    def __init__(self, name, health, house):
        '''
        Constructor
        '''
        super(Monster, self).__init__()
        self.name = name
        self.health = health
        self.add_observer(house)

    def update(self):
        ''' notify house upon defeat '''
        for observer in self.observers:
            observer.update(self.getName())
    @abstractmethod
    def attacked(self, personAttPow, weapon):
        ''' abstract method called when attacked '''
        pass
    
    def getName(self):
        ''' get monster name '''
        return self.name
    def setName(self, name):
        ''' set monster name '''
        self.name = name
    
    def getHealth(self):
        ''' get monster health '''
        return int(self.health)
    def setHealth(self, health):
        ''' set monster health '''
        self.health = health
    
class Person(Monster):
    ''' Person class '''
    def __init__(self,observer):
        #Persons have -1 attack because they restore 1 hp
        super(Person, self).__init__("Person", 100, observer)
    def attacked(self, personAtt, weapon):
        return -1
    
class Zombie(Monster):
    ''' Zombie class '''
    def __init__(self,observer):
        super(Zombie, self).__init__("Zombie", random.randint(50,100), observer)
    def attacked(self, personAtt, weapon):
        if(weapon.getName() == "SourStraws"):
            return random.randint(0,10)
        else:
            self.setHealth(self.getHealth() - (personAtt * weapon.getAttMod()))
        #call a check health method which will call update if dead and switch to a person(might need
        #the monsterlist from game in order to do that)
        if(self.getHealth() < 0):
            self.update()
        else:
            print(self.getName(), " ", str(self.getHealth()))
        return random.randint(0,10)
    
class Vampire(Monster):
    ''' Vampire class '''
    def __init__(self, observer):
        super(Vampire, self).__init__("Vampire", random.randint(100,200), observer)
    def attacked(self, personAtt, weapon):
        if(weapon.getName() == "ChocolateBars"):
            print(self.getName() + " " + str(self.getHealth()))
            return random.randint(10,20)
        else:
            self.setHealth(self.getHealth() - (personAtt * weapon.getAttMod()))
        #call a check health method which will call update if dead and switch to a person(might need
        #the monsterlist from game in order to do that)
        if(self.getHealth() < 0):
            self.update()
        else:
            print(self.getName(), " ", str(self.getHealth()))
        return random.randint(10,20)
    
class Ghoul(Monster):
    ''' Ghoul class '''
    def __init__(self, observer):
        super(Ghoul, self).__init__("Ghoul", random.randint(40,80), observer)
    def attacked(self, personAtt, weapon):
        if(weapon.getName() == "NerdBombs"):
            self.setHealth(self.getHealth() - (personAtt * weapon.getAttMod() * 5))
            if(self.getHealth() < 0):
                self.update()
            else:
                print(self.getName(), " ", str(self.getHealth()))
            return random.randint(15,30)
        else:
            self.setHealth(self.getHealth() - (personAtt * weapon.getAttMod()))
            if(self.getHealth() < 0):
                self.update()
            else:
                print(self.getName(), " ", str(self.getHealth()))
        #call a check health method which will call update if dead and switch to a person(might need
        #the monsterlist from game in order to do that)
        return random.randint(15,30)
    
class Werewolf(Monster):
    ''' Werewolf class '''
    def __init__(self, observer):
        super(Werewolf, self).__init__("Werewolf", 200, observer)
    def attacked(self, personAtt, weapon):
        if(weapon.getName() == "ChocolateBars" or weapon.getName() == "SourStraws"):
            print(self.getName() + " " + str(self.getHealth()))
            return random.randint(0,40)
        else:
            self.setHealth(self.getHealth() - (personAtt * weapon.getAttMod()))
            if(self.getHealth() < 0):
                self.update()
            else:
                print(self.getName(), " ", str(self.getHealth()))
        #call a check health method which will call update if dead and switch to a person(might need
        #the monsterlist from game in order to do that)
        return random.randint(0,40)