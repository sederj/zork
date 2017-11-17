import random
import Weapon
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
    def printWeapons(self):
        for ind,weapon in enumerate(self.weapons):
            if(weapon.getName == "Empty"):
                print((ind + 1) + " Empty")
            else:
                print((ind + 1) + ": " + weapon.getName() + " " + weapon.getUses())
    def attack(self,weapon,monster):
        if(self.weapons[weapon].getName() == "Empty"):
            print("That slot was empty, using Hershey Kisses.")
    def generateWeapons(self):
        self.weapons[0] = HersheyKiss()
        for i in range(8):
            weaponNum = random.randint(2,4)
            if (weaponNum == 2):
                self.weapons.append(SourStraw())
            elif (weaponNum == 3):
                self.weapons.append(ChocolateBar())
            elif (weaponNum == 4):
                self.weapons.append(NerdBomb())
            