
'''
Created on Nov 2, 2017

@author: Joseph Seder, Daniel Gritters
'''
from Home import Home
class Neighborhood(object):
    '''
    Neighborhood class information
    '''

    def __init__(self, rows, cols):
        '''
        Constructor
        '''
        self.rows = rows
        self.cols = cols
        self.numMonsters = 0
        self.homes = [[Home(self) for j in range(cols)] for i in range(rows)]
        
    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols
        
    def getHome(self, row, col):
        ''' get the list of homes '''
        return self.homes[row][col]
    
    def getMonsterList(self, row, col):
        ''' get the monster list at the home at row, col '''
        return self.getHome(row,col).getMonsters()
    
    def getNumMonsters(self):
        ''' get the number of monsters '''
        numMonsters = 0
        for row in range(self.rows):
            for col in range(self.cols):
                monsters = self.getHome(row,col).getMonsters()
                for monster in monsters:
                    if (monster.getName() != "Person"):
                        numMonsters = numMonsters + 1
        return numMonsters
     
    def addMonsters(self,addMonsters):
        self.numMonsters = self.numMonsters + addMonsters
        
    def update(self):
        self.numMonsters = self.numMonsters - 1
