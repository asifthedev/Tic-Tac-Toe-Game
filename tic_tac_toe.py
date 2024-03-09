class Board:
    def __init__(self):
        self.board = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']
        
    def print_board(self):
        print('\n')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('-----------')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('-----------')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    def update_board(self, position, player_type):
        try:
            if self.board[position-1] == ' ':
                self.board[position-1] = player_type
                return True
            else:
                print("Position is already occupied. Try again!")
                return False
        except IndexError:
            print(f"{position} is not in range (1,9). Try again!")
            return False

    def check_winner(self, player_type):
        if (self.board[0] == self.board[1] == self.board[2] == player_type or
            self.board[3] == self.board[4] == self.board[5] == player_type or
            self.board[6] == self.board[7] == self.board[8] == player_type or
            self.board[0] == self.board[3] == self.board[6] == player_type or
            self.board[1] == self.board[4] == self.board[7] == player_type or
            self.board[2] == self.board[5] == self.board[8] == player_type or
            self.board[0] == self.board[4] == self.board[8] == player_type or
            self.board[2] == self.board[4] == self.board[6] == player_type):
            return True
        else:
            return False

    def check_draw(self):
        if ' ' not in self.board:
            print("Match draw!")
            return True

class Player:
    def __init__(self, player_type):
        self.type = player_type
        self.name = self.get_name(self.type)

    def get_name(self, player_type):
        if player_type == 'X':
            return input("Selecting name for player X: ")
        elif player_type == '0':
            return input("Selecting name for player 0: ")
        else:
            return None  # Invalid player type

class Game:
    def __init__(self):
        self.board = Board()
        self.player_1 = Player("X")
        self.player_2 = Player("0")
        self.current_player = self.player_1
    
    def play(self):
        while True:
            try:
                message = f"{self.current_player.name}, enter position in range(1-9):"
                self.position = int(input(message))

                if self.board.update_board(self.position, self.current_player.type):
                    self.board.print_board()

                    if self.board.check_winner(self.current_player.type):
                        print(f"Congrats, {self.current_player.name} you are the winner!")
                        break

                    if self.board.check_draw():
                        break

                    # Switch players
                    if self.current_player == self.player_1:
                        self.current_player = self.player_2
                    else:
                        self.current_player = self.player_1
            except ValueError:
                print("Invalid value! hint: (1 -> 9)")

# Main part of the code
game = Game()
game.play()
