#!/usr/bin/env python3
"""
Helpdesk simulator
version 0.24
"""
import tkinter, random
from tkinter.scrolledtext import ScrolledText

class Physics:
  def __init__(self):
    self.speech=[] # (id,agentspeaks,direction,string,nextid)
  
    self.speech.append((0,True,"customer->agent","Init",[1,29,48,66 ]))
    self.speech.append((1,True,"customer->agent","My monitor isn't working anymore.",[2,6,7,25]))
    self.speech.append((2,True,'agent->customer',"Please hold.",[3]))
    self.speech.append((3,True,'agent->supervisor',"The monitor of a client is broken.",[4,62]))
    self.speech.append((4,True,"supervisor->agent","Should i open a new ticket?",[5,57]))
    self.speech.append((5,True,'agent->supervisor',"No, because the customer has argued, that he can fix it by himself.",[20]))
    self.speech.append((6,True,'agent->customer',"Can you be more specific?",[14]))
    
    self.speech.append((7,True,'agent->customer',"It's your fault.",[8]))
    self.speech.append((8,True,'customer->agent',"Can i talk to your supervisor please.",[9,11]))
    self.speech.append((9,True,'agent->customer',"No, he isn't available.",[10]))  
    self.speech.append((10,True,'customer->agent',"It's a bad service, bye.",[-1]))  
    self.speech.append((11,True,'agent->customer',"Sure, one moment please.",[-1]))    
    self.speech.append((12,True,'agent->supervisor',"Do you like to talk to a customer?",[12]))
    self.speech.append((13,True,'supervisor->agent',"Nope.",[-1]))
    
    self.speech.append((14,True,'customer->agent',"The display is black and i can see nothing.",[15]))
    self.speech.append((15,True,'agent->customer',"Plug in the monitor cable, does it work now?",[16,18]))
    self.speech.append((16,True,'customer->agent',"Thanks, it was my fault.",[17]))      
    self.speech.append((17,True,'agent->customer',"Have a nice day",[-1]))                  
    self.speech.append((18,True,'customer->agent',"No, it's not working",[19]))
    self.speech.append((19,True,'agent->customer',"Please hold",[-1]))       
           
    self.speech.append((20,True,'supervisor->agent',"Perhaps the cable is broken?",[21,23]))  
    self.speech.append((21,True,'agent->supervisor',"Thank you",[22]))  
    self.speech.append((22,True,'agent->customer',"The cable is broken. Bye",[-1])) 
    self.speech.append((23,True,'agent->supervisor',"Why do you think so?",[24]))  
    self.speech.append((24,True,'supervisor->agent',"Because this is the standard answer given in the manual",[-1]))  
                
    self.speech.append((25,True,'agent->supervisor',"Can you create a new ticket, please?",[26]))   
    self.speech.append((26,True,'supervisor->agent',"Nope, because that's your job.",[27])) 
    self.speech.append((27,True,'agent->supervisor',"you're right, sorry for asking you.",[28])) 
    self.speech.append((28,True,'agent->customer',"I have created a new ticket.",[-1]))                  
                              
    self.speech.append((29,True,"customer->agent","I can't login into my account",[30,37,43]))
    self.speech.append((30,True,"agent->customer","Please hold.",[31]))
    self.speech.append((31,True,"agent->supervisor","Are you familiar with login problems?",[32]))
    self.speech.append((32,True,"supervisor->agent","Sorry, but I'm in an important meeting.",[33]))
    self.speech.append((33,True,"agent->supervisor","You mean, you can't create a simple ticket for the issue?",[34]))
    self.speech.append((34,True,"supervisor->agent","Ok, what should i write down?",[35]))
    self.speech.append((35,True,"agent->supervisor","The user isn't able to login into his account and it's urgent.",[36]))
    self.speech.append((36,True,"agent->customer","A new ticket was created. Bye",[-1]))
    
    self.speech.append((37,True,"agent->supervisor","Can you create a new ticket for a login problem, please?",[38,41]))
    self.speech.append((38,True,"supervisor->agent","Done. Anything else, what i can do for you?",[39]))
    self.speech.append((39,True,"agent->supervisor","Sure, I'd like to get a cup of tea.",[40]))
    self.speech.append((40,True,"agent->customer","I have created a ticket for you, bye.",[-1]))
    self.speech.append((41,True,"supervisor->agent","Nope, and don't call me again.",[42]))
    self.speech.append((42,True,"agent->customer","Sorry, I don't know how to fix it, bye.",[-1]))
    
    self.speech.append((43,True,"agent->customer","Do you know the password?",[44]))
    self.speech.append((44,True,"customer->agent","Yes, I do.",[45]))
    self.speech.append((45,True,"agent->customer","Are you using a desktop PC or a smartphone?",[46]))
    self.speech.append((46,True,"customer->agent","I'm trying to login with a desktop PC.",[47]))
    self.speech.append((47,True,"agent->customer","Please install the latest update of the operating system.",[-1]))
    
    self.speech.append((48,True,"customer->agent","In my Python script there is an error.",[49]))
    self.speech.append((49,True,"agent->customer","Please hold.",[50]))
    self.speech.append((50,True,"agent->supervisor","Can you open a ticket about a Python script problem?",[51]))
    self.speech.append((51,True,"supervisor->agent","First, ask the customer for the details.",[52]))
    self.speech.append((52,True,"agent->supervisor","It's a general Python problem, please create a new ticket first.",[53]))
    self.speech.append((53,True,"supervisor->agent","It sounds, that the topic is important, isn't it?",[54]))
    self.speech.append((54,True,"agent->customer","Sorry, but i don't know how to fix the error in the Python script.",[55]))
    self.speech.append((55,True,"customer->agent","What does that mean?",[56]))
    self.speech.append((56,True,"agent->customer","I will end the conversation, bye.",[-1]))
    
    self.speech.append((57,True,"agent->supervisor","Yes, title: monitor isn't working.",[58]))
    self.speech.append((58,True,"supervisor->agent","It's up to me to find an answer, right?",[59]))
    self.speech.append((59,True,"agent->supervisor","Do you believe it's the cable?",[60]))
    self.speech.append((60,True,"supervisor->agent","No it's the graphics card.",[61]))
    self.speech.append((61,True,"agent->customer","It's the graphics card. Bye",[-1]))

    self.speech.append((62,True,"supervisor->agent","It's his own fault, because his graphics card is configured wrong.",[63]))
    self.speech.append((63,True,"agent->supervisor","But it can be a hardware problem as well.",[64]))
    self.speech.append((64,True,"supervisor->agent","No it's not. The customer has no idea in which position the jumper is.",[65]))
    self.speech.append((65,True,"agent->customer","Perhaps the DIP switch is in the wrong position, bye.",[-1]))

    self.speech.append((66,True,"customer->agent","The server is offline, help.",[67]))
    self.speech.append((67,True,"agent->customer","Please hold.",[68]))
    self.speech.append((68,True,"agent->supervisor","Hi, what is going on?",[69]))
    self.speech.append((69,True,"supervisor->agent","Nothing special, I'm trying to search something.",[70]))
    self.speech.append((70,True,"agent->supervisor","The server of a customer is down.",[71]))
    self.speech.append((71,True,"supervisor->agent","Ops, it was my fault. The new Apache config file has produced an error message.",[72]))
    self.speech.append((72,True,"agent->supervisor","How long does it take to fix it?",[73]))
    self.speech.append((73,True,"supervisor->agent","One hour, maybe longer.",[74]))
    self.speech.append((74,True,"agent->customer","The server will be online soon. Bye.",[-1]))
    
    self.pos=0
    self.cost=0
  def getmessage(self):
    self.cost+=self.getcost(self.pos)
    if self.pos==-1: 
      message="END, total cost="+str(self.cost)+"ct \n"
    else:
      message=self.speech[self.pos][2]+": "+self.speech[self.pos][3]+"\n"
      nodelist=self.speech[self.pos][4]
      self.pos=random.choice(nodelist)
    return message
  def getchoice(self):  
    result=[]
    for i in self.speech[self.pos][4]:
      message=self.speech[i][2]+": "+self.speech[i][3]
      result.append((message,i))
    return result
  def getcost(self,speechid):
    # 5ct for agent speech, 15ct for supervisor speech
    if "supervisor" in self.speech[speechid][2]: result=15
    else: result=5
    return result

class GUI:
  def __init__(self):
    self.fps=10 # 20
    self.myphysics = Physics()
    # tkinter
    self.tkwindow = tkinter.Tk()
    self.tkwindow.title("Helpdesk game v0.24")
    self.tkwindow.geometry("500x300+600+0") # place to right
    self.tkwindow.bind("<Key>", self.inputhandling)
    # tkinter form
    self.widgetinfo = tkinter.Label(self.tkwindow, text="info",justify="left", wraplength=250)
    self.widgetinfo.place(x=10, y=0)    
    self.widgetmessage = ScrolledText(self.tkwindow, width=60, height=8, wrap="word")    
    self.widgetmessage.place(x=10, y=20)
    self.buttonnext = tkinter.Button(self.tkwindow,text="next",command=self.action)
    self.buttonnext.place(x=10, y=250)
    self.buttonreset = tkinter.Button(self.tkwindow,text="reset",command=self.reset)
    self.buttonreset.place(x=80, y=250) 
    self.radiobutton = tkinter.IntVar()     
    # loop 
    self.reset()
    self.gameloop()
  def gameloop(self):
    self.painttkinter()
    self.tkwindow.after(int(1000/self.fps), self.gameloop) # call gameloop every tick             
  def painttkinter(self):
    # info
    result="fps "+str(self.fps)
    result+=" cost "+str(self.myphysics.cost)
    self.widgetinfo.config(text=result)  
  def inputhandling(self,event):
    if event.keysym=="Right": pass
  def reset(self):
    self.widgetmessage.delete('1.0', tkinter.END)
    self.myphysics.pos=0
    self.myphysics.cost=0
    self.action()
  def action(self):
    # message
    temp=self.myphysics.getmessage()
    self.widgetmessage.insert(tkinter.END,temp)
    self.widgetmessage.see(tkinter.END) # scroll to end
    
      
class Game():
  def __init__(self):
    self.mygui = GUI()
    self.mygui.tkwindow.mainloop()

mygame=Game()   
