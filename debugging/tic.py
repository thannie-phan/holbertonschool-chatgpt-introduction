#!/usr/bin/python3

def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there is a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """Checks if the board is full (draw)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main game loop for Tic Tac Toe."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Input validation loop
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                if row not in [0,1,2] or col not in [0,1,2]:
                    print("Row and column must be 0, 1, or 2. Try again.")
                    continue
                
                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue
                
                # Valid input
                break
            except ValueError:
                print("Invalid input. Please enter numbers 0, 1, or 2.")

        # Place the mark
        board[row][col] = player

        # Check winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check draw
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

# Start the game
tic_tac_toe()
