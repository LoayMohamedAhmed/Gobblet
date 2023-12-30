from typing import  List
from gobblet_node import GobbletNode
from stack import GobbletStack

class Player:
    def __init__(self, color: str):
        # Check if the color is a single character
        if len(color) != 1:
            raise ValueError("Color should be a single character")

        # Player attributes
        self.color = color
        self.win = False
        self.warn = False
        self.check = [False] * 3
        self.warning_list = [False] * 10

        self.stacks = [GobbletStack() for _ in range(3)]

        # Add four GobbletNode instances to each stack with lengths from 1 to 4
        for stack in self.stacks:
            for length in range(1, 5):
                gobblet_node = GobbletNode(length, self.color)
                stack.push(gobblet_node)

    def show_player(self):
        print(f"Player {self.color}     ", end="")
        for stack in self.stacks:
            if stack.isEmpty():
                print("0  ", end="")
            else:
                print(f"{stack.top().length}  ", end="")
        print()

    def show_check_player(self):
        print(f"Player {self.color} Check : ", end="")
        for value in self.check:
            print(f"{int(value)}  ", end="")
        print()

    def off_outer_clicks(self):
        self.check = [False] * len(self.check)

    def handle_clicks(self, c):
        for i, stack in enumerate(self.stacks):
            if not stack.isEmpty() and stack.top().color == c:
                self.check[i] = 1
            else:
                self.check[i] = 0

    def display_info(self):
        # Display information about the player
        print(f"Color: {self.color}, Win: {self.win}, Warn: {self.warn}")
        print("Play:")
        for stack in self.play:
            for node in stack:
                node.display_info()
            print("---")
        print("Check:", self.check)
