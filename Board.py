from button_image import ImageButton
from pieces import Piece
import copy

class Board():
    def __init__(self, root):
        self.board =[]
        self.small_square_size =175
        self.pieces = [Piece("assets/gray.jpg",(150,150) , -1)]
        for i in range(4):
            for j in range(4):
                self.board.append(ImageButton(root , Pieces= copy.copy(self.pieces) ,pos=((400+j * self.small_square_size + self.small_square_size / 2 )/1500, (50+i * self.small_square_size + self.small_square_size / 2)/800),event=lambda: print(f"played"),Btype="board"))
