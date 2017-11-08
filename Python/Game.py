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
        
    def move(self, direction):
        if (direction == "north"):
            self.row = self.row + 1
            if (self.row > self.maxRow):
                self.row = self.maxRow
                print ("You cannot travel further north")
        if (direction == "south"):
            self.row = self.row - 1
            if (self.row < 1):
                self.row = 0
                print ("You cannot travel further south")
        if (direction == "east"):
            self.col = self.col + 1
            if (self.col > self.maxCol):
                self.col = self.maxCol
                print ("You cannot travel further east")
        if (direction == "west"):
            self.col = self.col - 1
            if (self.col < 1):
                self.col = 0
                print ("You cannot travel further west")
        