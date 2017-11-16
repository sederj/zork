import random
import Weapon
'''
Created on Nov 2, 2017

@author: User
'''

class Player(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.health = random.randrange(100, 125)
        self.attack = random.randrange(10, 20)
        self.weapons = []
        self.weapons[0] = Weapon(1)
        for i in range(9):
            self.weapons[1+i] = Weapon(random.randint(2,4))
        
    