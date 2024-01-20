
class Piece():
    
    def __init__(self, image , size , player , last = False, pre_image = None):
        self.player = player
        self.image_path = image
        self.piece_size = size
        self.last = last
        self.image = pre_image
    
