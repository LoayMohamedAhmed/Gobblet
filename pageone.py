import tkinter as tk
from tkinter import *
import start
from button import button1
from PIL import  Image , ImageTk
from button_image import *
from pieces import *
from playerGUI import PlayerGUI
from BoardGUI import Board
from image_label import ImageLabel
from Algorithm import game


class PageOne(tk.Label):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.game = game.Game('w', 'b')  
        self.selected_piece = None 
        self.player_turn = 0
        self.played = True
        self.out = None
        self.out_in = None
        self.from_i = None
        self.from_j = None
        self.to_i=None
        self.to_j=None
        self.ava_clicks=[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        self.background1 = ImageLabel(self,image_path="assets\\black.jpg",size=(1500,800),position=(0,0)) 
        self.background1.label.pack()
        self.board = ImageLabel(self,image_path="assets\\board1.png",size=(700,700),position=(0.5,0.5))
        self.player1 = PlayerGUI(self , "assets\\whiteL.png",0,[(0.95,0.2),(0.95,0.5),(0.95,0.8)])
        self.player2 = PlayerGUI(self , "assets\\blackL.png",1,[(0.05,0.2),(0.05,0.5),(0.05,0.8)])
        board = Board(self)
        self.show1 = ImageLabel(self,image_path="assets\\gray.jpg",size=(150,150), position= (0.8,0.5))
        self.show2 = ImageLabel(self,image_path="assets\\gray.jpg",size=(150,150), position= (0.2,0.5))
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(start.StartPage)).pack()
        
    def select_piece(self , piece):
        if piece != None:
            self.selected_piece = piece
            if piece.player == 0:
                self.show1.update_image(self.selected_piece.image_path , self.selected_piece.piece_size)
            else:
                self.show2.update_image(self.selected_piece.image_path , self.selected_piece.piece_size)
        else:
            
            self.show1.update_image("assets\\gray.jpg",(150,150))
            self.show2.update_image("assets\\gray.jpg",(150,150))

    
    def change_turn(self):
       self.player_turn = (self.player_turn + 1)%2 


    def chose(self):
        self.played = not self.played
    
