import random
import Monster 
from Monster import Person
from Monster import Zombie
from Monster import Vampire
from Monster import Ghoul
from Monster import Werewolf
from Observer import Observer
'''
Created on Nov 2, 2017

@author: Joseph Seder, Daniel Gritters
'''

class Home(Observer):
    '''
    Class to represent a Home, containing a variety of monsters
    '''
    def __init__(self, observer):
        '''
        Constructor (creates 10 random monsters)
        '''
        self.numMonsters = 0
        self.monsterList = []
        
        for i in range(10):        
            randMonster = random.randrange(0,4)
            if(randMonster == 0):
                self.monsterList.append(Person(self))
            elif(randMonster == 1):
                self.monsterList.append(Zombie(self))
                self.numMonsters += 1
            elif(randMonster == 2):
                self.monsterList.append(Vampire(self))
                self.numMonsters += 1
            elif(randMonster == 3):
                self.monsterList.append(Ghoul(self))
                self.numMonsters += 1
            else:
                self.monsterList.append(Werewolf(self))
                self.numMonsters += 1
                
    def getNumMonsters(self):
        ''' return number of monsters in this home '''
        return self.numMonsters
    
    def setNumMonsters(self, numMonsters):
        ''' set the number of monsters in this home '''
        self.numMonsters = numMonsters
                    
    def update(self, monsterName):
        ''' removes a monster from the house's observables '''
        print(monsterName, " killed!")
        self.setNumMonsters(self.numMonsters - 1)
        if (self.getNumMonsters() <= 0):
            print("All monsters in this house have been turned back to people!")
        
    def getMonsters(self):
        ''' return list of monsters in home '''
        return self.monsterList
    
    def switchMonsters(self):
        ''' switch monster to person '''
        deadMonsters = []
        for ind,monster in enumerate(self.monsterList):    
            if(monster.getHealth() < 0):
                deadMonsters.append(ind)
        for x in deadMonsters:
            self.monsterList[x] = Person(self)