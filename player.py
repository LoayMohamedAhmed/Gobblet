from button_image import ImageButton
from pieces import Piece
import copy
class Player():
    def __init__(self, root , img_player , player_type ,pos):
        self.pieces = [Piece(img_player,(35,42) , player_type) , Piece(img_player, (70,84) , player_type) ,Piece(img_player,(105,128) , player_type) , Piece(img_player,(140,168) , player_type)]
        self.stack1 = ImageButton(root , Pieces= copy.copy(self.pieces) ,pos=pos[0],event=lambda: print(f"player {player_type}"))
        self.stack2 = ImageButton(root , Pieces= copy.copy(self.pieces) ,pos=pos[1],event=lambda: print(f"player {player_type}"))
        self.stack3 = ImageButton(root , Pieces= copy.copy(self.pieces) ,pos=pos[2],event=lambda: print(f"player {player_type}"))