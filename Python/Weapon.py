import random
'''
Created on Nov 2, 2017

@author: Joseph Seder, Daniel Gritters
'''

class Weapon(object):
    '''
    Weapon class information
    '''


    def __init__(self, name, attMod, uses):
        '''
        Constructor
        '''
        self.name = name
        self.attMod = attMod 
        self.uses = uses 
        
    def getName(self):
        ''' get the weapon's name '''
        return self.name
    def getAttMod(self):
        ''' get the weapon's attack modifier '''
        return self.attMod
    def getUses(self):
        ''' get the weapon's uses left '''
        return self.uses
    def decrement(self):
        ''' decrement the weaopon's remaining uses '''
        if(self.uses > 0):
            self.uses = self.uses - 1       

class Empty(Weapon):
    ''' Empty weapon class information '''
    def __init__(self):
        super(Empty, self).__init__("Empty", 0, 0)
                   
class HersheyKiss(Weapon):
    ''' HersheyKiss weapon class information '''
    def __init__(self):
        super(HersheyKiss, self).__init__("HersheyKiss", 1, -1)

class SourStraw(Weapon):
    ''' SourStraw weapon class information '''
    def __init__(self):
        super(SourStraw, self).__init__("SourStraw", random.uniform(1,1.75), 2)
        
class ChocolateBar(Weapon):
    ''' ChocolateBar weapon class information '''
    def __init__(self):
        super(ChocolateBar, self).__init__("ChocolateBar", random.uniform(2,2.4), 4)

class NerdBomb(Weapon):
    ''' NerdBomb weapon class information '''
    def __init__(self):
        super(NerdBomb, self).__init__("NerdBomb", random.uniform(3.5,5), 1)