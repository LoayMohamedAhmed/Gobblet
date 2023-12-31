from game import Game
from evaluate_score import Evaluation
import copy
from player import Player

class AIGame(Game):
    # assume a_i always player_1
    def __init__(self, player1_color: str, player2_color: str, depth: int):
        super().__init__(player1_color, player2_color)
        self.depth = depth
        self.evaluate = Evaluation(self.player1, self.player2, self.board)

    def play(self):
        self.show_board_player()
        while True:
            if self.current_player is self.player1:
                temp_depth = self.depth

                score = minimax_alpha_beta_pruning(self=self,temp_depth= temp_depth, is_maximizing=True, first_time=True, alpha=float('-inf'), beta=float('inf'))
 
                self.switch_player()
                self.show_board_player()
                continue

            self.available_click()

            self.show_check_board_player()

            if self.play_turn():
                break
            
            self.show_board_player()
            # == check values in object
            # is check same address in memory
            self.player1.win = self.board.check_winning(self.player1.color)
            self.player2.win = self.board.check_winning(self.player2.color)

            # if two players win --> we consider the player who play prevois step is the winner ,not current player
            if(self.current_player is self.player1):
                if self.player2.win :
                    print(f"Player {self.player2.color} wins!")
                    break
                elif self.player1.win:
                    print(f"Player {self.player1.color} wins!")
                    break
            else :
                if self.player1.win:
                    print(f"Player {self.player1.color} wins!")
                    break
                elif self.player2.win :
                    print(f"Player {self.player2.color} wins!")
                    break
        
            self.switch_player()
            self.current_player.warn = self.board.check_warning(c=self.current_player.color,warning_list=self.current_player.warning_list)

    def get_available_AI_move_board(self, player :Player):
        available_gobblets = []

        for i in range(4):
            for j in range(4):
                if self.board.stacks[i][j].getSize() != 0 and self.board.stacks[i][j].top().color == player.color:
                    temp_pair = (i, j)
                    available_gobblets.append(temp_pair)

        return available_gobblets
 
    def get_available_AI_move_stack(self, player :Player):
        # make a bool list with size => 4 to check if the size if choosen before or not 
        available_gobblets = []
        taken_before = [False] * 4

        for i in range(3):
            if player.stacks[i].getSize() != 0:
                if not taken_before[player.stacks[i].top().length - 1]:
                    available_gobblets.append(i)
                    taken_before[player.stacks[i].top().length - 1] = True

        return available_gobblets

def minimax_alpha_beta_pruning(self,temp_depth: int, is_maximizing: bool, first_time: bool, alpha: float, beta: float) -> float:


    if temp_depth == 0 or self.board.check_winning(self.player1.color) or self.board.check_winning(self.player2.color) :
        return self.evaluate.evaluate_board()
    
    final_score = 0.0
    cut_off = False

    if is_maximizing:
        final_score = float('-inf')
        #final_to_i, final_to_j, final_frm_i, final_frm_j = 0, 0, 0, 5

        # make a fun to return (index pair<i ,j>) number a available gobblet in board and out
        available_gobblets_frm_board = self.get_available_AI_move_board(self.player1)
        available_gobblets_frm_stack = self.get_available_AI_move_stack(self.player1)

        # make two for loop, first to iterate on move_board, second move_stack
        for x in range(len(available_gobblets_frm_board)):
            if cut_off:
                break
            temp_pair = available_gobblets_frm_board[x]
            temp_length = self.board.stacks[temp_pair[0]][temp_pair[1]].top().length

            if not self.board.suggest_cells_case_1(temp_length):
                break

 
            temp_board_flags = copy.deepcopy(self.board.flags)
            for i in range(4):
                if cut_off:
                    break
                for j in range(4):
                    if temp_board_flags[i][j] == True:
                        temp_gobblet = self.board.stacks[temp_pair[0]][temp_pair[1]].top()
                        self.board.stacks[temp_pair[0]][temp_pair[1]].pop()
                        self.board.stacks[i][j].push(temp_gobblet)

                        score = minimax_alpha_beta_pruning(self = self, temp_depth = temp_depth - 1, is_maximizing = False, first_time = False,alpha= alpha, beta=beta)

                        self.board.stacks[i][j].pop()
                        self.board.stacks[temp_pair[0]][temp_pair[1]].push(temp_gobblet)

                        if score > final_score:
                            final_score = score
                            final_frm_i, final_frm_j = temp_pair[0], temp_pair[1]
                            final_to_i, final_to_j = i, j

                        alpha = max(alpha, final_score)

                        if first_time:
                            print(f"score from  board ({temp_pair[0]},{temp_pair[1]}), to board ({i},{j}), with score: {score}")

                        if beta <= alpha:
                            cut_off = True
                            break

        self.player1.warn = self.board.check_warning(self.player1.color, self.player1.warning_list)

        for x in range(len(available_gobblets_frm_stack)):
            if cut_off:
                break
            temp_length = self.player1.stacks[available_gobblets_frm_stack[x]].top().length

            if self.player1.warn:
                if not self.board.suggest_cells_case_21(temp_length, self.player1.warning_list):
                    break
            else:
                if not self.board.suggest_cells_case_20(temp_length):
                    break

            temp_board_flags = copy.deepcopy(self.board.flags)
            for i in range(4):
                if cut_off:
                    break
                for j in range(4):
                    if temp_board_flags[i][j] == True:
                        temp_gobblet = self.player1.stacks[available_gobblets_frm_stack[x]].top()
                        self.player1.stacks[available_gobblets_frm_stack[x]].pop()
                        self.board.stacks[i][j].push(temp_gobblet)

                        score = minimax_alpha_beta_pruning(self = self, temp_depth = temp_depth - 1, is_maximizing = False, first_time = False,alpha= alpha, beta=beta)

                        self.board.stacks[i][j].pop()
                        self.player1.stacks[available_gobblets_frm_stack[x]].push(temp_gobblet)

                        if score > final_score:
                            final_score = score # use it as a flag to know if it get from out ir board
                            final_frm_i, final_frm_j = available_gobblets_frm_stack[x], 6
                            final_to_i, final_to_j = i, j

                        alpha = max(alpha, final_score)

                        if first_time:
                            print(f"score from  out ( {available_gobblets_frm_stack[x]} ), to board ({i},{j}), with score: {score}")

                        if beta <= alpha:
                            cut_off = True
                            break

        if first_time:
            print(f"final score is {final_score}")
            if final_frm_j == 6:
                print("from outer")
                print(f"score from  out ( {final_frm_i} ), to board ({final_to_i},{final_to_j}), with final Score: {final_score}")
                temp_gobblet = self.player1.stacks[final_frm_i].top()
                self.player1.stacks[final_frm_i].pop()
                self.board.stacks[final_to_i][final_to_j].push(temp_gobblet)
            else:
                print("from inner")
                print(f"score from  board ({final_frm_i},{final_frm_j}), to board ({final_to_i},{final_to_j}), with final Score: {final_score}")
                temp_gobblet = self.board.stacks[final_frm_i][final_frm_j].top()
                self.board.stacks[final_frm_i][final_frm_j].pop()
                self.board.stacks[final_to_i][final_to_j].push(temp_gobblet)
            print("\n\n")

    else:  # isMinimizing

        final_score = float('inf')
        #final_to_i, final_to_j, final_frm_i, final_frm_j = 0, 0, 0, 5

        available_gobblets_frm_board = self.get_available_AI_move_board(self.player2)
        available_gobblets_frm_stack = self.get_available_AI_move_stack(self.player2)

        # make two for loop, first to iterate on move_board, second move_stack
        for x in range(len(available_gobblets_frm_board)):
            if cut_off:
                break
            temp_pair = available_gobblets_frm_board[x]
            temp_length = self.board.stacks[temp_pair[0]][temp_pair[1]].top().length

            if not self.board.suggest_cells_case_1(temp_length):
                break

            temp_board_flags = copy.deepcopy(self.board.flags)
            for i in range(4):
                if cut_off:
                    break
                for j in range(4):
                    if temp_board_flags[i][j] == True:
                        temp_gobblet = self.board.stacks[temp_pair[0]][temp_pair[1]].top()
                        self.board.stacks[temp_pair[0]][temp_pair[1]].pop()
                        self.board.stacks[i][j].push(temp_gobblet)

                        score = minimax_alpha_beta_pruning(self = self, temp_depth = temp_depth - 1, is_maximizing = True, first_time = False,alpha= alpha, beta=beta)
                        
                        self.board.stacks[i][j].pop()
                        self.board.stacks[temp_pair[0]][temp_pair[1]].push(temp_gobblet)

                        if score < final_score:
                            final_score = score
                            final_frm_i, final_frm_j = temp_pair[0], temp_pair[1]
                            final_to_i, final_to_j = i, j

                        beta = min(beta, final_score)

                        if beta <= alpha:
                            cut_off = True
                            break

        self.player2.warn = self.board.check_warning(self.player2.color, self.player2.warning_list)


        for x in range(len(available_gobblets_frm_stack)):
            if cut_off:
                break
            temp_length = self.player2.stacks[available_gobblets_frm_stack[x]].top().length

            if self.player2.warn:
                if not self.board.suggest_cells_case_21(temp_length, self.player2.warning_list):
                    break
            else:
                if not self.board.suggest_cells_case_20(temp_length):
                    break

            temp_board_flags = copy.deepcopy(self.board.flags)
            for i in range(4):
                if cut_off:
                    break
                for j in range(4):
                    if temp_board_flags[i][j] == True:
                        temp_gobblet = self.player2.stacks[available_gobblets_frm_stack[x]].top()
                        self.player2.stacks[available_gobblets_frm_stack[x]].pop()
                        self.board.stacks[i][j].push(temp_gobblet)

                        score = minimax_alpha_beta_pruning(self = self, temp_depth = temp_depth - 1, is_maximizing = True, first_time = False,alpha= alpha, beta=beta)
                        
                        self.board.stacks[i][j].pop()
                        self.player2.stacks[available_gobblets_frm_stack[x]].push(temp_gobblet)

                        if score < final_score:
                            final_score = score
                            final_frm_i, final_frm_j = available_gobblets_frm_stack[x], 6
                            final_to_i, final_to_j = i, j

                        beta = min(beta, final_score)

                        if beta <= alpha:
                            cut_off = True
                            break

    return final_score
