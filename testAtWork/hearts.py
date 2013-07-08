import cardTable, drawUtils
import pygame, sys, random, time
from pygame.locals import *
from drawUtils import *

class textDisplay:
   currPlayer = 0
   currentPlayerDisplay = 0
   redPointDisplay = 0
   bluePointDisplay = 0
   redInfluenceDisplay = 0
   blueInfluenceDisplay = 0
   rulesDisplay = [allFont.render("Rules:",1,WHITE),
                   allFont.render("Click to attack adjacent territory",1,WHITE),
                   allFont.render("Click a friendly territory to fortify by your strength",1,WHITE),
                   allFont.render("       A   ",1,WHITE),
                   allFont.render("% = -------",1,WHITE),
                   allFont.render("     A + B ",1,WHITE),
                   allFont.render("",1,WHITE),
                   allFont.render("A = Number of territories attacker owns / 2",1,WHITE),
                   allFont.render("A = Number of territories defender owns / 3 + fortification bonus",1,WHITE),
                   allFont.render("",1,WHITE),
                   allFont.render("Foreach territory:",1,WHITE),
                   allFont.render(" gain points = max(fort bonus, number of adjacent friends)",1,WHITE)                   
                  ]
   def updateTextDisplay(self):
      pygame.draw.rect(MAINWINDOW, BGCOLOR, (300,0,250,100))
      MAINWINDOW.blit(self.currentPlayerDisplay, (300,0))
      MAINWINDOW.blit(self.redPointDisplay, (300,20))
      MAINWINDOW.blit(self.bluePointDisplay, (300,40))
      MAINWINDOW.blit(self.redInfluenceDisplay, (300,60))
      MAINWINDOW.blit(self.blueInfluenceDisplay, (300,80))
      for i in range(1,len(self.rulesDisplay)):
         MAINWINDOW.blit(self.rulesDisplay[i], (0,300+(i-1)*20))
   def changePlayer(self):
      if self.currPlayer == 1:
         self.currPlayer = 2
         self.currentPlayerDisplay = allFont.render("AI's turn, please wait", 1, WHITE)
      else:
         self.currPlayer = 1
         self.currentPlayerDisplay = allFont.render("Red Player's turn", 1, WHITE)
      self.updateTextDisplay()
   def changePoints(self,redPoints,bluePoints):
      redPointsStr = "Red players points = " + str(redPoints)
      bluePointsStr = "Blue players points = " + str(bluePoints)
      self.redPointDisplay = allFont.render(redPointsStr,1,WHITE)
      self.bluePointDisplay = allFont.render(bluePointsStr,1,WHITE)
      self.updateTextDisplay()
   def changeInfluence(self,redInfluence,blueInfluence):
      redInfluenceStr = "Red Player's strength = " + str(redInfluence)
      blueInfluenceStr = "Blue Player's strength = " + str(blueInfluence)
      
      self.redInfluenceDisplay = allFont.render(redInfluenceStr,1,WHITE)      
      self.blueInfluenceDisplay = allFont.render(blueInfluenceStr,1,WHITE)
      self.updateTextDisplay()
      
   def __init__(self,current):
      if current == 1:
         self.currPlayer = 1
         self.currentPlayerDisplay = allFont.render("Red Player's turn", 1, WHITE)
      else:
         self.currPlayer = 2
         self.currentPlayerDisplay = allFont.render("AI's turn, please wait", 1, WHITE)
      self.redPointDisplay = allFont.render("Red players points = 0",1,WHITE)
      self.bluePointDisplay = allFont.render("Blue players points = 0",1,WHITE)
      self.redInfluenceDisplay = allFont.render("Red Player's strength = 1",1,WHITE)
      self.blueInfluenceDisplay = allFont.render("Blue Player's strength = 1",1,WHITE)
      self.updateTextDisplay()
#
class player:
   points = 0
   def updatePoints(self,board,player):
      color = WHITE
      if player == 1:
         color = RED
      else:
         color = BLUE
      for tileIndex in board: 
         tile = board[tileIndex]
         if tile.getStatus() == color:
            adMap = tile.getAdjacencyMap()
            pointsForThisTile = 0
            for adTileIndex in adMap:
               adTile = board[adTileIndex]
               if not adTile == tile:
                  if (adTile.getStatus() == color
                     and pointsForThisTile < tile.getStrength()):
                     self.points = self.points + 1
                     pointsForThisTile = pointsForThisTile + 1
   def getPoints(self):
      return self.points
   def __init__(self):
      self.points = 0
#
class gameLogic:   
   gameNotOver = True
   turnNumber = 0
   pointsToPlayTo = 200
   p1 = player()
   p2 = player()
   currentPlayer = 1
   def __init__(self):
      #nothing to initialize
      pygame.key.set_repeat(500,100)
      MAINWINDOW.fill(BGCOLOR)
      self.gameNotOver = True
      self.turnNumber = 0
      self.pointsToPlayTo = 200
      self.p1 = player()
      self.p2 = player()
      self.currentPlayer = 1
   def displayGame(self,gameMode):
      #display the actual game
      MAINWINDOW.fill(BGCOLOR)
      return
   def displayMenu(self):
      #display the menu to start a new game, single player, multiplayer etc...
      
      self.showMenu()
      hostnameString = ""
      UserHasNotQuit = True
      while UserHasNotQuit:
         mouseClicked = False
         for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               sys.exit()
            elif event.type == MOUSEMOTION:
               mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
               mousex, mousey = event.pos
               mouseClicked = True
            if event.type == KEYDOWN:
               char = event.unicode
               keyname = pygame.key.name(event.key)
               if keyname == "backspace":
                  hostnameString = hostnameString[0:len(hostnameString)-1]
               elif len(hostnameString) < 15:
                  hostnameString = hostnameString + char
               pygame.draw.rect(MAINWINDOW, GREY,  (420,90,170,20))
               self.hostnameDisplay = allFont.render(hostnameString, 1, BLACK)
               MAINWINDOW.blit(self.hostnameDisplay, (420,90))     
               pygame.display.update() 
               
            
            if mouseClicked == True:
               if self.checkIfClickIsWithinMenuButtons(mousex,mousey,300,0,250,20):
                  #start single player mode
                  self.__init__()
                  self.displayGame(1)
                  self.showMenu()
               if self.checkIfClickIsWithinMenuButtons(mousex,mousey,300,30,250,20):
                  #start hotseat mode
                  self.__init__()
                  self.displayGame(2)
                  self.showMenu()
               if self.checkIfClickIsWithinMenuButtons(mousex,mousey,300,60,250,20):
                  #start multiplayer mode
                  self.__init__()
                  self.displayGame(3)
                  self.showMenu()
               #if self.checkIfClickIsWithinMenuButtons(mousex,mousey,300,120,250,20):
                  #display rules
                  
               if self.checkIfClickIsWithinMenuButtons(mousex,mousey,300,200,250,20):
                  UserHasNotQuit = False
                  
      pygame.quit()
      sys.exit()
   def showMenu(self):
      MAINWINDOW.fill(BGCOLOR)
      self.chooseDisplay = allFont.render("Choose play mode", 1, WHITE)
      MAINWINDOW.blit(self.chooseDisplay, (0,0))
      
      pygame.draw.rect(MAINWINDOW, WHITE, (300,0,290,20))   #single
      pygame.draw.rect(MAINWINDOW, GREY,  (300,30,290,20))  #hotseat
      pygame.draw.rect(MAINWINDOW, GREY,  (300,60,290,20))  #LAN
      pygame.draw.rect(MAINWINDOW, GREY,  (300,90,50,20))   #host
      pygame.draw.rect(MAINWINDOW, GREY,  (360,90,50,20))   #join
      pygame.draw.rect(MAINWINDOW, GREY,  (420,90,170,20))  #IP
      pygame.draw.rect(MAINWINDOW, GREY,  (300,160,290,20)) #Rules
      pygame.draw.rect(MAINWINDOW, WHITE, (300,200,290,20)) #Quit
      
      self.singlePlayerDisplay = allFont.render("Single Player", 1, BLACK)
      MAINWINDOW.blit(self.singlePlayerDisplay, (300,0))
      
      self.hotseatDisplay = allFont.render("Multiplayer hotseat", 1, BLACK)
      MAINWINDOW.blit(self.hotseatDisplay, (300,30))
      
      self.multiplayerDisplay = allFont.render("Multiplayer LAN", 1, BLACK)
      MAINWINDOW.blit(self.multiplayerDisplay, (300,60))      
      self.multiplayerDisplay = allFont.render("Host", 1, BLACK)
      MAINWINDOW.blit(self.multiplayerDisplay, (300,90))      
      self.multiplayerDisplay = allFont.render("Join", 1, BLACK)
      MAINWINDOW.blit(self.multiplayerDisplay, (360,90))      
      
      self.helpDisplay = allFont.render("Display Rules", 1, BLACK)
      self.quitDisplay = allFont.render("QUIT", 1, BLACK)
      MAINWINDOW.blit(self.helpDisplay, (300,160))      
      MAINWINDOW.blit(self.quitDisplay, (300,200))      
      pygame.display.update()
   def checkIfClickIsWithinMenuButtons(self,mousex,mousey,boundaryx,boundaryy,lenx,leny):
      if mousex > boundaryx and mousex < boundaryx + lenx and mousey > boundaryy and mousey < boundaryy + leny:
         return True
      return False

#   
gameLogic = gameLogic()    
# run the game loop
gameLogic.displayMenu()