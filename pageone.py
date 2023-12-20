import tkinter as tk
from tkinter import *
import start
from button import button1
from PIL import  Image , ImageTk
from button_image import *
from pieces import *
from player import Player
from Board import Board

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)   
        self.background1 = Image.open("assets\\black.jpg")
        self.background1 = self.background1.resize((1500,800))
        self.background1 = ImageTk.PhotoImage(self.background1) # Add this line
        label1 = Label(self ,image=self.background1) # Change this line
        label1.place(x=0, y=0, relwidth=1, relheight=1)
        self.board = Image.open("assets\\board.jpg")
        self.board = self.board.resize((700,700))
        self.board = ImageTk.PhotoImage(self.board) # Add this line
        label_board = Label(self ,image=self.board) # Change this line
        label_board.place(relx=0.5, rely=0.5,anchor=CENTER)
        player1 = Player(self , "assets\\X_large.png",1,[(0.95,0.2),(0.95,0.5),(0.95,0.8)])
        player2 = Player(self , "assets\\O_large.png",1,[(0.05,0.2),(0.05,0.5),(0.05,0.8)])
        board = Board(self)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(start.StartPage)).pack()
                  
        