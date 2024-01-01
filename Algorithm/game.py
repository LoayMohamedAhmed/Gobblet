from typing import List
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(1, os.path.join(parent_dir, 'Algorithm'))

from player import Player

from board import Board

class Game:
    def __init__(self, player1_color: str, player2_color: str):
        # Create two players with different colors
        self.player1 = Player(player1_color)
        self.player2 = Player(player2_color)
        

        # Set the current player to player1
        self.current_player = self.player1

        # Create the game board
        self.board = Board()

    def switch_player(self):
        # Switch the current player
        if self.current_player is self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def show_board_player(self):
        self.player1.show_player()
        self.player2.show_player()
        self.board.show_board()

    def show_check_board_player(self):
        self.player1.show_check_player()
        self.player2.show_check_player()
        self.board.show_check_board()

    def available_click(self):
        self.board.handle_click(c=self.current_player.color)
        self.player1.handle_clicks(c=self.current_player.color)
        self.player2.handle_clicks(c=self.current_player.color)

        #return self.board, self.player1, self.player2

    def get_click_from(self):
        out_in = int(input("If you want to choose gobblet from out, press 0. If from the board, press 1: "))
        if out_in == 0:
            out = int(input("Choose which index: "))
            return out, 0, 0, out_in
        else:
            i = int(input("Choose which index i: "))
            j = int(input("Choose which index j: "))
            return 0, i, j, out_in

    def get_click_to(self):
        index_i = int(input("Choose which index i: "))
        index_j = int(input("Choose which index j: "))
        return index_i, index_j
    
    def play_turn_from(self, out, from_i, from_j, out_in):
        self.out = out
        self.from_i = from_i
        self.from_j =  from_j
        self.out_in = out_in
        #################out, from_i, from_j, out_in = self.get_click_from()
        if out_in == 1:  # Player choose from the board
            choosen_len = self.board.stacks[from_i][from_j].top().length
            not_lose = self.board.suggest_cells_case_1(choosen_len)
            if not not_lose: # not_lose = false -> game over
                print("GAME OVER")
                return True ,self.board.flags

        else:  # Player choose from the out
            choosen_len = self.current_player.stacks[out].top().length
            #warning_flag = any(self.current_player.warning_list)
            
            if not self.current_player.warn:  # No warning
                not_lose = self.board.suggest_cells_case_20(choosen_len)
                if not not_lose:
                    print("GAME OVER")
                    return True, self.board.flags
            else:  # With warning
                not_lose = self.board.suggest_cells_case_21(choosen_len, self.current_player.warning_list)
                if not not_lose:
                    print("GAME OVER")
                    return True, self.board.flags

        self.player1.off_outer_clicks()
        self.player2.off_outer_clicks()

        self.board.show_check_board()

        return False, self.board.flags 
    
    def play_turn_to(self, to_i, to_j):

        ################to_i, to_j = self.get_click_to()

        if self.out_in == 1: # Player choose from the board
            temp_gobblet = self.board.stacks[self.from_i][self.from_j].top()
            self.board.stacks[self.from_i][self.from_j].pop()
        else:
            temp_gobblet = self.current_player.stacks[self.out].top()
            self.current_player.stacks[self.out].pop()

        self.board.stacks[to_i][to_j].push(temp_gobblet)

        self.show_board_player()

        #return False
    


    def play(self):
        self.show_board_player()
        while True:
            self.available_click()

            self.show_check_board_player()

            if self.play_turn_from():
                break

            if self.play_turn_to():
                break
            
            ####        error   self.show_board_player()
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
