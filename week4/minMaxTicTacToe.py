class TicTacToe:
    def __init__(self):
        # Initialise the game board with empty spaces
        self.__board = [ str(_) for _ in range(9)]
        self.__players = ["X", "O"]
        self.__moveCount = 1

    # Resets the game
    def __reset(self):
        self.__board = [ str(_) for _ in range(9)]
        self.__moveCount = 1

    def __checkWin(self):

        return (self.__board[0] == self.__board[4] == self.__board[8] == self.__players[(self.__moveCount+1)%2] ) or (self.__board[2] == self.__board[4] == self.__board[6]== self.__players[(self.__moveCount+1)%2]) or (self.__board[0] == self.__board[1] == self.__board[2] == self.__players[(self.__moveCount+1)%2]) or (self.__board[3] == self.__board[4] == self.__board[6] == self.__players[(self.__moveCount+1)%2]) or (self.__board[6] == self.__board[7] == self.__board[8] == self.__players[(self.__moveCount+1)%2]) or (self.__board[0] == self.__board[3] == self.__board[6] == self.__players[(self.__moveCount+1)%2]) or (self.__board[1] == self.__board[4] == self.__board[7] == self.__players[(self.__moveCount+1)%2]) or (self.__board[2] == self.__board[5] == self.__board[8] == self.__players[(self.__moveCount+1)%2])

    
    def __checkEnd(self):
        return (self.__moveCount > 8)

    def __display_board(self):
        """Display the current state of the board."""
        for i in range(9):
            if i%3 == 0 and i != 0:
                print("|")
                print("-------")
            print("|"+self.__board[i], end="")
        print("|")
        

    def __player_move(self):
        """Handle the player's move."""
        while True:
            try:
                position = int(input("Enter your move (0-8): "))
                break
            except ValueError:
                print("Invald input")
                continue
        # TODO: While the position is invalid, ask the user to enter it again.
        while self.__board[position] in ['X', "O"] or position < 0 or position > 8:
            position = int(input("Invalid position please enter again: "))
        self.__board[position] = self.__players[self.__moveCount%2]
        self.__moveCount += 1


    def run(self):
        """Main game loop."""
        print("Welcome to Tic-Tac-Toe.\nYou are player X. I am player O.\n")
        while True:
            if self.__checkEnd():
                print("It was a draw!")
                self.__reset()
            self.__display_board()
            self.__player_move()
            if self.__checkWin():
                print("Player " + self.__players[(self.__moveCount+1)%2] + " Won")
                self.__reset()


# Example usage:
if __name__ == "__main__":
    # TODO: Instantiate and start the game
    x = TicTacToe()
    x.run()
    pass

