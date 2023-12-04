'''
LICENCE belongs to:
GOLDEN NERDS :)

Created by:
Heydarova Nargiz
Guliyev Magsud
Mirzaguliyeva Farah
Alizade Fuad
'''
class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.grid = self.create_grid()
        self.current_player = '*'

    def create_grid(self):
        """
        A nested list is used to represent the grid 
        """
        return [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
    
    def display_board(self):
        """Display the current state of the Connect4 grid."""
        print("\n   1 2 3 4 5 6 7 ")
        print(" +----------------")
        for i in range(6):
            print(f'{6 - i}|', end=' ')
            for j in range(7):
                print(self.grid[i][j], end=' ')
            print()

    def clear_grid(self):
        """ Empty the grid for playing again"""
        #TODO Add this to play_again function 
        for i in range(len(self.grid)):
            for j in range(len(self.grid[1])):
                self.grid[i][j] = ' '

    def drop_disc(self, column):
        """ Implementing the disc droping """
        for row in range(self.rows - 1, -1, -1):
            if self.grid[row][column] == ' ':
                self.grid[row][column] = self.current_player
                break

    def switch_player(self):
        # Swiching players 
        self.current_player = 'O' if self.current_player == '*' else '*'

    def check_winner(self):
        # Check horizontally
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if (
                    self.grid[row][col] == self.grid[row][col + 1] == self.grid[row][col + 2] == self.grid[row][col + 3] != ' '
                ):
                    return True

        # Check vertically
        for row in range(self.rows - 3):
            for col in range(self.columns):
                if (
                    self.grid[row][col] == self.grid[row + 1][col] == self.grid[row + 2][col] == self.grid[row + 3][col] != ' '
                ):
                    return True

        # Check diagonally (down-right)
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if (
                    self.grid[row][col] == self.grid[row + 1][col + 1] == self.grid[row + 2][col + 2] == self.grid[row + 3][col + 3] != ' '
                ):
                    return True

        # Check diagonally (up-right)
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if (
                    self.grid[row][col] == self.grid[row - 1][col + 1] == self.grid[row - 2][col + 2] == self.grid[row - 3][col + 3] != ' '
                ):
                    return True

        return False

    def is_grid_full(self):
        #Check if the grid is already full
        return all(cell != ' ' for row in self.grid for cell in row)
    
    def is_opponent_close_to_win(self):
        #Checking if oppenent is close to win
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row][col] == ' ':
                    # Check if placing a disc in this position would lead to opponent winning
                    if self.check_opponent_winning_move(row, col):
                        return True
        return False

    def check_opponent_winning_move(self, row, col):
        # Check horizontally
        if self.check_consecutive(row, col, 0, 1):
            return True

        # Check vertically
        if self.check_consecutive(row, col, 1, 0):
            return True

        # Check diagonally (down-right)
        if self.check_consecutive(row, col, 1, 1):
            return True

        # Check diagonally (up-right)
        if self.check_consecutive(row, col, -1, 1):
            return True

        return False

    def check_consecutive(self, row, col, row_delta, col_delta):
        opponent = 'O' if self.current_player == '*' else '*'
        consecutive_count = 0

        for step in range(1, 4):
            new_row, new_col = row + step * row_delta, col + step * col_delta

            if (
                0 <= new_row < self.rows
                and 0 <= new_col < self.columns
                and self.grid[new_row][new_col] == opponent
            ):
                consecutive_count += 1
            else:
                break

        return consecutive_count == 3

        

    def play_game(self):
        """" Main game loop here"""
        print(f'{"-------------------------":^50}')
        print(f'{"-Welcome to Connect Four-":^50}')
        print(f'{"-------------------------":^50}')
        while True:
            if  self.is_opponent_close_to_win():
                print('\n')
                print('--------------------------------------------')
                print("Attention, your oppenent is close to win!!! |")
                print('--------------------------------------------')

            self.display_board()
            #Using try-except method to prevent errors
            try:
                column = int(input(f"Player {self.current_player}, choose a column (1-{self.columns}): ")) - 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if 0 <= column < self.columns and self.grid[0][column] == ' ':
                self.drop_disc(column)

                if self.check_winner():
                    self.display_board()
                    print(f"Player {self.current_player} wins!")
                    self.play_again()
                    break

                if self.is_grid_full():
                    self.display_board()
                    print("The game is a draw!")
                    break

                self.switch_player()
            else:
                print("Invalid move. Please choose a valid column.")
    def play_again(self):
        #Allows players to choose to play again.
        #If players choose not to play again game ends
        choise = input("Do want to play again(y/n)?: ")
        if choise == 'y':
          self.clear_grid()
          self.play_game()
        elif choise=='n':
            print("Thank you for playing Connect4, have a good day :)")

# Start the game
if __name__ == "__main__":
    connect_four_game = ConnectFour()
    connect_four_game.play_game()

