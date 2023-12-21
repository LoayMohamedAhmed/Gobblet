from button_image import ImageButton
from pieces import Piece
import copy

class Board():
    def __init__(self, root, page):
        self.page = page
        self.board =[]
        self.small_square_size =175
        self.pieces = [Piece("assets/blue.jpg",(140,150) , -1)]
        for i in range(4):
            for j in range(4):
                self.board.append(ImageButton(root , Pieces= copy.copy(self.pieces) ,pos=((400+j * self.small_square_size + self.small_square_size / 2 )/1500, (50+i * self.small_square_size + self.small_square_size / 2)/800),event=self.clickFunction, page=self.page))
    def clickFunction(self, event=None):
        selected_piece = self.page.get_selected_piece()  # Get the selected piece from the PageOne class
        print(selected_piece)
        if selected_piece:
            self.pieces.append(selected_piece)  
            self.page.clear_selected_piece()  
        self.func()