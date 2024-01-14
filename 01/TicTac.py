"""This is TicTac Game"""

from random import randint


class OccupiedFieldError(Exception):
    """Show when gamer try chose field that already occupied"""

    def __str__(self):
        return "This place is already occupied by another player!"


class TicTacGame:

    def __init__(self, n, player="computer"):
        self.board = [["*" for i in range(n)] for j in range(n)]
        self.current_player = "X"
        self.player = player
        self.winner = ""

    def show_board(self):
        """Show game board"""

        for row in range(len(self.board)):
            for column in range(len(self.board)):
                print(self.board[row][column], end='\t')
            print()

    def _validate_input(self):
        """Check users input until user enter validate value"""

        while True:
            try:
                position_row, position_column = map(int, input("Chose the row and column for your move: ").split())
                if self.board[position_row][position_column] != "*":
                    raise OccupiedFieldError
            except ValueError:
                print("Row and column must be integer and not empty. Try again!")
            except IndexError:
                print("You go out of field. Enter validated value of row and column")
            except OccupiedFieldError:
                print("This place is already occupied by another player! Try to choose another one.")
            else:
                print("You done your move", end="\n\n")
                return position_row, position_column

    def _fill_tracking_move(self, position_row: int, position_column: int, gamer: str):
        """Fill auxiliary structure for checking board state and indicate winner on-line"""

        gamer_id = 1
        if gamer == "O":
            gamer_id = -1

        self.move_tracking[position_column] += gamer_id
        self.move_tracking[position_row + len(self.board)] += gamer_id

        if position_row == position_column:
            if len(self.board) % 2 != 0 and position_column == len(self.board)//2:
                self.move_tracking[-1] += gamer_id
            self.move_tracking[-2] += gamer_id
        elif len(self.board) - position_row == len(self.board) - position_column:
            self.move_tracking[-1] += gamer_id

        if len(self.board) in (abs(self.move_tracking[position_column]),
                               abs(self.move_tracking[position_row + len(self.board)]),
                               abs(self.move_tracking[-2]), abs(self.move_tracking[-1])):
            self.winner = self.current_player

    def start_game(self):
        """basic logic os program"""

        if len(self.board) < 3:
            print(f"The winner is {self.current_player}")
        else:
            self.move_tracking = [0] * (len(self.board) * 2 + 2)
            count_moves = 0
            while not self._check_winner():
                if count_moves == len(self.board) * len(self.board):
                    break
                self.show_board()
                print(f"Current player is {self.current_player} \n")

                if self.player == "human":
                    position_row, position_column = self._validate_input()
                else:
                    position_row = randint(0, len(self.board) - 1)
                    position_column = randint(0, len(self.board) - 1)
                    while self.board[position_row][position_column] != "*":
                        position_row, position_column = randint(0, len(self.board) - 1), randint(0, len(self.board) - 1)

                self.board[position_row][position_column] = self.current_player
                self._fill_tracking_move(position_row, position_column, self.current_player)

                if self.current_player == "X":
                    self.current_player = "O"
                else:
                    self.current_player = "X"
                count_moves += 1

            print("Final board: ")
            self.show_board()
            if count_moves == len(self.board) * len(self.board) and not self._check_winner():
                print("Nobody wins")
            else:
                print(f"The winner is {self.winner}")

    def _check_winner(self):
        if self.winner != "":
            return self.winner
        return None


if __name__ == "__main__":
    scale_board = int(input("Set the size of the field for the game: "))
    mode = input("Chose mode: computer vs computer: enter 'computer' or human vs human: enter 'human': ")
    game = TicTacGame(scale_board, mode)
    game.start_game()
