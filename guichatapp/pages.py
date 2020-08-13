from tkinter import *
from tkinter.scrolledtext import ScrolledText


class MainPage(Frame):

    def server(mainP):     
        print(mainP.appL)

    def client(mainP):
        print(mainP)



    def __init__(self,root):
        Frame.__init__(self,root)
        self.config(bg='dark grey')
        self.pack(fill=BOTH,expand=1)
        
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
    def start(page):
        print(page)

    def __init__(self,root):
        Frame.__init__(self,root)
        self.config(bg='dark grey')
        self.pack(fill=BOTH,expand=1)
        
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

        self.ngRb=Radiobutton(self.f2,text='Ngrok',font='arial 14')
        self.ngRb.pack(side=TOP,padx=5)
        
        self.authL=Label(self.f2,text='Authtoken: ',font='arial 14')
        self.authL.pack(side=LEFT,padx=5,pady=20)
        
        self.authB=Entry(self.f2,font='arial 14',width=40,highlightbackground='black')
        self.authB.pack(side=LEFT,padx=5,pady=20)

        self.f3=Frame(self)
        self.f3.pack(pady=40)

        self.startB=Button(self.f3,text='Start',font='helvetica 18',width=20,bg='light blue',fg='green',highlightbackground='red',command=self.start)
        self.startB.pack(pady=30,ipadx=10,ipady=10)

class ClientPage(Frame):
    def start(page):
        print(page)

    def __init__(self,root):
        Frame.__init__(self,root)
        self.config(bg='dark grey')
        self.pack(fill=BOTH,expand=1)
        
        self.appL=Label(self, bg = 'yellow', fg='green', font='helvetica 20',text='GUI CHAT APP',width=32, relief=RAISED)
        self.appL.pack(fill=X)

        self.f1=Frame(self)
        self.f1.pack(pady=40)
        
        self.authL=Label(self.f1,text='Connection link: ',font='arial 14')
        self.authL.pack(side=LEFT,padx=5,pady=20)
        
        self.authB=Entry(self.f1,font='arial 14',width=40,highlightbackground='black')
        self.authB.pack(side=LEFT,padx=5,pady=20)

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
    def __init__(self,root):
        Frame.__init__(self,root)
        self.pack()

        self.appL=Label(self, bg = 'yellow', fg='green', font='helvetica 20',text='GUI CHAT APP', relief=RAISED)
        self.appL.pack(fill=X)

        sname = StringVar()
        self.splate=Label(self, bg = 'green', fg= 'blue', font='helvetica 18',textvariable=sname, relief=SOLID)
        self.splate.pack(fill=X)
        sname.set('You: '+'Deshdeepak')

        oname = StringVar()
        self.oplate=Label(self, bg = 'green', fg= 'blue', font='helvetica 18',textvariable=oname, relief=SOLID)
        self.oplate.pack(fill=X)
        oname.set('Friend: '+'Shubham')

        self.chat=ScrolledText(self,state=DISABLED,height=27,font='arial 12')
        self.chat.pack(fill=X)

        self.chat.tag_config('left',justify='left',foreground='blue')
        self.chat.tag_config('right',justify='right',foreground='green')

        self.msgB=Entry(self,font='helvetica 14')
        self.msgB.pack(expand=True,fill=BOTH,side=LEFT)

        self.sendB=Button(self,text='>',font='helvetica 16',bg='light green')
        self.sendB.pack(fill=BOTH,side=RIGHT)

        self.chat.config(state=NORMAL)
        for i in range(50): 
            self.chat.insert(END,'RMessage'*3+'\n','left')
            self.chat.insert(END,'SMessage'*4+'\n','right')
        self.chat.config(state=DISABLED)
        self.chat.see(END)
        
