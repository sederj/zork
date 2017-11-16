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
        self.maxRow = 4
        self.maxCol = 4
        self.player = Player()
        self.row = 1
        self.col = 1
        self.gameOver = False
        
    def start(self):
        while (self.gameOver == False):
            command = input()
            if (command[:4] == "move"):
                self.move(self, command[5:])
            elif (command[:6] == "attack"):
                self.attack(self, command[5:])
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
    
    def attack(self):
        
        