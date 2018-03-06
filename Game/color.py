import random



class ColorGame:
#the list of possible colour.
  COLOR = ['Red','Blue','Green','Pink','White','Yellow','Orange','Purple','Brown']
#the player's score, initially 0.
  SCORE = 0
#the game time left, initially 30 seconds.
  TIME_LEFT = 60


  def __init__(self, event):
    self__event = event
    self.__theColors = ColorGame.COLOR
    self.__differentColor = []
    self.timeLeft = ColorGame.TIME_LEFT
    self.scoreTracker = ColorGame.SCORE



#accssors

  def getColor(self):
    return self.__theColors


#mutators

#a countdown timer function. 
  def countdown(self):

    if self.timeLeft > 0 :
      
      self.timeLeft -= 1

      return self.timeLeft

  def getRandColor(self):
   self.__differentColor = random.shuffle(self.__theColors)
   return self.__differentColor

  
#score changer. Adds points      
  def scoreTrackers(self):
    if self.timeLeft >= 0:
      self.scoreTracker += 1
      return self.scoreTracker 

    
      
    
