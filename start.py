from tkinter import *
from button import button1
from PIL import  Image , ImageTk
from pageone import*
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)   
        self.background = Image.open("assets\python.jpg")
        self.background = self.background.resize((1500,900))
        self.background = ImageTk.PhotoImage(self.background) # Add this line
        label = Label(self ,image=self.background) # Change this line
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.bt=button1(self,"assets\\start-button.png",(0.5,0.84),event=lambda: master.switch_frame(PageOne))
        self.bt.create_button()


