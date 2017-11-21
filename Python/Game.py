from Neighborhood import Neighborhood
from Player import Player
from Monster import Person
from Observer import Observer

'''
Created on Nov 2, 2017

@author: Joseph Seder, Daniel Gritters
'''
class Game(Observer):
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
        
    def getMaxRow(self):
        ''' get the maximum row '''
        return self.maxRow
    def getMaxCol(self):
        ''' get the maximum col '''
        return self.maxCol
        
    def getRow(self):
        ''' return the player's row '''
        return self.row
    def setRow(self, row):
        ''' set the player's row '''
        self.row = row
        
    def getCol(self):
        ''' return the player's col '''
        return self.col
    def setCol(self, col):
        ''' set the player's col '''
        self.col = col
        
    def getGameOver(self):
        ''' return whether or not the game is over '''
        return self.gameOver
    
    def setGameOver(self, gameover):
        ''' set the game over state '''
        self.gameOver = gameover
    
    def start(self):
        ''' start of the game, handles user input '''
        self.printWelcome()
        self.printHelp()
        while (self.gameOver == False):
            print()
            print("You have ", self.neighborhood.getNumMonsters(), " monsters left to destroy!")
            print()
            command = input("command: ")
            if (command[:4] == "move"):
                self.move(command)
            elif (command[:6] == "attack"):
                #print weapons with a number and prompt to choose a weapon
                self.player.printWeapons();
                print("Select the number of the weapon you wish to use.")
                weapon = input()
                #error check input
                weapon = int(weapon)
                # -1 to align with list indices
                weapon = weapon - 1
                if(isinstance(weapon,int)):
                    if(weapon >=0 and weapon <= 9):
                        self.attack(weapon)
                    else:
                        print("Invalid weapon. Choose 1-10")
                else:
                    print("Input an integer for the weapon of choice") 
                    
                if (self.neighborhood.getNumMonsters() <= 0):
                    self.setGameOver(True) 
            elif (command[:8] == "location"):
                print("Neighborhood is a ", (self.getMaxRow()+1), " x ", (self.getMaxCol()+1), " grid \n")
                print("Current row: ", (self.getRow()+1), "\n")
                print("Current col: ", (self.getCol()+1), "\n")  
            elif (command[:4] == "help"):
                self.printHelp()
            elif (command[:11] == "check house"):
                self.printHomeInfo()
            elif (command[:4] == "quit"):
                self.setGameOver(True)
            else:
                print("Invalid Command\n")
                self.printHelp()
        
    def move(self, direction):
        ''' command to move the player north, south, east, or west '''
        direction = direction[5:]
        if (direction == "north"):
            self.setRow(self.getRow() + 1)
            if (self.getRow() > self.getMaxRow()):
                self.setRow(self.getMaxRow())
                print ("You cannot travel further north")
        elif (direction == "south"):
            self.setRow(self.getRow() - 1)
            if (self.getRow() < 1):
                self.setRow(0)
                print ("You cannot travel further south")
        elif (direction == "east"):
            self.setCol(self.getCol() + 1)
            if (self.getCol() > self.getMaxCol()):
                self.setCol(self.getMaxCol())
                print ("You cannot travel further east")
        elif (direction == "west"):
            self.setCol(self.getCol() - 1)
            if (self.getCol() < 1):
                self.setCol(0)
                print ("You cannot travel further west")
        else:
            print("Invalid Direction\n")
    
    def attack(self,weapon):
        ''' attack method of the game, which alters the Player and Monster objects '''
        if (weapon < 0 or weapon > 9):
            print("Invalid weapon selection")
            weapon = 0
        if(weapon != 0 and self.player.getWeapons()[weapon].getName() == "Empty"):
            print("That slot was empty, using Hershey Kisses.")
            weapon = 0
        monsters = self.neighborhood.getMonsterList(self.row,self.col)
        for monster in monsters:
            self.player.attackMon(weapon,monster)
        self.neighborhood.getHome(self.row,self.col).switchMonsters()
        self.player.decWeapon(weapon)
        print("Remaining Player Health: " + str(self.player.getHealth()))
        if(self.player.getHealth() < 0):
            self.setGameOver(True)
            print("Game Over")
            
    def printWelcome(self):
        ''' print a friendly welcome message '''
        print("Welcome to zork! People are monsters in the village and you must save them, by destroying them!")
        print("There are no razors in the candy, but other deadly candy weapons will help you save the village!")
        
    def printHelp(self):
        ''' print the possible user commands '''
        print()
        print("Commands:")
        print("check house")
        print("move direction")
        print("attack")
        print("location")
        print("help")
        print("quit")
        print()
        
    def printHomeInfo(self):
        ''' print info about the home the player is currently at '''
        print()
        print(self.neighborhood.getNumMonsters(), " monsters left")
        monsters = self.neighborhood.getMonsterList(self.row,self.col)
        for monster in monsters:
            print(monster.getName(), " ", monster.getHealth())
        print()
        