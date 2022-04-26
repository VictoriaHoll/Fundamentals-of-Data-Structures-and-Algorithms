# 1b Fundamentals of Data Structures and Algorithms

# Assignment 3, Marbles

class MarblesBoard():
    def __init__(self, board):
        self.board = list(board)
    def switch(self):
        position_1 = self.board[0] 
        position_2 = self.board[1]
        self.board[0] = position_2
        self.board[1] = position_1 
        return self.board
    def rotate(self):
        former_first = self.board[0]
        i = 1
        while i < len(self.board):          
            self.board[i-1] = self.board[i]
            i += 1
        self.board[-1] = former_first
        return self.board       
    def is_solved(self):
        i = 1
        while i < len(self.board):
            if self.board[i-1] < self.board[i]:
                i +=1
            else:
                return False
        return True 
    def __repr__(self):
        return '%s' % (self.board)
    def __str__(self):
        return str(self.board)


class Solver():
    def __init__(self, board):
        self.board = board
    def solve(self):
        total_steps = 0
        i = 0
        print(self.board)
        while i < 100**2:
            if self.board.is_solved():
                return print('total steps: ', total_steps)
            elif self.board.board[0] == 0 or self.board.board[1] == 0:
                self.board.rotate()
                total_steps += 1
                i += 1
                print(self.board)
            elif self.board.board[0] > self.board.board[1]:
                self.board.switch()
                total_steps += 1
                i += 1
                print(self.board)
            else:
                self.board.rotate() 
                total_steps += 1
                i += 1
                print(self.board)

# Big O notation dictates that program runs at: comparing two numbers, switching or rotating values in a list is O(n).


import sys
draft_input = sys.argv[1].split(',')
final_input = list(map(int, draft_input)) # => [1,2,3]

board_grade = MarblesBoard(final_input)
player_grade = Solver(board_grade)
player_grade.solve()