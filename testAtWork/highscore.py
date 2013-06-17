import time
class HighScore:
   fileName = "highscores.txt"
   highScoreFile = 0
   highScoreArray = []
   def __init__(self):
      try:
         self.highScoreFile = open(self.fileName,"r+")
         self.readFile()
         self.highScoreFile.close()
         self.sortList()
      except IOError:
         print "File doesn't exist, creating"
      self.writeFile()
   def readFile(self):
      for line in self.highScoreFile:
         fields = line.split(" ")
         self.highScoreArray.append((fields[0],fields[1],fields[2],fields[3]))
   def writeFile(self):
      self.highScoreFile = open(self.fileName,"w+")
      for i in range(len(self.highScoreArray)):
         name,playerPoints,aiPoints,turns = self.highScoreArray[i]
         writeString = str(name) + " " + str(playerPoints) + " " + str(aiPoints) + " " + str(turns)
         self.highScoreFile.write(writeString)
      self.highScoreFile.write("")
      self.highScoreFile.close()
   def sortList(self):
      temp = self.highScoreArray.sort(cmp=lambda x,y:self.compareTwoScores(x,y),reverse=True)
   def compareTwoScores(self, list1, list2):
      name1,player1,ai1,turn1 = list1
      name2,player2,ai2,turn2 = list2
      if int(turn1) < int(turn2):
         return 1
      elif int(turn2) < int(turn1):
         return -1
      else:
         if int(ai1) > int(ai2):
            return -1
         elif int(ai2) > int(ai1):
            return 1
         else:
            if int(player1) > int(player2):
               return 1
            elif int(player2) > int(player1):
               return -1
            else:
               return 0

   def addScore(self, name, player, ai, turn):
      self.highScoreArray.append((name,player,ai,str(turn)+"\n"))
      self.sortList()
      if len(self.highScoreArray) > 10:
         self.highScoreArray.pop(10)
      self.writeFile()
      return
#
#h = HighScore()
#h.addScore("asdf",201,199,10)