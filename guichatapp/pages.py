import os
try:
    from tkinter import *
except:
    os.system('sudo apt-get install python3-tk')
    os.system('apt-get install python-tkinter')
    from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from .ngrok import Ngrok
import socket
from threading import Thread
from time import sleep

port =9999
host='localhost'
sname=''
oname=''

def br(msg):
    txts=msg.split()
    l=['']
    i=0
    for txt in txts:
        if len(l[i]+txt+' ')<=30:
            l[i]+=txt+' '
        else:
            i+=1
            l.append('')
            l[i]=txt+' '
    return '\n'.join(l)+'\n'



class MainPage(Frame):

    def server(self):     
        global sname
        sname=self.nameB.get()
        sName.set('You : '+sname)
        
        serverPage=ServerPage(self.master)
        self.destroy()
        serverPage.pack()

    def client(self):
        global sname
        sname=self.nameB.get()
        sName.set('You : '+sname)
        
        clientPage=ClientPage(self.master)
        self.destroy()
        clientPage.pack()

    def __init__(self,app):
        Frame.__init__(self,app)
        self.config(bg='dark grey')
        
        self.appL=Label(self, bg = 'yellow', fg='green', font='helvetica 20',text='GUI CHAT APP',width=32, relief=RAISED)
        self.appL.pack(fill=X)

        self.f1=Frame(self)
        self.f1.pack(pady=40)

        self.nameL=Label(self.f1,text='Name: ',font='veranda 12')
        self.nameL.pack(expand=True,side=LEFT)

        self.nameB=Entry(self.f1,font='veranda 12',width=40,highlightbackground='black')
        self.nameB.pack(expand=True,side=RIGHT)
       
        self.f2=Frame(self)
        self.f2.pack(pady=50)
       
        self.serverB=Button(self.f2,text='Server',font='helvetica 18',width=20,bg='yellow',fg='blue',highlightbackground='red',command=self.server)
        self.serverB.pack(side=TOP,pady=30,ipadx=10,ipady=10)
        
        self.clientB=Button(self.f2,text='Client',font='helvetica 18',width=20,bg='yellow',fg='blue',highlightbackground='red',command=self.client)
        self.clientB.pack(side=BOTTOM,pady=30,ipadx=10,ipady=10)
        
class ServerPage(Frame):

    def start(self):
        global port,sname,oname
        p=self.portB.get()
        if p!='':
            port=int(p)
        
        s=socket.socket()

        try:
            s.bind(('',port))
        except socket.error as e:
            messagebox.showerror('Error',e)
            return

        s.listen(1)

        if self.ngV.get():
            authtoken=self.authB.get()
            link=Ngrok(port,authtoken)
            self.conB.insert(END,link)
            self.conB.update()
        else:
            pass
        def serverStart(serverP):
            global c
            c,addr=s.accept()
            oname=c.recv(1024).decode()
            oName.set('Friend : '+oname)
            c.send(bytes(sname,'utf-8'))
            chatPage=ChatPage(serverP.master)
            serverP.destroy()
            chatPage.pack()
        sT=Thread(target=serverStart,args=(self,))
        sT.start()


    def ng(self):
        if self.ngV.get():
            self.authB.configure(state=NORMAL)  
        else:
            self.authB.configure(state=DISABLED)

    def __init__(self,app):
        Frame.__init__(self,app)
        self.config(bg='dark grey')
        
        self.appL=Label(self, bg = 'yellow', fg='green', font='helvetica 20',text='GUI CHAT APP',width=32, relief=RAISED)
        self.appL.pack(fill=X)

        self.f1=Frame(self)
        self.f1.pack(pady=40)

        self.portL=Label(self.f1,text='Port: ',font='veranda 12')
        self.portL.pack(side=LEFT,padx=10,ipadx=10)

        self.portB=Entry(self.f1,font='veranda 12',width=10,highlightbackground='black')
        self.portB.pack(side=RIGHT,padx=10)
        
        self.f2=Frame(self)
        self.f2.pack(pady=40)
        
        self.ngV=IntVar()
        self.ngV.set(1)
        self.ngCb=Checkbutton(self.f2,text='Ngrok',font='arial 14',command=self.ng,variable=self.ngV,offvalue=0,onvalue=1)
        self.ngCb.pack(side=TOP,padx=5)
        
        self.authL=Label(self.f2,text='Authtoken: ',font='arial 14')
        self.authL.pack(side=LEFT,padx=5,pady=20)
        
        self.authB=Entry(self.f2,font='arial 14',width=40,highlightbackground='black')
        self.authB.pack(side=LEFT,padx=5,pady=20)

        self.f3=Frame(self)
        self.f3.pack(pady=40)

        self.startB=Button(self.f3,text='Start',font='helvetica 18',width=20,bg='light blue',fg='green',highlightbackground='red',command=self.start)
        self.startB.pack(pady=30,ipadx=10,ipady=10)

        self.f4=Frame(self)
        self.f4.pack(pady=10)
        
        self.conL=Label(self.f4,text='Connection link: ',font='arial 14')
        self.conL.pack(side=LEFT,padx=5,pady=20)
        
        self.conB=Entry(self.f4,font='arial 14',width=40,highlightbackground='black')
        self.conB.pack(side=LEFT,padx=5,pady=20)

class ClientPage(Frame):
	
    def start(self):
        global host,port,sname,oname,c

        link=self.conB.get()
        
        if link=='':
            h=self.hostB.get()
            p=self.portB.get()
            if h!='':
                host=h
            if p !='':
            	port=int(p)
        else:
            hp=link.split('//')[1]
            host=hp.split(':')[0]
            port=int(hp.split(':')[1])
        
        c=socket.socket()
        
        def clientStart(clientP):
            c.connect((host,port))
            oname=c.recv(1024).decode()
            oName.set('Friend : '+oname)
            c.send(bytes(sname,'utf-8'))
            chatPage=ChatPage(clientP.master)
            clientP.destroy()
            chatPage.pack()

        cT=Thread(target=clientStart,args=(self,))
        cT.start()
        
    def __init__(self,app):
        Frame.__init__(self,app)
        self.config(bg='dark grey')
        
        self.appL=Label(self, bg = 'yellow', fg='green', font='helvetica 20',text='GUI CHAT APP',width=32, relief=RAISED)
        self.appL.pack(fill=X)

        self.f1=Frame(self)
        self.f1.pack(pady=40)
        
        self.conL=Label(self.f1,text='Connection link: ',font='arial 14')
        self.conL.pack(side=LEFT,padx=5,pady=20)
        
        self.conB=Entry(self.f1,font='arial 14',width=40,highlightbackground='black')
        self.conB.pack(side=LEFT,padx=5,pady=20)

        self.f2=Frame(self)
        self.f2.pack(pady=40)

        self.hostL=Label(self.f2,text='Host: ',font='veranda 12')
        self.hostL.pack(side=LEFT,padx=10,ipadx=10)

        self.hostB=Entry(self.f2,font='veranda 12',width=20,highlightbackground='black')
        self.hostB.pack(side=LEFT,padx=10)

        self.portL=Label(self.f2,text='Port: ',font='veranda 12')
        self.portL.pack(side=LEFT,padx=10,ipadx=10)

        self.portB=Entry(self.f2,font='veranda 12',width=10,highlightbackground='black')
        self.portB.pack(side=LEFT,padx=10)
         
        self.f3=Frame(self)
        self.f3.pack(pady=40)

        self.startB=Button(self.f3,text='Start',font='helvetica 18',width=20,bg='light blue',fg='green',highlightbackground='red',command=self.start)
        self.startB.pack(pady=30,ipadx=10,ipady=10)



class ChatPage(Frame):
    
    class Receiver(Thread):
        def __init__(self,chatPage):
            Thread.__init__(self)
            self.chatPage = chatPage
        def run(self):
            global c
            while True:
                msg=c.recv(1024).decode()
                self.chatPage.chat.config(state=NORMAL)
                self.chatPage.chat.insert(END,msg,'left')
                self.chatPage.chat.insert(END,'\n')
                self.chatPage.chat.config(state=DISABLED)
                self.chatPage.chat.see(END) 


    def sendMsg(*args):
        self=args[0]
        global c
        msg=self.msgB.get()
        self.msgB.delete(0,END)
        if msg !='':
            msg=br(msg)
            c.send(bytes(msg,'utf-8'))
            self.chat.config(state=NORMAL)
            self.chat.insert(END,msg,'right')
            self.chat.insert(END,'\n')
            self.chat.config(state=DISABLED)
            self.chat.see(END)


    def __init__(self,app):
        Frame.__init__(self,app)

        self.appL=Label(self, bg = 'yellow', fg='green', font='helvetica 20',text='GUI CHAT APP', relief=RAISED)
        self.appL.pack(fill=X)
        
        self.splate=Label(self, bg = 'green', fg= 'blue', font='helvetica 18',textvariable=sName, relief=SOLID)
        self.splate.pack(fill=X)

        self.oplate=Label(self, bg = 'green', fg= 'blue', font='helvetica 18',textvariable=oName, relief=SOLID)
        self.oplate.pack(fill=X)

        self.chat=ScrolledText(self,state=DISABLED,height=27,font='arial 12')
        self.chat.pack(fill=X)

        self.chat.tag_config('left',justify='left',foreground='blue',background='pink')
        self.chat.tag_config('right',justify='right',foreground='green',background='yellow')

        self.msgB=Entry(self,font='helvetica 14')
        self.msgB.bind('<Return>',self.sendMsg)
        self.msgB.pack(expand=True,fill=BOTH,side=LEFT)

        self.sendB=Button(self,text='>',font='helvetica 16',bg='light green',command=self.sendMsg)
        self.sendB.pack(fill=BOTH,side=RIGHT)
        
        self.receiver=self.Receiver(self)
        self.receiver.start()
        
class App(Tk):
	
	def __init__(self):
            
            Tk.__init__(self)
            self.title('Gui Chat App')
            self.geometry('525x650')
            self.resizable(0,0)
            self.config(bg='dark grey')

            mainPage=MainPage(self)
            mainPage.pack(fill=BOTH,expand=1)

            global sName,oName
            sName=StringVar() 
            oName=StringVar()
