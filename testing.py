# Tic Tac Toe game main function (self made)

# Importing the necessary modules
import random
import time

# Function to print the board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end = " ")
        for j in range(3):
            print(board[i][j], end = " | ")
        print()
        print("-------------")

# Function to check if the board is full
def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

# Function to check if the player has won
def player_won(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return

# Function to check if the computer has won
def computer_won(board, computer):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == computer:
            return True
        if board[0][i] == board[1][i] == board[2][i] == computer:
            return True
    if board[0][0] == board[1][1] == board[2][2] == computer:
        return True
    if board[0][2] == board[1][1] == board[2][0] == computer:
        return True
    return

# Function to check if the game is over
def game_over(board):
    return is_full(board) or player_won(board, "X") or computer_won(board, "O")

# Function to check if the player can win in the next move
def player_can_win(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if player_won(board, "X"):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "
    return None

# Function to check if the computer can win in the next move
def computer_can_win(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if computer_won(board, "O"):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "
    return None

# Function to check if the player can block the computer from winning
def player_can_block(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if computer_won(board, "O"):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "
    return None

# Function to check if the computer can block the player from winning
def computer_can_block(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if player_won(board, "X"):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "
    return None

# Function to check if the player can make a fork
def player_can_fork(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if player_can_win(board):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                board_copy = [row[:] for row in board]
                if player_can_win(board_copy):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "   
    return None

# Function to check if the computer can make a fork
def computer_can_fork(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if computer_can_win(board):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                board_copy = [row[:] for row in board]
                if computer_can_win(board_copy):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "   
    return None
    
# Function to make a move
def make_move(board, player, i, j):
    board[i][j] = player

# Function to get the player's move
def get_player_move(board):
    while True:
        try:
            i, j = map(int, input("Enter the row and column (0-2) where you want to place your X: ").split())
            if board[i][j] == " ":
                return i, j
            else:
                print("This cell is already occupied. Please try again.")
        except:
            print("Invalid input. Please try again.")

# Function to get the computer's move
def get_computer_move(board):
    if computer_can_win(board):
        return computer_can_win(board)
    if player_can_win(board):
        return player_can_win(board)
    if computer_can_block(board):
        return computer_can_block(board)
    if player_can_block(board):
        return player_can_block(board)
    if computer_can_fork(board):
        return computer_can_fork(board)
    if player_can_fork(board):
        return player_can_fork(board)
    while True:
        i, j = random.randint(0, 2), random.randint(0, 2)
        if board[i][j] == " ":
            return i, j

# Function to play the game
def play_game():
    board = [[" " for j in range(3)] for i in range(3)]
    print_board(board)
    while not game_over(board):
        i, j = get_player_move(board)
        make_move(board, "X", i, j)
        print_board(board)
        if game_over(board):
            break
        i, j = get_computer_move(board)
        make_move(board, "O", i, j)
        print_board(board)
    if player_won(board, "X"):
        print("Congratulations! You won!")
    elif computer_won(board, "O"):
        print("The computer won!")
    else:
        print("It's a draw!")

# Main function
if __name__ == "__main__":
    play_game()
    time.sleep(5)
    print("Thank you for playing the game!")
    time.sleep(5)
    print("Goodbye!")
    time.sleep(5)

# End of program




