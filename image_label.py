import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk


class ImageLabel():
    def __init__(self, root, image_path=None ,size = None , position =None):
        self.image_path = image_path
        self.image = Image.open(self.image_path).resize(size)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(root, image=self.photo, width=size[0], height=size[1],borderwidth=0,background="black")
        self.label.place(relx=position[0] , rely= position[1]  , anchor= CENTER)
        #self.label.pack()
        self.label.image = self.photo # <== this is where we anchor the img object

    def update_image(self, image_path , size):
        self.image_path = image_path
        self.image = Image.open(self.image_path).resize((size[0], size[1]))
        self.photo = ImageTk.PhotoImage(self.image)
        self.label.configure(image=self.photo)

