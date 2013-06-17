import board, drawUtils, territoriesAI, highscore
import pygame, sys, random, time
from pygame.locals import *
from drawUtils import *
from territoriesAI import AI
from board import Board
from highscore import HighScore
global currentPlayer
# draw on the surface object
MAINWINDOW.fill(BGCOLOR)
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
#      self.updateRules()
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
b = Board()
ai = AI(b.board)
highScoreInterface = HighScore()
turnNumber = 0
pointsToPlayTo = 200
p1 = player()
p2 = player()

currentPlayerDisplay = ""
for i in range(1, len(b.board)+1):
   b.drawSquareByIndex(i,b.tileLength,b.board[i].getStatus())
pygame.display.update()

currentPlayer = 1
redPoints = 0
bluePoints = 0
textBox = textDisplay(currentPlayer)
textBox.changePoints(redPoints,bluePoints)
for i in range(1, len(b.board)+1):
   b.drawSquareByIndex(i,b.tileLength,b.board[i].getStatus())
   strength = allFont.render(str(b.board[i].getStrength()),1,BLACK)
   MAINWINDOW.blit(strength, b.board[i].getCoordinate())
pygame.display.update()
         
# run the game loop
while True:
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
      if mouseClicked == True:
         turnNumber = turnNumber + 1
         #figure out where the click was
         for i in range(1,len(b.board)+1):
            if b.isWithinSquareByIndex(mousex,mousey,i):
               
               redCount = 0
               blueCount = 0
               for j in range(1,len(b.board)+1):
                  if b.board[j].getStatus() == RED:
                     redCount = redCount + 1
                  if b.board[j].getStatus() == BLUE:
                     blueCount = blueCount + 1
               if currentPlayer == 1:
                  if not b.isPlayerAdjacent(i,1):
                     continue
                  if b.board[i].getStatus() == WHITE:
                     b.board[i].setStatus(RED)
                     b.board[i].setStrength(redCount)
                  elif b.board[i].getStatus() == RED:
                     b.board[i].setStrength(redCount)
                  elif b.board[i].getStatus() == BLUE:
                     redCount = redCount/2
                     blueCount = blueCount/3 + b.board[i].getStrength()
                     r = random.randint(1,100)
                     if r > (100*redCount)/(blueCount+redCount):
                        b.board[i].setStatus(RED)
                        b.board[i].setStrength(redCount)
                  currentPlayer = 2
               elif currentPlayer == 2:
                  if not b.isPlayerAdjacent(i,2):
                     continue
                  if b.board[i].getStatus() == WHITE:
                     b.board[i].setStatus(BLUE)
                     b.board[i].setStrength(b.board[i].getStrength() +1)
                  elif b.board[i].getStatus() == BLUE:
                     b.board[i].setStrength(b.board[i].getStrength() +1)
                  elif b.board[i].getStatus() == RED:
                     blueCount = blueCount/2
                     redCount = redCount/3 + b.board[i].getStrength()
                     r = random.randint(1,100)
                     if r > (100*blueCount)/(blueCount+redCount):
                        b.board[i].setStatus(BLUE)
                        b.board[i].setStrength(blueCount)
                  currentPlayer = 1
               
         #update the board
         MAINWINDOW.fill(BGCOLOR)
         textBox.changePlayer()
         
         redCount = 0
         blueCount = 0
         for i in range(1,len(b.board)+1):
            if b.board[i].getStatus() == RED:
               redCount = redCount + 1
            if b.board[i].getStatus() == BLUE:
               blueCount = blueCount + 1
            b.drawSquareByIndex(i,b.tileLength,b.board[i].getStatus())
            strength = allFont.render(str(b.board[i].getStrength()),1,BLACK)
            MAINWINDOW.blit(strength, b.board[i].getCoordinate())
         textBox.changeInfluence(redCount,blueCount)
         pygame.display.update()
         time.sleep(0.5)
         aiMove = ai.getNextMove(b.board)
         
         if b.isPlayerAdjacent(aiMove,2):
            if b.board[aiMove].getStatus() == WHITE:
               b.board[aiMove].setStatus(BLUE)
               b.board[aiMove].setStrength(blueCount)
            elif b.board[aiMove].getStatus() == BLUE:
               b.board[aiMove].setStrength(blueCount)
            elif b.board[aiMove].getStatus() == RED:
               blueCount = blueCount/2
               redCount = redCount/3 + b.board[aiMove].getStrength()
               r = random.randint(1,100)
               if r > (100*blueCount)/(blueCount+redCount):
                  b.board[aiMove].setStatus(BLUE)
                  b.board[aiMove].setStrength(blueCount)
         currentPlayer = 1
         
         MAINWINDOW.fill(BGCOLOR)
         textBox.changePlayer()
         p1.updatePoints(b.board,1)
         p2.updatePoints(b.board,2)
         
         textBox.changePoints(p1.getPoints(),p2.getPoints())
         redCount = 0
         blueCount = 0
         for i in range(1, len(b.board)+1):
            if b.board[i].getStatus() == RED:
               redCount = redCount + 1
            if b.board[i].getStatus() == BLUE:
               blueCount = blueCount + 1
            b.drawSquareByIndex(i,b.tileLength,b.board[i].getStatus())
            strength = allFont.render(str(b.board[i].getStrength()),1,BLACK)
            MAINWINDOW.blit(strength, b.board[i].getCoordinate())
         textBox.changeInfluence(redCount,blueCount)
         pygame.display.update()
         
         if p1.getPoints() >= pointsToPlayTo:
            if p2.getPoints() > p1.getPoints():
               print "AI wins"
               winnerDisplay = allFont.render("So Sorry! You LOST!", 1, WHITE)
               MAINWINDOW.blit(winnerDisplay, (300,100))
               pygame.display.update()
               highScoreInterface.addScore("AI",p2.getPoints(),p1.getPoints(),turnNumber)
               time.sleep(3)
               pygame.quit()
               sys.exit()
               
            print "Player wins"
            winnerDisplay = allFont.render("Congratulations! You WON!", 1, WHITE)
            MAINWINDOW.blit(winnerDisplay, (300,100))
            pygame.display.update()
            highScoreInterface.addScore("player",p1.getPoints(),p2.getPoints(),turnNumber)
            time.sleep(3)
            pygame.quit()
            sys.exit()
         elif p2.getPoints() >= pointsToPlayTo:
            print "AI wins"
            winnerDisplay = allFont.render("So Sorry! You LOST!", 1, WHITE)
            MAINWINDOW.blit(winnerDisplay, (300,100))
            pygame.display.update()
            highScoreInterface.addScore("AI",p2.getPoints(),p1.getPoints(),turnNumber)
            time.sleep(3)
            pygame.quit()
            sys.exit()
         
