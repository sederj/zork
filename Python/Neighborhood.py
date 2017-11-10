
'''
Created on Nov 2, 2017

@author: User
'''

class Neighborhood(object):
    '''
    classdocs
    '''


    def __init__(self, rows, cols):
        '''
        Constructor
        '''
        homes = [[Home() for j in range(cols)] for i in range(rows)]