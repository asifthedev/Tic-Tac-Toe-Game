class Board:
    """
    Represents the Tic Tac Toe game board.
    """

    def __init__(self):
        """
        Initializes the game board with empty spaces.
        """
        self.board = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']

    def print_board(self):
        """
        Prints the current state of the game board.
        """
        print('\n')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('-----------')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('-----------')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    def update_board(self, position, player_type):
        """
        Updates the game board with the player's move.

        Parameters:
            position (int): The position where the player wants to place their move.
            player_type (str): The type of the player ('X' or '0').

        Returns:
            bool: True if the move is successfully placed, False otherwise.
        """
        try:
            if self.board[position - 1] == ' ':
                self.board[position - 1] = player_type
                return True
            else:
                print("Position is already occupied. Try again!")
                return False
        except IndexError:
            print(f"{position} is not in range (1,9). Try again!")
            return False

    def check_winner(self, player_type):
        """
        Checks if the specified player has won the game.

        Parameters:
            player_type (str): The type of the player ('X' or '0').

        Returns:
            bool: True if the player has won, False otherwise.
        """
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
        """
        Checks if the game has ended in a draw.

        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        if ' ' not in self.board:
            print("Match draw!")
            return True


class Player:
    """
    Represents a player in the Tic Tac Toe game.
    """

    def __init__(self, player_type):
        """
        Initializes a player with the specified type.

        Parameters:
            player_type (str): The type of the player ('X' or '0').
        """
        self.type = player_type
        self.name = self.get_name(self.type)

    def get_name(self, player_type):
        """
        Retrieves the name of the player based on the player type.

        Parameters:
            player_type (str): The type of the player ('X' or '0').

        Returns:
            str: The name of the player.
        """
        if player_type == 'X':
            return input("Selecting name for player X: ")
        elif player_type == '0':
            return input("Selecting name for player 0: ")
        else:
            return None  # Invalid player type


class Game:
    """
    Represents the Tic Tac Toe game.
    """

    def __init__(self):
        """
        Initializes the game with a game board and players.
        """
        self.board = Board()
        self.player_1 = Player("X")
        self.player_2 = Player("0")
        self.current_player = self.player_1

    def play(self):
        """
        Starts and manages the game loop.
        """
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


if __name__ == '__main__':
    game = Game()
    game.play()
