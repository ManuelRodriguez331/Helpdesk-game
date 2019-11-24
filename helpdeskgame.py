#!/usr/bin/env python3
"""
Helpdesk simulator
version 0.4

"""
import tkinter, random, time
from tkinter.scrolledtext import ScrolledText

class Physics:
  def __init__(self):
    # (id,agentspeaks,direction,string,nextid)
    # nextid=-1 -> speech ends
    self.speech=[ 
      (0,"customer->agent","Init",[1,29,48,66]),
      (1,"customer->agent","My monitor isn't working anymore.",[2,6,7,25]),
      (2,'agent->customer',"Please hold.",[3,102]),
      (3,'agent->supervisor',"The monitor of a client is broken.",[4,62]),
      (4,"supervisor->agent","Should i open a new ticket?",[5,57]),
      (5,'agent->supervisor',"No, because the customer has argued, that he can fix it by himself.",[20]),
      (6,'agent->customer',"Can you be more specific?",[14]),
      
      (7,'agent->customer',"It's your fault.",[8]),
      (8,'customer->agent',"Can i talk to your supervisor please.",[9,11]),
      (9,'agent->customer',"No, he isn't available.",[10]),  
      (10,'customer->agent',"It's a bad service, bye.",[-1]),  
      (11,'agent->customer',"Sure, one moment please.",[-1]),    
      (12,'agent->supervisor',"Do you like to talk to a customer?",[12]),
      (13,'supervisor->agent',"Nope.",[-1]),
      
      (14,'customer->agent',"The display is black and i can see nothing.",[15]),
      (15,'agent->customer',"Plug in the monitor cable, does it work now?",[16,18]),
      (16,'customer->agent',"Thanks, it was my fault.",[17]),      
      (17,'agent->customer',"Have a nice day",[-1]),                  
      (18,'customer->agent',"No, it's not working",[19]),
      (19,'agent->customer',"Please hold",[-1]),       
             
      (20,'supervisor->agent',"Perhaps the cable is broken?",[21,23]),  
      (21,'agent->supervisor',"Thank you",[22]),  
      (22,'agent->customer',"The cable is broken. Bye",[-1]), 
      (23,'agent->supervisor',"Why do you think so?",[24]),  
      (24,'supervisor->agent',"Because this is the standard answer given in the manual",[-1]),  
                  
      (25,'agent->supervisor',"Can you create a new ticket, please?",[26]),   
      (26,'supervisor->agent',"Nope, because that's your job.",[27]), 
      (27,'agent->supervisor',"you're right, sorry for asking you.",[28]), 
      (28,'agent->customer',"I have created a new ticket.",[-1]),                  
                                
      (29,"customer->agent","I can't login into my account",[30,37,43]),
      (30,"agent->customer","Please hold.",[31]),
      (31,"agent->supervisor","Are you familiar with login problems?",[32]),
      (32,"supervisor->agent","Sorry, but I'm in an important meeting.",[33]),
      (33,"agent->supervisor","You mean, you can't create a simple ticket for the issue?",[34]),
      (34,"supervisor->agent","Ok, what should i write down?",[35]),
      (35,"agent->supervisor","The user isn't able to login into his account and it's urgent.",[36]),
      (36,"agent->customer","A new ticket was created. Bye",[-1]),
      
      (37,"agent->supervisor","Can you create a new ticket for a login problem, please?",[38,41]),
      (38,"supervisor->agent","Done. Anything else, what i can do for you?",[39]),
      (39,"agent->supervisor","Sure, I'd like to get a cup of tea.",[40]),
      (40,"agent->customer","I have created a ticket for you, bye.",[-1]),
      (41,"supervisor->agent","Nope, and don't call me again.",[42]),
      (42,"agent->customer","Sorry, I don't know how to fix it, bye.",[-1]),
      
      (43,"agent->customer","Do you know the password?",[44]),
      (44,"customer->agent","Yes, I do.",[45]),
      (45,"agent->customer","Are you using a desktop PC or a smartphone?",[46]),
      (46,"customer->agent","I'm trying to login with a desktop PC.",[47]),
      (47,"agent->customer","Please install the latest update of the operating system.",[-1]),
      
      (48,"customer->agent","In my Python script there is an error.",[49]),
      (49,"agent->customer","Please hold.",[50]),
      (50,"agent->supervisor","Can you open a ticket about a Python script problem?",[51]),
      (51,"supervisor->agent","First, ask the customer for the details.",[52]),
      (52,"agent->supervisor","It's a general Python problem, please create a new ticket first.",[53]),
      (53,"supervisor->agent","It sounds, that the topic is important, isn't it?",[54]),
      (54,"agent->customer","Sorry, but i don't know how to fix the error in the Python script.",[55]),
      (55,"customer->agent","What does that mean?",[56]),
      (56,"agent->customer","I will end the conversation, bye.",[-1]),
      
      (57,"agent->supervisor","Yes, title: monitor isn't working.",[58]),
      (58,"supervisor->agent","It's up to me to find an answer, right?",[59]),
      (59,"agent->supervisor","Do you believe it's the cable?",[60]),
      (60,"supervisor->agent","No it's the graphics card.",[61]),
      (61,"agent->customer","It's the graphics card. Bye",[-1]),

      (62,"supervisor->agent","It's his own fault, because his graphics card is configured wrong.",[63]),
      (63,"agent->supervisor","But it can be a hardware problem as well.",[64]),
      (64,"supervisor->agent","No it's not. The customer has no idea in which position the jumper is.",[65]),
      (65,"agent->customer","Perhaps the DIP switch is in the wrong position, bye.",[-1]),

      (66,"customer->agent","The server is offline, help.",[67,83]),
      (67,"agent->customer","Please hold.",[68,75,93]),
      (68,"agent->supervisor","Hi, what is going on?",[69]),
      (69,"supervisor->agent","Nothing special, I'm trying to search for something.",[70]),
      (70,"agent->supervisor","The server of a customer is down.",[71]),
      (71,"supervisor->agent","Ops, it was my fault. The new Apache config file has produced an error message.",[72]),
      (72,"agent->supervisor","How long does it take to fix it?",[73]),
      (73,"supervisor->agent","One hour, maybe longer.",[74]),
      (74,"agent->customer","The server will be online soon. Bye.",[-1]),
      
      (75,"agent->supervisor","Can you open a new ticket, please?",[76]),
      (76,"supervisor->agent","What is the problem?",[77]),
      (77,"agent->supervisor","The server of a customer is offline.",[78]),
      (78,"supervisor->agent","He should reboot it with the console.",[79]),
      (79,"agent->supervisor","First, you want to explain that's the fault of the customer? Secondly, please give me the ticket number.",[80]),
      (80,"supervisor->agent","The id is 123, and i will take a look at the problem.",[81]),
      (81,"agent->supervisor","Thank you",[82]),
      (82,"agent->customer","The ticket id is 123, an expert is fixing the problem right now.",[-1]),
      
      (83,"agent->customer","Which one?",[84]),
      (84,"customer->agent","There is only one server, the ID is 123.",[85]),
      (85,"agent->customer","What have you done so far to fix the problem?",[86]),
      (86,"customer->agent","I have tried to turn it on and off, and i have installed all the software updates.",[87]),
      (87,"agent->customer","Are you familiar with the config file of the Apache webserver?",[88]),
      (88,"customer->agent","No, I'm not. Do you think that the problem is located there?",[89]),
      (89,"agent->customer","This has to be investigated next. Please open the file and tell me which php modules are loaded.",[90]),
      (90,"customer->agent","I don't know, where the init file is located, can i call you back?",[91]),
      (91,"agent->customer","It's stored at /etc/httpd. Please check the loaded php modules and call me back if you are finished.",[92]),
      (92,"customer->agent","Sounds great, Thank you for your help, bye.",[-1]),
      
      (93,"agent->supervisor","The server of a customer is down.",[94]),
      (94,"supervisor->agent","Please fix it according to the manual.",[95]),
      (95,"agent->supervisor","First, I'd like to ask for your opinion.",[96]),
      (96,"supervisor->agent","I trust you, you are an experienced agent and can bring the server online without my help.",[97]),
      (97,"agent->supervisor","Thanks for the help.",[98]),
      (98,"agent->customer","Can you provide more information about the server problem?",[99]),
      (99,"customer->agent","After rebooting the virtual machine, a message is shown, that the webserver can't be initalized.",[100]),
      (100,"agent->customer","Sounds interesting, i will create a ticket, one moment please.",[101]),
      (101,"agent->customer","Hi, I'm done with the ticket. Right now, i can't fix the issue. Bye.",[-1]),

      (102,'agent->supervisor',"The customer has a broken monitor, i will create a ticket in the issue tracker.",[103]),
      (103,"supervisor->agent","It's correct, go ahead",[104]),
      (104,'agent->supervisor',"The issue can be fixed, by providing a new monitor.",[105]),
      (105,"supervisor->agent","Hm",[106]),
      (106,'agent->supervisor',"I have to open a second tab for activating the workflow.",[107]),
      (107,'agent->supervisor',"And now i can enter the adress of the customer.",[108]),
      (108,"supervisor->agent","Go ahead",[109]),
      (109,'agent->customer',"Thanks for waiting, a technican will visit you and will install a new monitor. Bye.",[110]),
      (110,'customer->agent',"Thank you very much.",[-1]),
    ]
    self.pos=0
    self.cost=0
    self.poslog=[]
  def getmessage(self):
    self.cost+=self.getcost(self.pos)
    if self.pos==-1: 
      message="END, total cost="+str(self.cost)+"ct \n"
    else:
      self.poslog.append(self.pos)
      message=self.speech[self.pos][1]+": "+self.speech[self.pos][2]+"\n"
      nodelist=self.speech[self.pos][3]
      self.pos=random.choice(nodelist)
    return message
  def getcost(self,speechid):
    # 5ct for agent speech, 15ct for supervisor speech
    if "supervisor" in self.speech[speechid][1]:
      result=15
    else: result=5
    return result
  def reset(self):
    self.pos=0
    self.cost=0
    self.poslog=[]


class GUI:
  def __init__(self):
    self.fps=10 # 20
    self.myphysics = Physics()
    # tkinter
    self.tkwindow = tkinter.Tk()
    self.tkwindow.title("Helpdesk game")
    self.tkwindow.geometry("500x270+600+0") # place to right
    self.tkwindow.bind("<Key>", self.inputhandling)
    # tkinter form
    self.widgetinfo = tkinter.Label(self.tkwindow, text="info",justify="left", wraplength=500)
    self.widgetinfo.place(x=10, y=0)    
    self.widgetmessage = ScrolledText(self.tkwindow, width=65, height=9, wrap="word")    
    self.widgetmessage.place(x=10, y=50)
    self.buttonnext = tkinter.Button(self.tkwindow,text="next",command=self.action)
    self.buttonnext.place(x=10, y=220)
    self.buttonreset = tkinter.Button(self.tkwindow,text="reset",command=self.reset)
    self.buttonreset.place(x=80, y=220) 
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
    result+="\nhistory "+str(self.myphysics.poslog)
    self.widgetinfo.config(text=result)  
  def inputhandling(self,event):
    if event.keysym=="Right": pass
  def reset(self):
    self.widgetmessage.delete('1.0', tkinter.END)
    self.myphysics.reset()
    self.action()
  def action(self):
    # message
    msg=self.myphysics.getmessage()
    self.widgetmessage.insert(tkinter.END,msg)
    self.widgetmessage.see(tkinter.END) # scroll to end

      
class Game():
  def __init__(self):
    self.mygui = GUI()
    self.mygui.tkwindow.mainloop()

mygame=Game()

