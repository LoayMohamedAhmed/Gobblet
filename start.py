from tkinter import *
from button import button1
from PIL import  Image , ImageTk
from pageone import*
from image_label import ImageLabel
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)   
        self.background1 = ImageLabel(self,image_path="assets\\python.jpg",size=(1500,800),position=(0,0)) 
        self.background1.label.pack()
        self.bt=button1(self,"assets\\start-button.png",(0.5,0.84),event=lambda: master.switch_frame(PageOne))
        self.bt.create_button()


