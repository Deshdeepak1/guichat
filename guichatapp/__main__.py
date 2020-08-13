from tkinter import *
from .pages import *
root=Tk()
root.title('Gui Chatapp')
root.geometry('525x650')
root.resizable(0,0)

#chatPage=ChatPage(root)
#mainPage=MainPage(root)
serverPage=ServerPage(root)
root.mainloop()

