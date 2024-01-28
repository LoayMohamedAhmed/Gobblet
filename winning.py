import tkinter as tk
import button
import image_label
import start
class winninig(tk.Frame):
    def __init__(self, master, number , img):
        tk.Frame.__init__(self, master)
        self.background1 = image_label.ImageLabel(self, image_path="assets\\gray.jpg", size=(1500,800), position=(0.5,0.5))
        self.background2 = image_label.ImageLabel(self, image_path=img, size=(200,300), position=(0.5,0.45))
        self.message = tk.Label(self, text = f"player {number} won!", font=("Arial", 20))
        self.message.place(relx=0.5, rely= 0.2 , anchor="center") 
        self.top_menue = self.bt=button.button1(self,"assets\\back.png",(0.5,0.7),event=lambda: master.switch_frame(start.StartPage),size=(75,75))


