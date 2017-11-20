import random
from Weapon import Empty
from Weapon import HersheyKiss
from Weapon import SourStraw
from Weapon import ChocolateBar
from Weapon import NerdBomb
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
        self.generateWeapons()
    def getWeapons(self):
        return self.weapons
    def getHealth(self):
        return self.health
    def printWeapons(self):
        for ind,weapon in enumerate(self.weapons):
            #if(weapon.getName() == "Empty"):
            #    index = str(ind + 1)
            #    print(index + ": Empty")
            #else:
            
            print(str(ind + 1) + ": " + weapon.getName() + " " + str(weapon.getUses()))
    def decWeapon(self,weaponNum):
        weapon = self.weapons[weaponNum]
        weapon.decrement()
        if(weapon.getUses() == 0):
            self.weapons[weaponNum] = Empty()
                            
    def attackMon(self,weaponNum,monster):
        self.health = self.health - monster.attacked(self.attack,self.weapons[weaponNum])
    #    if (self.health <= 0):
    #       self.update() we will use this if we decide to make player an observable
    #       I think we should do an observable but it would have to have a different update method
    #        print("Game Over")
    def generateWeapons(self):
        self.weapons.append(HersheyKiss())
        for i in range(8):
            weaponNum = random.randint(2,4)
            if (weaponNum == 2):
                self.weapons.append(SourStraw())
            elif (weaponNum == 3):
                self.weapons.append(ChocolateBar())
            elif (weaponNum == 4):
                self.weapons.append(NerdBomb())
            