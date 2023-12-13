from tkinter import*
from tkinter import font
from PIL import Image, ImageTk
class button1():
    def __init__(self,root, image_pth , pos , text , img_text, event):
        self.position = pos
        self.root=root
        self.text = text
        self.flag = img_text
        self.func = event
        self.image = Image.open(image_pth)
        self.image =self.image.resize((150,100))
        self.image = ImageTk.PhotoImage(image=self.image)
        self.font= font.Font(size=20,family="Times") 

    def create_button(self):
        bt = Button(self.root,image=self.image,borderwidth=0,background="black",command=self.func,highlightthickness=0)
        bt.config(activebackground="black",)
        bt.place(relx=self.position[0],rely=self.position[1],anchor=CENTER)