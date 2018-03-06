from tkinter import *
from color import *
import tkinter.messagebox

#from guess import *
#create a GUI window.
class gameGUI:
  def __init__(self):
  
    self.root = Tk()
#set the title.
    self.root.title("What's the Color?")
    
#set the size.
    self.root.geometry("400x630")
    self.game = ColorGame("What's the Color?")
    self.root.configure(background="black")
    
    self.photo = PhotoImage(file="cover.gif")
    self.photoLabel = Label(self.root, image=self.photo)
    self.photoLabel.pack()
    
#add an instructions label.
    self.__instructions = Label(self.root, text="Type in the color of the words, and not the word text!", font=('Bell MT bold', 16), bg="black",fg="light green")
    self.__instructions.pack()

#add a score label.
    self.__scoreLabel = Label(self.root, text="Score: ", font=('Time bold', 15), fg="white", bg="black")
    self.__scoreLabel.pack()

#Dynamic Score Label
    self.__scoreLabelVar = StringVar()
    self.__scoreLabelVar.set(value = '')
    self.__labelScore = Label(self.root, textvariable = self.__scoreLabelVar, font=('Time bold',18), fg="red", bg="black")
    self.__labelScore.pack()

#add a time label.
    self.__timeLabel = Label(text = "Time Left", bg="black", fg="white", font=('Time bold', 15))
    self.__timeLabel.pack()
    #self.message = "Time left: %d" % self.game.timeLeft


#Dynamic Timer Label:
    
    self.__timeLabelVar = StringVar()
    self.__timeLabelVar.set(value = '')
    self.__newTimeLabel = Label(self.root, textvariable = self.__timeLabelVar, font=('Time Bold', 18), fg="red", bg="black")
    self.__newTimeLabel.pack()

    

#add a label for displaying the colours.
    self.__label = Label(self.root, font=('Times New Roman bold', 70), bg="black")
    
    self.__label.pack()


###add a text entry box for typing in colours.
    
    self.__nameColorEntry = Entry(self.root, width = 20)
    self.__nameColorEntry.bind('<Return>', self.checkColor)
    self.__nameColorEntry.pack()

   

#Buttons
    self.playButton = Button(self.root, text="Play",command = self.countdown)
    self.playButton.pack()

    self.resetButton = Button(self.root, text="Score", command = self.scoreWindow)
    self.resetButton.pack()
    
    self.quitButton = Button(self.root, text="Quit", command= self.closeWindow)
    self.quitButton.pack()

#Checks if color type matches the color
  def checkColor(self, check):
    if self.__nameColorEntry.get().lower() == self.game.getColor()[3].lower():
      self.game.getRandColor()
      self.__nameColorEntry.delete(0,'end')
      self.__scoreLabelVar.set(self.game.scoreTrackers())
    else:
      self.game.getRandColor()
      self.__nameColorEntry.delete(0, 'end')

    
      
    
#Displays Initial colors
  def showColors(self):
      self.__label.config(fg=str(self.game.getColor()[3]), text=str(self.game.getColor()[2]))
                             

#Starts Countdown Timer and program
  def countdown(self):
    
    if self.game.countdown():

      self.__timeLabelVar.set(self.game.timeLeft)

      self.__newTimeLabel.after(1000,self.countdown)
      
      self.playButton.configure(state= DISABLED)
      self.showColors()
      self.__nameColorEntry.focus_set()


#displays score    
  def scoreWindow(self):
      tkinter.messagebox.showinfo("Result","Your score is: %s" % self.game.scoreTracker)
#ends game
  def closeWindow(self):
    if tkinter.messagebox.askokcancel("Quit", "Are you sure?"):
      self.root.destroy()

      
      
      
      

#start the GUI
gameGUI()
