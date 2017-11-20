
'''
Created on Nov 2, 2017

@author: User
'''
from Home import Home
class Neighborhood(object):
    '''
    classdocs
    '''


    def __init__(self, rows, cols):
        '''
        Constructor
        '''
        self.numMonsters = 0
        self.homes = [[Home(self) for j in range(cols)] for i in range(rows)]
        
        
        
    def getHomes(self):
        return self.homes
    def getMonsterList(self, row, col):
        return self.homes[row][col].getMonsters()
    def getNumMonsters(self):
        return self.numMonsters
    def addMonsters(self,addMonsters):
        self.numMonsters = self.numMonsters + addMonsters