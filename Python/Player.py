import random
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
        self.weapons = Weapon[9]
        weapons[0] = Weapon(True)
        for i in range(9):
            weapons[1+i] = Weapon(False)
        
    