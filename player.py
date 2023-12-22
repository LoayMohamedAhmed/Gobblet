from button_image import ImageButton
from pieces import Piece
import copy
class Player():
    def __init__(self, root , img_player , player_type , pos ):
        self.pieces = [Piece(img_player,(42,42) , player_type ) , Piece(img_player, (84,84) , player_type) ,Piece(img_player,(128,128) , player_type) , Piece(img_player,(150,150) , player_type)]
        self.s = [copy.copy(self.pieces),copy.copy(self.pieces),copy.copy(self.pieces)]
        self.stack1 = ImageButton(root , Pieces= self.s[0] ,pos=pos[0],event=lambda: print(f"player {player_type}"),Btype="player")
        self.stack2 = ImageButton(root , Pieces= self.s[1] ,pos=pos[1],event=lambda: print(f"player {player_type}"),Btype="player")
        self.stack3 = ImageButton(root , Pieces= self.s[2] ,pos=pos[2],event=lambda: print(f"player {player_type}"),Btype="player")
    
    
