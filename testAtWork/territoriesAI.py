import random, board, drawUtils
from drawUtils import *
class AI:
   stateOfBoard = 0
   ATTACK = 1
   CONQUER = 2
   state = 2
   
   def getNextMove(self,board):
      self.stateOfBoard = board
      if self.state == self.ATTACK:
         indexOfHighestOwned = 0
         for i in range(1,len(self.stateOfBoard)+1):
            if self.stateOfBoard[i].getStatus() == BLUE:
               indexOfHighestOwned = i
         tileToInvadeFrom = self.stateOfBoard[indexOfHighestOwned]
         potentialTilesToInvade = tileToInvadeFrom.getAdjacencyMap()
         
         highestWhite = 0
         highestRed = 0
         for index in potentialTilesToInvade:
            if (self.stateOfBoard[index].getStatus() == WHITE
            and index > highestWhite):
               highestWhite = index
            if (self.stateOfBoard[index].getStatus() == RED
            and index > highestRed):
               highestRed = index
         #
         if highestWhite == 0 and highestRed == 0:
            self.state = 2
         elif highestWhite == 0:
            return highestRed
         else:
            return highestWhite
      if self.state == self.CONQUER:
         #get a list of all attackable tiles
         isTileAttackable = {1: False,
                             2: False,
                             3: False,
                             4: False,
                             5: False,
                             6: False,
                             7: False,
                             8: False,
                             9: False,
                             10: False,
                             11: False,
                             12: False
                            }
         redCount = 0
         blueCount = 0
         for tileIndex in self.stateOfBoard:
            tile = self.stateOfBoard[tileIndex]
            if tile.getStatus() == RED:
               redCount = redCount + 1
            elif tile.getStatus() == BLUE:
               blueCount = blueCount + 1
               for adjacentIndex in tile.getAdjacencyMap():
                  adjacentTile = self.stateOfBoard[adjacentIndex] 
                  if (adjacentTile.getStatus() == BLUE or isTileAttackable[adjacentIndex] == True):
                     continue
                  isTileAttackable[adjacentIndex] = True
         #find attack that has best chance of success
         indexOfBestTile = 0
         odds = 0
        
         redCount = redCount /3
         blueCount = blueCount /2
         for index in isTileAttackable:
            if isTileAttackable[index] == True:
               #print "tile " + str(index) + " is attackable"
               if self.stateOfBoard[index].getStatus() == WHITE:
                  odds = 100
                  indexOfBestTile = index
                  continue
               strength = self.stateOfBoard[index].getStrength()
               oddsForThisTile = (blueCount*100)/(blueCount+redCount+strength)
               #print "-odds = " + str(oddsForThisTile)
               if oddsForThisTile >= odds:
                  odds = oddsForThisTile
                  indexOfBestTile = index
                  #print "--best odds yet = " + str(odds)
         #print "attacking: " +str(indexOfBestTile)
         
         return indexOfBestTile
   
   def __init__(self):
      self.state = 2
      
   #