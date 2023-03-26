from tkinter import *

from PIL import Image,ImageTk
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
mixer.init()

class musicplayer:
    def __init__(self, Tk, ):
        self.root=Tk
        self.root.title('Music_Player')
        self.root.geometry("400x600")
        self.root.configure(background='White')

        self.photo=ImageTk.PhotoImage(file='bg.jpg')
        photo=Label(self.root,image=self.photo).place(width=350,height=350,y=30,x=25)

        self.label1=Label(self.root,text="Lets play ",bg="black",fg="white")
        self.label1.pack(side=BOTTOM,fill=X)

        def openfile():
            global filename
            filename=filedialog.askopenfilename()

        self.menubar=Menu(self.root)
        self.root.configure(menu=self.menubar)

        self.submenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='File',menu=self.submenu)
        self.submenu.add_command(label='Open',command=openfile)

        self.submenu1 = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Help', menu=self.submenu1)
        self.submenu1.add_command(label='About')


        def playm():
            try:
                paused

            except NameError:
                try:
                    mixer.music.load('filename')
                    mixer.music.play()
                    self.label1['text'] = "music playing"
                except:
                    passs
            else:
                mixer.music.unpause()
                self.label1['text']='music_unpaused'
        def stopm():
            mixer.music.stop()
            self.label1['text']="music stoped"

        def pause():
            global paused
            paused=TRUE
            mixer.music.play()
            self.label1['text'] = "music paused"

        self.photo1 = ImageTk.PhotoImage(file='new1.png')
        photo1= Button(self.root, image=self.photo1,bd=0,bg="black",command=playm).place(x=150, y=450,height=50,width=50)

        self.photo2 = ImageTk.PhotoImage(file='play.png')
        photo2 = Button(self.root, image=self.photo2, bd=0, bg="white",command=stopm).place(x=50, y=450, height=50, width=50)
        self.photo3 = ImageTk.PhotoImage(file='pause1.jpg')
        photo3 = Button(self.root, image=self.photo3, bd=0, bg="blue",command=pause).place(x=240, y=450, height=50, width=60)

        def volume(vol):
            volume=int(vol)%100
            mixer.music.set_volume(volume)


        self.volimg=ImageTk.PhotoImage(file='vm1.jpg')
        volimg=Button(self.root,image=self.volimg).place(x=100,y=520,height=40,width=40)
        self.scale=Scale(self.root,from_=0,to=100,orient=HORIZONTAL,bg='gray',length=120,command=volume)
        self.scale.place(x=140,y=520)
root=Tk()
obj=musicplayer(root)
root.mainloop()