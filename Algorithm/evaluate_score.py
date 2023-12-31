from player import Player
from board import Board

class Evaluation:
    def __init__(self, a_i: Player, opponent_player: Player, board: Board):
        self.opponent_player = opponent_player
        self.a_i = a_i
        self.board = board


    def evaluate_board(self):
        if self.board.check_winning(self.a_i.color):
            return float('inf')
        if self.board.check_winning(self.opponent_player.color):
            return float('-inf')
        
        piece_count_weight = 1
        threat_weight = 3
        blocking_weight = 5

        ai_score = 0
        opponent_score = 0

        # Piece count
        ai_score += piece_count_weight * self.count_pieces(self.a_i.color)
        opponent_score += piece_count_weight * self.count_pieces(self.opponent_player.color)

        # Threats 
        ai_score += threat_weight * self.count_threats(self.opponent_player.color)
        opponent_score += threat_weight * self.count_threats(self.a_i.color)

        #  blocking
        ai_score += blocking_weight * self.count_blocks(self.a_i.color)
        opponent_score += blocking_weight * self.count_blocks(self.opponent_player.color)

        return ai_score - opponent_score
 
    # to give a score to the pieces on the board based on (number, size, postion)
    def count_pieces(self, player_color):
        result = 0

        for i in range(4):
            for j in range(4):
                if self.board.stacks[i][j].isEmpty():
                    continue
                
                if self.board.stacks[i][j].top().color == player_color :
                    if(i == 0 or i==3) and (j==0 or j ==3):
                        # handel corner
                        result += 2 * ( 0.25 * self.board.stacks[i][j].top().length)

                    elif (i == 0 or i==3) or (j==0 or j ==3):
                        # handel boundary
                        result += (0.25 * self.board.stacks[i][j].top().length)
                    
                    else:
                        # handle center
                        result += 2 * (0.25 * self.board.stacks[i][j].top().length)

        return result

    def count_threats( self, player_color):

        result = 0

        #check horizontally
        for i in range(4):
            count = 0
            for j in range(4):
                if self.board.stacks[i][j].isEmpty():
                    pass
                elif self.board.stacks[i][j].top().color != player_color:
                    count += 1
                else:
                    count -= 1

            if count == 3:
            
                result += 1

        #check vertically
        for i in range(4):
            count = 0
            for j in range(4):
                if self.board.stacks[j][i].isEmpty():
                    pass
                elif self.board.stacks[j][i].top().color != player_color:
                    count += 1
                else:
                    count -= 1

            if count == 3:
            
                result += 1

        # check top left diagonal
        count = 0
        for i in range(4):
            if self.board.stacks[i][i].isEmpty():
                pass
            elif self.board.stacks[i][i].top().color != player_color:
                count += 1
            else:
                count -= 1
        if count == 3:
            result += 1


        # check top right diagonal
        count = 0
        for i in range(4):

            j = 3 - i
            if self.board.stacks[i][j].isEmpty():
                pass
            elif self.board.stacks[i][j].top().color != player_color:
                count += 1
            else:
                count -= 1
        if count == 3:
            result += 1

        return result

    def count_blocks( self, player_color):

        result = 0
        count_p = 0
        count_o = 0
        #check horizontally
        for i in range(4):
            count_p = 0
            count_o = 0
            for j in range(4):
                if self.board.stacks[i][j].isEmpty():
                    break
                elif self.board.stacks[i][j].top().color != player_color:
                    count_p += 1
                else:
                    count_o += 1

            if count_o == 3 and count_p == 1:
                result += 1
                
        #check vertically
        for i in range(4):
            count_p = 0
            count_o = 0
            for j in range(4):
                if self.board.stacks[j][i].isEmpty():
                    break
                elif self.board.stacks[j][i].top().color != player_color:
                    count_p += 1
                else:
                    count_o += 1

            if count_o == 3 and count_p == 1:
                result += 1

        # check top left diagonal
        count_p = 0
        count_o = 0
        for i in range(4):
            if self.board.stacks[i][i].isEmpty():
                break
            elif self.board.stacks[i][i].top().color != player_color:
                count_p += 1
            else:
                count_o += 1
        if count_o == 3 and count_p == 1:
            result += 1


        # check top right diagonal
        count_p = 0
        count_o = 0
        for i in range(4):
            j = 3 - i
            if self.board.stacks[i][j].isEmpty():
                break
            elif self.board.stacks[i][j].top().color != player_color:
                count_p += 1
            else:
                count_o += 1
        if count_o == 3 and count_p == 1:
            result += 1

        return result

