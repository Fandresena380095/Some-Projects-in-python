#tkinter holds a lot of methods
from tkinter import *

root = Tk() #this will initialize a blank window
root.geometry('300x250') #the height and width of your window

#label(what window are you creating your stuff?, what is the text?)
l = Label(root ,text="Hello World!")
l.pack() #this will add your label in your root windows


root.mainloop() #This holds your view in place

