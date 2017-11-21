'''
Created on Nov 20, 2017

@author: Joseph Seder, Daniel Gritters
'''
from abc import ABCMeta, abstractmethod
 
class Observer(object):
        __metaclass__ = ABCMeta
 
        @abstractmethod
        def update(self):
                pass