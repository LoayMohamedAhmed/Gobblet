from stack import GobbletStack

class Board:
    def __init__(self):
        # Initialize a 2D array of GobbletStack instances (4x4)
        self.stacks = [[GobbletStack() for _ in range(4)] for _ in range(4)]

        # Initialize a 2D array of boolean values (4x4) with initial value False
        self.flags = [[False] * 4 for _ in range(4)]
        #Initialize count1  for player 1 to count number of same moves to detect draw
        self.count1 = 0
        self.count2 = 0

    def handle_click(self, c):
        for i in range(4):
            for j in range(4):
                if self.stacks[i][j].getSize() != 0 and  self.stacks[i][j].top().color == c :
                    self.flags[i][j] = True
                else:
                    self.flags[i][j] = False

    # in board
    def suggest_cells_case_1(self, choosen_size):
        check = False
        for i in range(4):
            for j in range(4):
                # check on each cell if the cell is empty or have same color c
                if self.stacks[i][j].isEmpty() or self.stacks[i][j].top().length < choosen_size:
                    self.flags[i][j] = 1    # suggest it
                    check = True
                else:
                    self.flags[i][j] = 0
        return check    # if check still equal false then player have no play (player loose ---> game over)
    
    #in board and there is probability that player 1 take same move
    def check_and_increment1(self):
        draw1 = False
        self.count1 = self.count1 + 1
        if (self.count1 == 3):
            draw1 = True
        
        return draw1
    
    #in board and there is probability that player 2 take same move
    def check_and_increment2(self):
        draw2 = False
        self.count2 = self.count2 + 1
        if (self.count2 == 3):
            draw2 = True
        
        return draw2
    
    # out board without warning
    def suggest_cells_case_20(self, choosen_size):
        check = False
        for i in range(4):
            for j in range(4):
                if self.stacks[i][j].isEmpty():
                    self.flags[i][j] = 1
                    check = True
                else:
                    self.flags[i][j] = 0
        return check    #if check still equal false then player have no play (player loose ---> game over)

    # out board with warning
    def suggest_cells_case_21(self, choosen_size, warning_list):
        itr = 0
        check = False
        # handle horizontally
        for i in range(4): # 0 1 2
            for j in range(4):
                self.flags[i][j] = 0  # Reset all 2D board flags to zero first
                if self.stacks[i][j].isEmpty():
                    self.flags[i][j] = 1
                    check = True
                if warning_list[itr] == False:
                    continue
                if self.stacks[i][j].isEmpty() or self.stacks[i][j].top().length < choosen_size:
                    self.flags[i][j] = 1
                    check = True
            itr += 1
        
        # handle vertically
        for i in range(4):
            if warning_list[itr] == False:
                continue
            for j in range(4):
                if self.stacks[j][i].isEmpty() or self.stacks[j][i].top().length < choosen_size:
                    self.flags[j][i] = 1
                    check = True
            itr += 1
        
        # handle top left diagonal
        if warning_list[itr] == True:
            for i in range(4):
                if self.stacks[i][i].isEmpty() or self.stacks[i][i].top().length < choosen_size:
                    self.flags[i][i] = 1
                    check = True
        itr += 1

        # handle top right diagonal
        if warning_list[itr] == True:
            for i in range(4):
                j = 3 - i
                if self.stacks[i][j].isEmpty() or self.stacks[i][j].top().length < choosen_size:
                    self.flags[i][j] = 1
                    check = True

        return check    # if check still equal false then player have no play (player loose ---> game over)
    
    def check_winning(self, c):
        # make three for loop to check vertically, horizontally , diagonally

        # check horizontally
        check = True
        for i in range(4):
            check = True
            for j in range(4):
                if self.stacks[i][j].isEmpty() or self.stacks[i][j].top().color != c :
                    check = False
            if check: 
                return check
            
        # check vertically
        check = True
        for i in range(4):
            check = True
            for j in range(4):
                if self.stacks[j][i].isEmpty() or self.stacks[j][i].top().color != c :
                    check = False
            if check: 
                return check
        
        # check top left diagonal
        check = True
        for i in range(4):
            if self.stacks[i][i].isEmpty() or self.stacks[i][i].top().color != c :
                check = False
        if check:
            return check
        
        # check top right diagonal
        check = True
        for i in range(4):
            # i --> 0  1   2   3
            # j --> 3  2   1   0
            j = 3 - i
            if self.stacks[i][j].isEmpty() or self.stacks[i][j].top().color != c :
                check = False
        
        return check
    
    def check_warning(self, c, warning_list):
        itr = 0
        check = False

        # Check horizontally
        for i in range(4):
            count = 0
            for j in range(4):
                if self.stacks[i][j].isEmpty():
                    pass
                elif self.stacks[i][j].top().color != c:
                    count += 1
                else:
                    count -= 1

            if count == 3:
                warning_list[itr] = True
                check = True
            else:
                warning_list[itr] = False
            itr += 1

        # Check vertically
        for i in range(4):
            count = 0
            for j in range(4):
                if self.stacks[j][i].isEmpty():
                    pass
                elif self.stacks[j][i].top().color != c:
                    count += 1
                else:
                    count -= 1

            if count == 3:
                warning_list[itr] = True
                check = True
            else:
                warning_list[itr] = False
            itr += 1

        # Check top left diagonal
        count = 0
        for i in range(4):
            if self.stacks[i][i].isEmpty():
                pass
            elif self.stacks[i][i].top().color != c:
                count += 1
            else:
                count -= 1

        if count == 3:
            warning_list[itr] = True
            check = True
        else:
            warning_list[itr] = False
        itr += 1

        # Check top right diagonal
        count = 0
        for i in range(4):
            j = 3 - i
            if self.stacks[i][j].isEmpty():
                pass
            elif self.stacks[i][j].top().color != c:
                count += 1
            else:
                count -= 1

        if count == 3:
            warning_list[itr] = True
            check = True
        else:
            warning_list[itr] = False
        itr += 1

        return check
 
    def show_check_board(self):
        for i in range(4):
            for j in range(4):
                print("+---", end="")
            print("+")

            for j in range(4):
                print(f"| {1 if self.flags[i][j] else 0}", end="")
            print("|")

        for j in range(4):
            print("+---", end="")
        print("+")
 
    def show_board(self):
        for i in range(4):
            for j in range(4):
                print("+---+---", end="")
            print("+")

            for j in range(4):
                if self.stacks[i][j].isEmpty():
                    print("| 0, 0", end="")
                else:
                    top_node = self.stacks[i][j].top()
                    print(f"| {top_node.length}, {top_node.color}", end="")
            print("|")

        for j in range(4):
            print("+---+---", end="")
        print("+")
