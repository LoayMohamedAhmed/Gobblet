from tkinter import *
from button import button1
from hVSh import*
from AI_mode import *
from AIvsAI import *
import start
import image_label
class winninig(tk.Frame):
    def __init__(self, master, mode , number , img):
        tk.Frame.__init__(self, master)  
        self.message = tk.Label(self, text = f"player {number}  won!")
        self.message.place(relx=0.5, rely= 0.2 , anchor="center" , font=("Arial", 40)) 
        self.background1 = image_label.ImageLabel(self, image_path="assets\\gray.jpg", size=(1500,800), position=(0.5,0.5))
        self.background1 = image_label.ImageLabel(self, image_path=img, size=(150,300), position=(0.5,0.5))
        self.play_again = self.bt=button1(self,"assets\\playB.png",(0.4,0.7),event=lambda: master.switch_frame(mode),size=(150,150))
        self.top_menue = self.bt=button1(self,"assets\\back.png",(0.3,0.7),event=lambda: master.switch_frame(start.StartPage),size=(150,150))
        


