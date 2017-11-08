import random
'''
Created on Nov 2, 2017

@author: User
'''

class Home(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        monsters = 0
        monsterList = []
        randMonster = randrange(0,4)
        if(randMonster == 0):
            monsterList.append(Person(self))
        elif(randMonster == 1):
            monsterList.append(Zombie(self))
            monsters += 1
        elif(randMonster == 2):
            monsterList.append(Vampire(self))
            monster += 1
        elif(randMonster == 3):
            monsterList.append(Ghoul(self))
            monsters += 1
        else:
            monsterList.append(Werewolf(self))
            monsters += 1
    def 
        