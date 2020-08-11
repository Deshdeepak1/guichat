from tkinter import *

root=Tk()
root.title('Gui Chatapp')
root.geometry('700x720')
root.resizable(0,0)

scroll = Scrollbar(root)
scroll.pack(side = RIGHT,fill = Y)

text_area = Text(root,yscrollcommand = scroll.set,height=20,width=60,font='helvetica 15',bg='LightSkyBlue1',fg='gray17')
scroll.config(command=text_area.yview)
text_area.pack(expand=True, fill=BOTH)

root.mainloop()
