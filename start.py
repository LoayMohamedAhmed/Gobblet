from tkinter import *
from button import button1
from PIL import  Image , ImageTk
from hVSh import*
from AI_mode import *
from image_label import ImageLabel
from AIvsAI import AIvsAI
import game_sittings
class StartPage(tk.Frame):
    def __init__(self, master):
            tk.Frame.__init__(self, master)   
            self.background1 = ImageLabel(self,image_path="assets\\gray.jpg",size=(1500,800),position=(0.5,0.5)) 
            self.background1 = ImageLabel(self,image_path="assets\\goblet.png",size=(600,250),position=(0.5,0.3)) 
            self.bt=button1(self,"assets\\button2.png",(0.5,0.6),event=lambda: master.switch_frame(game_sittings.sitting),size=(150,100))


