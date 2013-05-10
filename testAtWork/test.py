import pygame, sys, random
from pygame.locals import *
from pygame import font
global length
global gap
global boardCoor
global boardAdjacencyMap
global boardStatus
global columnWidth
global rowHeight
global oddRowOffset
global currentPlayer
def drawSquare(xposition,yposition,length,color):
   pygame.draw.rect(DISPLAYSURF, color, (xposition,yposition,length,length))
def drawSquareByIndex(index,length,color):
   xposition,yposition = boardCoor[index]
   pygame.draw.rect(DISPLAYSURF, color, (xposition,yposition,length,length))
def isWithinSquareByCoordinate(testx,testy,x1,y1,x2,y2):
   if testx > x1 and testx < x2 and testy > y1 and testy < y2:
     return True
   return False
def isWithinSquareByIndex(testx,testy,index):
   x1,y1 = boardCoor[index]
   x2 = x1 + length
   y2 = y1 + length
   if testx > x1 and testx < x2 and testy > y1 and testy < y2:
     return True
   return False
def getColumnCoor(columnIndex,rowIndex):
   if rowIndex % 2 == 1:
      return (columnIndex - 1)*columnWidth + oddRowOffset
   else:
      return (columnIndex - 1)*columnWidth
def getRowCoor(rowIndex):
   return (rowIndex -1)*rowHeight
# 1 2
#3 4 5
# 6 7
#8 9 A
# B C
def isPlayerAdjacent(index, player):
   color = WHITE
   if player == 1:
      color = RED
   else:
      color = BLUE
   goodTile = 0
   adjacentTiles = boardAdjacencyMap[index]
   rtn = False   
   for i in adjacentTiles:
      if boardStatus[i] == color:
         rtn = True
         goodTile = i
         break
   return rtn
pygame.init()

allFont = font.SysFont("monospace",15)
# set up the window
DISPLAYSURF = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOR = BLACK

# draw on the surface object
DISPLAYSURF.fill(BGCOLOR)
length = 50
gap = 3
oddRowOffset = 25
columnWidth = length + gap
rowHeight = length + gap
# 1 2
#3 4 5
# 6 7
#8 9 A
# B C
boardCoor =  { 1:(getColumnCoor(1,1),getRowCoor(1)), 
               2:(getColumnCoor(2,1),getRowCoor(1)), 
               3:(getColumnCoor(1,2),getRowCoor(2)), 
               4:(getColumnCoor(2,2),getRowCoor(2)), 
               5:(getColumnCoor(3,2),getRowCoor(2)),
               6:(getColumnCoor(1,3),getRowCoor(3)),
               7:(getColumnCoor(2,3),getRowCoor(3)),
               8:(getColumnCoor(1,4),getRowCoor(4)),
               9:(getColumnCoor(2,4),getRowCoor(4)),
               10:(getColumnCoor(3,4),getRowCoor(4)),
               11:(getColumnCoor(1,5),getRowCoor(5)),
               12:(getColumnCoor(2,5),getRowCoor(5))
             }

boardAdjacencyMap = { 1:(1,2,3,4),
                      2:(1,2,4,5),
                      3:(1,3,4,6),
                      4:(1,2,3,4,5,6,7),
                      5:(2,4,5,7),
                      6:(3,4,6,7,8,9),
                      7:(4,5,6,7,9,10),
                      8:(6,8,9,11),
                      9:(6,7,8,9,10,11,12),
                      10:(7,9,10,12),
                      11:(8,9,11,12),
                      12:(9,10,11,12)
                    }
boardStatus = {1:WHITE,
               2:WHITE,
               3:WHITE,
               4:BLUE,
               5:WHITE, 
               6:WHITE, 
               7:WHITE, 
               8:WHITE, 
               9:RED, 
               10:WHITE, 
               11:WHITE, 
               12:WHITE
              }
boardStrength = { 1:0,
                  2:0,
                  3:0,
                  4:1,
                  5:0, 
                  6:0, 
                  7:0, 
                  8:0, 
                  9:1, 
                  10:0, 
                  11:0, 
                  12:0
                }
currentPlayerDisplay = ""
for i in range(1, len(boardCoor)+1):
   drawSquareByIndex(i,length,boardStatus[i])
pygame.display.update()

currentPlayer = 1
currentPlayerDisplay = allFont.render("Red Player's turn", 1, WHITE)
DISPLAYSURF.blit(currentPlayerDisplay, (300,0))
for i in range(1, len(boardCoor)+1):
   drawSquareByIndex(i,length,boardStatus[i])
   strength = allFont.render(str(boardStrength[i]),1,BLACK)
   DISPLAYSURF.blit(strength, boardCoor[i])
pygame.display.update()
         
# run the game loop
while True:
   mouseClicked = False
   #DISPLAYSURF.fill(BGCOLOR) # drawing the window
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
         #figure out where the click was
         for i in range(1,len(boardCoor)+1):
            if isWithinSquareByIndex(mousex,mousey,i):
               if currentPlayer == 1:
                  if not isPlayerAdjacent(i,1):
                     continue
                  if boardStatus[i] == WHITE:
                     boardStatus[i] = RED
                     boardStrength[i] = boardStrength[i] +1
                  elif boardStatus[i] == RED:
                     boardStrength[i] = boardStrength[i] +1
                  elif boardStatus[i] == BLUE:
                     redCount = 0
                     for j in range(1,len(boardStatus)+1):
                        if boardStatus[j] == RED:
                           redCount = redCount + 1
                     redCount = redCount/2
                     if redCount >= boardStrength[i]+1:
                        redCount = boardStrength[i]
                     if random.randint(redCount,boardStrength[i]+1) == boardStrength[i]:
                        boardStatus[i] = RED
                        boardStrength[i] = boardStrength[i] / 2 +1
                  currentPlayer = 2
               elif currentPlayer == 2:
                  if not isPlayerAdjacent(i,2):
                     continue
                  if boardStatus[i] == WHITE:
                     boardStatus[i] = BLUE
                     boardStrength[i] = boardStrength[i] +1
                  elif boardStatus[i] == BLUE:
                     boardStrength[i] = boardStrength[i] +1
                  elif boardStatus[i] == RED:
                     blueCount = 0
                     for j in range(1,len(boardStatus)+1):
                        if boardStatus[j] == BLUE:
                           blueCount = blueCount + 1
                     blueCount = blueCount/2
                     if blueCount >= boardStrength[i]+1:
                        blueCount = boardStrength[i]
                     if random.randint(blueCount,boardStrength[i]+1) == boardStrength[i]:
                        boardStatus[i] = BLUE
                        boardStrength[i] = boardStrength[i] / 2+1
                  currentPlayer = 1
               
         #update the board
         DISPLAYSURF.fill(BGCOLOR)
#         pygame.display.update()
         if currentPlayer == 1:
            currentPlayerDisplay = allFont.render("Red Player's turn", 1, WHITE)
         else:
            currentPlayerDisplay = allFont.render("Blue Player's turn", 1, WHITE)
         DISPLAYSURF.blit(currentPlayerDisplay, (300,0))
         
         
         for i in range(1, len(boardCoor)+1):
            drawSquareByIndex(i,length,boardStatus[i])
            strength = allFont.render(str(boardStrength[i]),1,BLACK)
            DISPLAYSURF.blit(strength, boardCoor[i])
         pygame.display.update()
