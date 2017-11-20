import random
'''
Created on Nov 2, 2017

@author: User
'''

class Weapon(object):
    '''
    classdocs
    '''


    def __init__(self, name, attMod, uses):
        '''
        Constructor
        '''
        self.name = name
        self.attMod = attMod 
        self.uses = uses 
        
    def getName(self):
        return self.name
    def getAttMod(self):
        return self.attMod
    def getUses(self):
        return self.uses
    def decrement(self):
        if(self.uses > 0):
            self.uses = self.uses - 1       
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
class Empty(Weapon):
    def __init__(self):
        super(Empty, self).__init__("Empty", 0, 0)
#         self.name = "Empty"
#         self.attMod = 0
#         self.uses = 0 
                   
class HersheyKiss(Weapon):
    def __init__(self):
        super(HersheyKiss, self).__init__("HersheyKiss", 1, -1)
#         self.name = "HersheyKiss"
#         self.attMod = 1
#         self.uses = -1

class SourStraw(Weapon):
    def __init__(self):
        super(SourStraw, self).__init__("SourStraw", random.uniform(1,1.75), 2)
#         self.name = "SourStraws"
#         self.attMod = random.uniform(1,1.75)
#         self.uses = 2
        
class ChocolateBar(Weapon):
    def __init__(self):
        super(ChocolateBar, self).__init__("ChocolateBars", random.uniform(2,2.4), 4)
#         self.name = "ChocolateBars"
#         self.attMod = random.uniform(2,2.4)
#         self.uses = 4

class NerdBomb(Weapon):
    def __init__(self):
        super(NerdBomb, self).__init__("NerdBomb", random.uniform(3.5,5), 1)
#         self.name = "NerdBombs"
#         self.attMod = random.uniform(3.5,5)
#         self.uses = 1