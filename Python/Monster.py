import random 
from abc import ABCMeta, abstractmethod
'''
Created on Nov 2, 2017

@author: User
'''

class Monster(object):
    '''
    classdocs
    '''

    def __init__(self, name, health, attack, observer):
        '''
        Constructor
        '''
        self.name = name
        self.health = health
        self.attack = attack
        self.observers = []
    
    def addObserver(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)
    
    def removeObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def removeAllObservers(self):
        self.observers = []
    def update(self):
        for observer in self.observers:
            observer.update()
    @abstractmethod
    def attacked(self, person, weapon):
        pass