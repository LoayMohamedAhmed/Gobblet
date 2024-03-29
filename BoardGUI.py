import button_image as b
from pieces import Piece
import copy
import tkinter as tk
from PIL import Image, ImageTk

class Board():
    def __init__(self, root):
        self.board =[]
        self.small_square_size =175
        self.image_path = "assets/gray.jpg"
        self.image_size = (150,150)
        self.image = Image.open(self.image_path)
        self.image = self.image.resize(self.image_size)
        self.image = ImageTk.PhotoImage(image=self.image)
        self.pieces = [Piece(self.image_path,(150,150) , -1 , True,self.image)]
        
        for i in range(4):
            self.temp =[]
            for j in range(4):
                newb=b.ImageButton(root , Pieces= copy.copy(self.pieces) ,pos=((400+j * self.small_square_size + self.small_square_size / 2 )/1500, (50+i * self.small_square_size + self.small_square_size / 2)/800),event=lambda: print(f"played"),Btype="board", index=(i,j))
                self.temp.append(newb)
                b.buttons_list.append(newb) # add board buttons to list
            self.board.append(self.temp)



    