import random
import Monster 
from Monster import Person
from Monster import Zombie
from Monster import Vampire
from Monster import Ghoul
from Monster import Werewolf
'''
Created on Nov 2, 2017

@author: User
'''

class Home(object):
    '''
    classdocs
    '''


    def __init__(self, observer):
        '''
        Constructor
        '''
        self.numMonsters = 0
        self.monsterList = []
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
            
        self.observer = observer
        observer.addMonsters(self.numMonsters)
        
    def update(self):
        self.observer.update()
    def getMonsters(self):
        return self.monsterList