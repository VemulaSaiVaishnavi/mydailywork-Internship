import math
import time

class TicTacToe:
    def __init__(self):
        self.board=[" "for _ in range(9)]
          #creates empty board
    def print_board(self):
        print()
        for i in range(0,9,3):
            print("|", self.board[i], "|", self.board[i+1], "|", self.board[i+2], "|")
            print()
    def check_winner(self, player):
        wins = [
            [0,1,2], [3,4,5], [6,7,8],  #rows
            [0,3,6], [1,4,7], [2,5,8],  #columns
            [0,4,8], [2,4,6]            #diagonals
    ]

        for w in wins:
            if (self.board[w[0]] == player and
                self.board[w[1]] == player and
                self.board[w[2]] == player):
                return True
        return False
    def is_draw(self):
        return " " not in self.board
    def available_moves(self):
        return [i for i in range(9) if self.board[i] == " "]
    def minimax(self, is_maximizing):
        if self.check_winner("O"):
            return 1                  #ai wins
        if self.check_winner("X"):
            return -1                 #human wins
        if self.is_draw():
            return 0                  #draw
        if is_maximizing:
            best_score = -math.inf
            for move in self.available_moves():
                self.board[move] = "O"
                score = self.minimax(False)
                self.board[move] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for move in self.available_moves():
                self.board[move] = "X"
                score = self.minimax(True)
                self.board[move] = " "
                best_score = min(score, best_score)
            return best_score
    def ai_move(self):
        best_score = -math.inf
        best_move = None
        for move in self.available_moves():
            self.board[move] = "O"
            score = self.minimax(False)
            self.board[move] = " "
            if score > best_score:
                best_score = score
                best_move = move
        self.board[best_move] = "O"
    def human_move(self):
        while True:
            try:
                move=int(input("Enter your move (1-9): ")) - 1
                if move in self.available_moves():
                    self.board[move] = "X"
                    break
                else:
                    print("Invalid move. Try again.")
            except:
                print("Please enter a valid number between 1 and 9.")
    def play(self):
            print("🎮 Tic Tac Toe: Human (X) vs AI (O)")
            self.print_board()
            while True:
                self.human_move()
                self.print_board()
                if self.check_winner("X"):
                    print("🎉 You win!")
                    break
                if self.is_draw():
                    print("🤝 Draw!")
                    break
                print("AI is making move...")
                time.sleep(2)
                self.ai_move()
                self.print_board()
                print("AI has made move, now your turn!!")
                if self.check_winner("O"):
                    print("💀 AI wins!")
                    break
                if self.is_draw():
                    print("🤝 Draw!")
                    break
game = TicTacToe()
game.play()

