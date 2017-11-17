import random
'''
Created on Nov 2, 2017

@author: User
'''

class Weapon(object):
    '''
    classdocs
    '''


    def __init__(self, weaponNum):
        '''
        Constructor
        '''
        if (weaponNum == 1):
            self.name = "HersheyKisses"
            self.attMod = 1
            self.uses = -1
        elif (weaponNum == 2):
            self.name = "SourStraws"
            self.attMod = random.uniform(1,1.75)
            self.uses = 2
        elif (weaponNum == 3):
            self.name = "ChocolateBars"
            self.attMod = random.uniform(2,2.4)
            self.uses = 4
        elif (weaponNum == 4):
            self.name = "NerdBombs"
            self.attMod = random.uniform(3.5,5)
            self.uses = 1
        
#         if(isDefault == False):
#             randWeap = randrange(0,2)
#             if(randWeap == 0):
#                 self.name = "SourStraws"
#                 self.attMod = uniform(1,1.75)
#                 self.uses = 2
#             elif(randWeap == 1):
#                 self.name = "ChocolateBars"
#                 self.attMod = uniform(2,2.4)
#                 self.uses = 4
#             else:
#                 self.name = "NerdBombs"
#                 self.attMod = uniform(3.5,5)
#                 self.uses = 1
#         else:
#             self.name = "HersheyKisses"
#             self.attMod = 1
#             self.uses = -1
    def getAttack(self, weapon):
        random.randomfloatbetween(lowval, highval)
            
class HersheyKiss(Weapon):

    def __init__(self):
        Weapon.__init__(self, 1)

class SourStraw(Weapon):

    def __init__(self):
        Weapon.__init__(self, 2)

class ChocolateBar(Weapon):

    def __init__(self):
        Weapon.__init__(self, 3)

class NerdBomb(Weapon):

    def __init__(self):
        Weapon.__init__(self, 4)