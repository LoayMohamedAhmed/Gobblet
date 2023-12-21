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
        self.player1 = Player(self , "assets\\X_large.png",1,[(0.95,0.2),(0.95,0.5),(0.95,0.8)], self)
        self.player2 = Player(self , "assets\\O_large.png",2,[(0.05,0.2),(0.05,0.5),(0.05,0.8)], self)
        self.board = Board(self, self)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(start.StartPage)).pack()
        self.selected_piece = None
        self.init_selected()
                  
    def init_selected(self):
            
        self.empty_image = Image.open("assets\\Empty.png")
        self.empty_image = self.empty_image.resize((100,100))  
        self.empty_image = ImageTk.PhotoImage(self.empty_image)

        
        self.text_label = tk.Label(self, text="Selected Piece: ")
        self.text_label.place(x=50, y=50)  

        
        self.image_label = tk.Label(self, image=self.empty_image)
        self.image_label.place(x=200, y=50)  
    def update_selected_piece(self, piece, image_path):
        print(piece.piece_size)
        print(self.extract_state())
        self.selected_piece = piece  # Set the selected piece
        image = Image.open(image_path)
        image = image.resize(piece.piece_size)  # Resize the image
        image = ImageTk.PhotoImage(image)
        self.image_label.config(image=image)
        self.image_label.image = image  # Keep a reference to the image



    def get_selected_piece(self):
        return self.selected_piece  # Add this line

    def clear_selected_piece(self):
        self.image_label.config(image=self.empty_image)
        self.selected_piece = None  # Clear the selected piece
        
    def set_selected_piece(self, piece):
        self.selected_piece = piece  # Set the selected piece
    
    def extract_state(self):
        state = {
            'board': [],
            'player1': [0, 0, 0, 0],
            'player2': [0, 0, 0, 0]
        }
        size_mapping = {
            (140,168): 3,
            (105,128): 2,
            (70,84): 1,
            (35,42): 0
        }
        # Extract info from the board
        for i in range(4):
            for j in range(4):
                button = self.board.board[i*4 + j]
                if button.pieces and button.pieces[-1].piece_size != (140,150):
                    cell_info = (button.pieces[-1].player, size_mapping.get(button.pieces[-1].piece_size, 'unknown'))
                    state['board'].append(cell_info)
                else:
                    state['board'].append(())

        # Extract info from the players
        for player in [self.player1, self.player2]:
            player_info = state[f'player{player.pieces[0].player}']
            for stack in [player.stack1, player.stack2, player.stack3]:
                if stack.pieces:
                    size_index = size_mapping.get(stack.pieces[-1].piece_size, 'unknown')
                    if size_index != 'unknown':
                        player_info[size_index] += 1

        return state
                  
        