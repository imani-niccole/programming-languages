# Tic Tac Toe game in Python

# Ashley Darling
# The program will display a tic tac toe board and play with the player. It deciphers between if the
# player won or if it tied with the program 

# Display the Tic Tac Toe board
def display_board(board):
    print("---------")
    for row in board:
        print("|".join(row))
        print("---------")

# Check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:  # Check main diagonal
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:  # Check anti-diagonal
        return True
    return False

# Check if the board is full (draw)
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        display_board(board)
        print(f"Player {current_player}'s turn. Enter row and column (0, 1, or 2):")
        
        # Get row and column input
        try:
            row = int(input("Row: "))
            col = int(input("Column: "))
            if board[row][col] != " ":
                print("Cell already taken. Choose another.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers between 0 and 2.")
            continue
        
        # Place the player's move
        board[row][col] = current_player
        
        # Check for win or draw
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_full(board):
            display_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()
