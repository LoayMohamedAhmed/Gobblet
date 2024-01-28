from tkinter import *
from tkinter import font,messagebox
from PIL import Image, ImageTk
from pieces import Piece
import tkinter as tk
import random
from winning import winninig

#pip install pillow
#pip install future
buttons_list=[] #list for board buttons
def randomize_list_indexes(lst):
    indexes = list(range(len(lst)))
    random.shuffle(indexes)
    return [lst[i] for i in indexes]
class ImageButton(Button):
     def __init__(self, root, Pieces , pos, event , Btype, index=None):
        self.position = pos
        self.page = root
        self.pieces = Pieces
        self.root = root
        self.func = event
        self.Btype = Btype
        self.index = index
        self.font = font.Font(size=20, family="Times")
        self.image = Image.open(self.pieces[-1].image_path) if not self.pieces[-1].last else self.pieces[-1].image
        self.image = self.image.resize(self.pieces[-1].piece_size) if not self.pieces[-1].last else self.pieces[-1].image
        self.image = ImageTk.PhotoImage(image=self.image) if not self.pieces[-1].last else self.pieces[-1].image
        self.flag=True
        self.game = self.page.game # Refer to the existing game instance
        self.ai_coordinate = None # coordinate of ai game (from_x,from_y,to_X,to_Y)


        super().__init__(root, image=self.image, borderwidth=0, background="black", command=self.clickFunction, highlightthickness=0)
        self.config(activebackground="black")
        self.place(relx=self.position[0], rely=self.position[1], anchor=CENTER)

        self.toggleState = 1

     def clickFunction(self, event=None):
          
          
          


          # Call the appropriate methods of the game based on the user's actions
          if self.page.selected_piece != None and self.Btype == "board":
               # A piece is being moved to this location
               self.page.to_i, self.page.to_j = self.index
               #fX, fY, tX, tY = self.ai_coordinate
               #self.Ai_move(fX,fY,tX,tY)

               # Check if the position the player wants to play to is available
               if self.page.ava_clicks[self.page.to_i][self.page.to_j] == 1:
                    self.pieces.append(self.page.selected_piece)
                    self.page.selected_piece = None
                    self.page.chose()
                    self.page.select_piece(None)
                    self.enable_buttons()  # enable buttons again after disabling them

                    # Call game.play_turn_to() with the appropriate parameters
                    self.game.play_turn_to(self.page.to_i, self.page.to_j)
                    self.check_winner()

                         # Switch player in the game logic and update the GUI
                    self.game.switch_player()
                    self.page.change_turn()
                    self.game.current_player.warn = self.game.board.check_warning(c=self.game.current_player.color,warning_list=self.game.current_player.warning_list)
                    if self.page.mode == "AI_mode":
                                   self.ai_coordinate , _ = self.game.minimax_alpha_beta_pruning(3,True,True,float('-inf'),float('inf'),False)
                                   fX, fY, tX, tY = self.ai_coordinate
                                   self.Ai_move(fX,fY,tX,tY)
                                   self.game.switch_player()
                                   self.page.change_turn()
               else:
                    messagebox.showinfo("Error", "This position is not available. Please choose another position.")
          else: # this condition is responsible for selecting piece either from inside or outside the board
               if self.pieces:
                    self.current_piece = self.pieces[-1]
                    if self.current_piece.player == self.page.player_turn and self.page.played:
                         self.page.chose()
                         self.page.select_piece(self.pieces[-1]) 
                         self.pieces.pop()
                         #out_in-> If you want to choose gobblet from player 0. If from the board, press 1: 
                         #out ->index of gobblet stack player 
                         if self.Btype == "player":
                              print("Gobblet is choosen from player")
                              self.page.out = self.index[0]
                              self.page.out_in=0
                              self.page.from_i, self.page.from_j = self.index
                              win_flag,self.page.ava_clicks=self.game.play_turn_from(self.page.out, self.page.from_i, self.page.from_j, self.page.out_in)
                              # Call game.play_turn_from() with the appropriate parameters
                              #self.ai_coordinate , _ = self.game.minimax_alpha_beta_pruning(2,True,True,float('-inf'),float('inf'))
                              
                              if win_flag:
                                   self.check_winner()
                                   self.game.available_click()
                         else:
                              print("Gobblet is choosen from Board")
                              self.page.out=None
                              self.page.out_in=1
                              self.page.from_i, self.page.from_j =self.index
                              win_flag,self.page.ava_clicks=self.game.play_turn_from(self.page.out, self.page.from_i, self.page.from_j, self.page.out_in)
                              #new
                              
                              # Call game.play_turn_from() with the appropriate parameters
                              if win_flag:
                                   self.check_winner()
                                   self.game.available_click()
                         

               

               
          # This code explain game flow in ai algo
          # Update the game state after each action
          #game.available_click()
          #game.current_player.warn = game.board.check_warning(c=game.current_player.color,warning_list=game.current_player.warning_list)
          # game.player1.win = game.board.check_winning(game.player1.color)
          # game.player2.win = game.board.check_winning(game.player2.color)
         

          # Update the image
          self.change_image()
          self.game.player1.win = self.game.board.check_winning(self.game.player1.color)
          self.game.player2.win = self.game.board.check_winning(self.game.player2.color)
          
          # If a player wins, display a message box
          self.check_winner()

          print("------------------------------------------------------------")
     def stop(self):
          # Create a new window
          top = Toplevel()
          top.title("stop")
          top.geometry('%dx%d+%d+%d' % (500, 300,500,300))
          # Open the image file
          img = Image.open('assets\\stop.jpg')
          img = img.resize((500,300))
          # Convert the image file to a PhotoImage object
          img = ImageTk.PhotoImage(img)
          
          # Create a label with the image
          label = Label(top, image=img)
          label.image = img  # keep a reference!

          # Display the label
          label.pack()
     
     def disable_buttons(self, lst):
        one_d_list=[element for sublist in lst for element in sublist] #convert 2d list to 1d
        for i in range(len(one_d_list)):
            if one_d_list[i] == False:
                buttons_list[i].config(state=tk.DISABLED)
            else:
                print(buttons_list)
                buttons_list[i].config(state=tk.NORMAL)


     def enable_buttons(self):
          for i in range(len(buttons_list)):
            buttons_list[i].config(state=tk.NORMAL)
     
     def check_winner(self):
          self.game.player1.win = self.game.board.check_winning(self.game.player1.color)
          self.game.player2.win = self.game.board.check_winning(self.game.player2.color)
                                   
          # If a player wins, display a message box
          if self.game.player1.win:
               self.master.master.switch_to_winning(1, self.page.p1_img_dir if self.page.mode != "AI_VS_AI" else "assets\\robot1.png")
          elif self.game.player2.win:
               self.master.master.switch_to_winning(2, self.page.p2_img_dir if self.page.mode != "AI_VS_AI" else "assets\\robot2.png")


     def change_image(self):
          if self.pieces:
               self.image=self.pieces[-1].image_path
               self.size = self.pieces[-1].piece_size
               self.image = Image.open(self.image)
               self.image = self.image.resize(self.size)
               self.image = ImageTk.PhotoImage(image=self.image)
               self.config(image=self.image)
               self.func()  # Call the function passed in the 'event' parameter
          elif self.flag:
               self.image = Image.open("assets\\no more.png" if self.Btype =="player" else "assets\\gray.jpg")
               self.image = self.image.resize((150,150))
               self.image = ImageTk.PhotoImage(image=self.image)
               self.config(image=self.image)
               self.flag = False
          else:
               messagebox.showinfo("peaces", "you have selected all pices") if self.Btype =="player" else True
               self.stop() if self.Btype =="player" else True
     
     def Ai_move(self, from_x , from_y , to_x , to_y):
          if from_y==6:
             Piece = self.page.player2.pl_pieces[from_x].pieces.pop()
             self.page.player2.pl_pieces[from_x].change_image()
             self.page.board.board[to_x][to_y].pieces.append(Piece)
             self.page.board.board[to_x][to_y].change_image()
          else:
             Piece = self.page.board.board[from_x][from_y].pieces.pop()
             self.page.board.board[from_x][from_y].change_image()
             self.page.board.board[to_x][to_y].pieces.append(Piece)
             self.page.board.board[to_x][to_y].change_image()
     
          