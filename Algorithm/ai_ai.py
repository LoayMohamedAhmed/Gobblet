from ai_game import AIGame

class Ai_Ai(AIGame):
    def __init__(self, depth_1: int, depth_2: int,):
        self.player1.color = 'w'
        self.player2.color = 'b'
    
    def get_player1_move(self):
        temp_depth_1 = self.depth_1
        return self.minimax_alpha_beta_pruning(self=self,temp_depth=temp_depth_1, is_maximizing=True, first_time=True, alpha=float('-inf'), beta=float('inf'),flag=True)
    

    def get_player2_move(self):
        temp_depth_2 = self.depth_2
        return self.minimax_alpha_beta_pruning(self=self,temp_depth=temp_depth_2, is_maximizing=True, first_time=True, alpha=float('-inf'), beta=float('inf'),flag=False)