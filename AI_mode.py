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
from Algorithm import game , ai_game


class AI(tk.Label):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.game = ai_game.AIGame('w', 'b',2)
        self.master = master  
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
        self.board = Board(self)
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
    
    def winning_messege(self ,message):
        top = Toplevel()
        top.title("winning")
        top.geometry("400x200")  # Set the size of the window

        message = tk.Label(top, text = f"{message} \n do you want to play another game or return to start menu?")
        message.pack()

        button_frame = tk.Frame(top)
        button_frame.pack(side=tk.BOTTOM, pady=10)  # Place the frame at the bottom of the window

        buttons = []
        self.replay_image = Image.open("assets\\replay.png")
        self.replay_image = self.replay_image.resize((150,90))
        self.replay_image = ImageTk.PhotoImage(image=self.replay_image)
        replay = tk.Button(button_frame, image=self.replay_image, command=lambda : [self.master.switch_frame(AI) , top.destroy()],highlightthickness=0 , borderwidth=0)
        replay.pack(side=tk.LEFT, padx=10)  # Add horizontal padding between buttons
        buttons.append(replay)

        self.top_menu_image = Image.open("assets\\start-button.png")
        self.top_menu_image = self.top_menu_image.resize((150,100))
        self.top_menu_image = ImageTk.PhotoImage(image=self.top_menu_image)
        top_menu = tk.Button(button_frame, image=self.top_menu_image, command=lambda : [self.master.switch_frame(start.StartPage),top.destroy()],highlightthickness=0 , borderwidth=0)
        top_menu.pack(side=tk.LEFT, padx=10)  # Add horizontal padding between buttons
        buttons.append(top_menu)
