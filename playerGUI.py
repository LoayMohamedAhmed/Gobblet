import button_image as b
from pieces import Piece
import copy
class PlayerGUI():
    def __init__(self, root , img_player , player_type , pos ):
        self.pieces = [Piece(img_player,(42,42) , player_type ) , Piece(img_player, (84,84) , player_type) ,Piece(img_player,(128,128) , player_type) , Piece(img_player,(150,150) , player_type)]
        self.s = [copy.copy(self.pieces),copy.copy(self.pieces),copy.copy(self.pieces)]
        self.stack1 = b.ImageButton(root , Pieces= self.s[0] ,pos=pos[0],event=lambda: print(f"player {player_type}"),Btype="player", index=(0,-1))
        self.stack2 = b.ImageButton(root , Pieces= self.s[1] ,pos=pos[1],event=lambda: print(f"player {player_type}"),Btype="player", index=(1,-1))
        self.stack3 = b.ImageButton(root , Pieces= self.s[2] ,pos=pos[2],event=lambda: print(f"player {player_type}"),Btype="player", index=(2,-1))
        self.pl_pieces = [self.stack1 , self.stack2 , self.stack3]
    
