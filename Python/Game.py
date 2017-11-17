import Neighborhood
import Player
'''
Created on Nov 2, 2017

@author: User
'''
class Game(object):
    """ classdocs """
    

    def __init__(self):
        '''
        Constructor
        '''
        self.neighborhood = Neighborhood(4, 4)
        self.maxRow = 3
        self.maxCol = 3
        self.player = Player()
        self.row = 0
        self.col = 0
        self.gameOver = False
        
    def start(self):
        while (self.gameOver == False):
            command = input()
            if (command[:4] == "move"):
                self.move(self, command[5:])
            elif (command[:6] == "attack"):
                #print weapons with a number and prompt to choose a weapon
                player.printWeapons();
                print("Select the number of the weapon you wish to use.")
                weapon = input()
                #error check input
                if(isinstance(weapon,int)):
                    if(weapon >=1 and weapon <= 10):
                        self.attack(self, weapon)
                    else:
                        print("Invalid weapon. Choose 1-10")
                else:
                    print("Input an integer for the weapon of choice")    
            else:
                print("Invalid Command\n")
        
    def move(self, direction):
        if (direction == "north"):
            self.row = self.row + 1
            if (self.row > self.maxRow):
                self.row = self.maxRow
                print ("You cannot travel further north")
        elif (direction == "south"):
            self.row = self.row - 1
            if (self.row < 1):
                self.row = 0
                print ("You cannot travel further south")
        elif (direction == "east"):
            self.col = self.col + 1
            if (self.col > self.maxCol):
                self.col = self.maxCol
                print ("You cannot travel further east")
        elif (direction == "west"):
            self.col = self.col - 1
            if (self.col < 1):
                self.col = 0
                print ("You cannot travel further west")
        else:
            print("Invalid Direction\n")
    
    def attack(self,weapon):
        monsters = self.neighborhood.getHomes()[self.row,self.col].getMonsterList()
        for monster in monsters:
            self.player.attack(weapon,monster)