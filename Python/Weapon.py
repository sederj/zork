import random
'''
Created on Nov 2, 2017

@author: User
'''

class Weapon(object):
    '''
    classdocs
    '''


    def __init__(self, isDefault):
        '''
        Constructor
        '''
        if(isDefault == False):
            randWeap = randrange(0,2)
            if(randWeap == 0):
                self.name = "SourStraws"
                self.attMod = uniform(1,1.75)
                self.uses = 2
            elif(randWeap == 1):
                self.name = "ChocolateBars"
                self.attMod = uniform(2,2.4)
                self.uses = 4
            else:
                self.name = "NerdBombs"
                self.attMod = uniform(3.5,5)
                self.uses = 1
        else:
            self.name = "HersheyKisses"
            self.attMod = 1
            self.uses = -1