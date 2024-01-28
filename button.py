from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

class button1():
    def __init__(self, root, image_path, pos, event, size):
        self.position = pos
        self.root = root
        self.func = event
        self.image_path = image_path
        self.size = size
        self.font = font.Font(size=20, family="Times")
        image = Image.open(image_path)
        image = image.resize(self.size)
        self.image = ImageTk.PhotoImage(image=image)
        self.create_button()

    def update_image(self, image_path):
        image = Image.open(image_path)
        image = image.resize(self.size)
        self.image = ImageTk.PhotoImage(image=image)
        self.bt.config(image=self.image)

    def create_button(self):
        self.bt = Button(self.root, image=self.image, borderwidth=0, background="black", command=self.func, highlightthickness=0)
        self.bt.config(activebackground="black")
        self.bt.place(relx=self.position[0], rely=self.position[1], anchor=CENTER)

    def destroy_button(self):
        self.bt.destroy()
