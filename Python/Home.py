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
        numMonsters = 0
        monsterList = []
        randMonster = random.randrange(0,4)
        if(randMonster == 0):
            monsterList.append(Person(self))
        elif(randMonster == 1):
            monsterList.append(Zombie(self))
            numMonsters += 1
        elif(randMonster == 2):
            monsterList.append(Vampire(self))
            numMonsters += 1
        elif(randMonster == 3):
            monsterList.append(Ghoul(self))
            numMonsters += 1
        else:
            monsterList.append(Werewolf(self))
            numMonsters += 1
            
        self.observer = observer
        observer.setMonsters(observer.getMonsters() + numMonsters)
        
    def update(self):
        self.observer.update()
    def getMonsters(self):
        return self.monsterList