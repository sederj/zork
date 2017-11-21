import random
from Weapon import Empty
from Weapon import HersheyKiss
from Weapon import SourStraw
from Weapon import ChocolateBar
from Weapon import NerdBomb
'''
Created on Nov 2, 2017

@author: Joseph Seder, Daniel Gritters
'''

class Player(object):
    '''
    This class holds the game's player object
    '''
    def __init__(self):
        '''
        set the player's initial health, attack, and weapons
        player's attack and health have been boosted for testing
        purposes
        '''
        self.health = random.randrange(10000, 10025)
        self.attack = random.randrange(40, 50)
        self.weapons = []
        self.generateWeapons()
        
    
    def getWeapons(self):
        ''' get the player's list of weapons '''
        return self.weapons
    def getHealth(self):
        ''' get the player's health '''
        return self.health
    def printWeapons(self):
        ''' print the player's current weapon inventory '''
        for ind,weapon in enumerate(self.weapons):
            if(weapon.getName() == "Empty"):
                index = str(ind + 1)
                print(index + ": Empty")
            else:
                print(str(ind + 1) + ": " + weapon.getName() + " " + str(weapon.getUses()))
    def decWeapon(self,weaponNum):
        ''' decrement a weapon from the player's inventory '''
        weapon = self.weapons[weaponNum]
        weapon.decrement()
        if(weapon.getUses() == 0):
            self.weapons[weaponNum] = Empty()
                            
    def attackMon(self,weaponNum,monster):
        ''' subtract the attack of the monster from the player's health '''
        self.health = self.health - monster.attacked(self.attack,self.weapons[weaponNum])

    def generateWeapons(self):
        ''' generate a random list of weapons '''
        self.weapons.append(HersheyKiss())
        for i in range(9):
            weaponNum = random.randint(2,4)
            if (weaponNum == 2):
                self.weapons.append(SourStraw())
            elif (weaponNum == 3):
                self.weapons.append(ChocolateBar())
            elif (weaponNum == 4):
                self.weapons.append(NerdBomb())
            