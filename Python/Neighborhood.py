
'''
Created on Nov 2, 2017

@author: User
'''
import Home
class Neighborhood(object):
    '''
    classdocs
    '''


    def __init__(self, rows, cols):
        '''
        Constructor
        '''
        self.homes = [[Home() for j in range(cols)] for i in range(rows)]
    
    def getHomes(self):
        return self.homes