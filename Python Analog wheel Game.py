
import tkinter
import numpy as np
import pandas as pd
import time
import threading
from random import *
  
class Roulette:
  
 
  
  
 
  def setwindow(self):
   
    self.btn_start = tkinter.Button(self.root, text = 'start/stop',command = self.newtask)
    self.btn_start.place(x=115, y=125, width=65, height=50)
  
    self.btn1 = tkinter.Button(self.root, text='Sam', bg='red')
    self.btn1.place(x=20, y=20, width=50, height=50)
  
    self.btn2 = tkinter.Button(self.root, text='Ram', bg='white')
    self.btn2.place(x=90, y=20, width=50, height=50)
  
    self.btn3 = tkinter.Button(self.root, text='Harry', bg='white')
    self.btn3.place(x=160, y=20, width=50, height=50)
  
    self.btn4 = tkinter.Button(self.root, text='Bini', bg='white')
    self.btn4.place(x=230, y=20, width=50, height=50)
  
    self.btn5 = tkinter.Button(self.root, text='Gita', bg='white')
    self.btn5.place(x=230, y=90, width=50, height=50)
  
    self.btn6 = tkinter.Button(self.root, text='Brita', bg='white')
    self.btn6.place(x=230, y=160, width=50, height=50)
  
    self.btn7 = tkinter.Button(self.root, text='Mike', bg='white')
    self.btn7.place(x=230, y=230, width=50, height=50)
  
    self.btn8 = tkinter.Button(self.root, text='Brinda', bg='white')
    self.btn8.place(x=160, y=230, width=50, height=50)
  
    self.btn9 = tkinter.Button(self.root, text='Dhoni', bg='white')
    self.btn9.place(x=90, y=230, width=50, height=50)
  
    self.btn10 = tkinter.Button(self.root, text='Jack', bg='white')
    self.btn10.place(x=20, y=230, width=50, height=50)
  
    self.btn11 = tkinter.Button(self.root, text='Kapil', bg='white')
    self.btn11.place(x=20, y=160, width=50, height=50)
  
    self.btn12 = tkinter.Button(self.root, text='Kafle', bg='white')
    self.btn12.place(x=20, y=90, width=50, height=50)
  
  

    self.WholeButtons = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11,self.btn12]



  def __init__(self):
    
    self.root = tkinter.Tk()
    self.root.title('Analog Wheel Lottery Game')
    self.root.minsize(300, 300)
    
    self.isloop = False
    self.newloop = False
    
    self.setwindow()
    self.root.mainloop()
  
  
  def rounds(self):
 
    if self.isloop == True:
      return
  
 
    i = 0

    while True:
      if self.newloop == True:
        self.newloop = False
        return
  
  
      time.sleep(0.1)
   
      for x in self.WholeButtons:
        x['bg'] = 'white'
  
  
      self.WholeButtons[i]['bg'] = 'purple'

      i += 1
   
      if i >= len(self.WholeButtons):
        i = 0
  

  def newtask(self):
    if self.isloop == False:
   
      t = threading.Thread(target = self.rounds)
    
      t.start()
    
      self.isloop = True
    elif self.isloop == True:
      self.isloop = False
      self.newloop = True
  
  
c = Roulette()


data = np.random.rand (10000)
Category = (0.0,0.08,0.3,1.0)
labels = ('一等奖','二等奖','三等奖')
result = pd.cut (data,Category,labels=labels)
result = pd.value_counts(result)
print(result)