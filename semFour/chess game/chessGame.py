import copy

# Initialize an 8x8 chessboard with pieces
def initialize_board():
    return [
        ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["r", "n", "b", "q", "k", "b", "n", "r"]
    ]

# Print the board
def print_board(board):
    print("\n".join([" ".join(row) for row in board]))
    print("\n")

# Check if a move is valid (simplified)
def is_valid_move(board, start, end, turn):
    x1, y1 = start
    x2, y2 = end
    piece = board[x1][y1]

    # Prevent moving empty space
    if piece == ".":
        return False
    
    # Prevent moving opponent's piece
    if turn == "white" and piece.islower():
        return False
    if turn == "black" and piece.isupper():
        return False

    # Simplified move validation (full rules require more logic)
    if piece.lower() == "p":  # Pawn moves
        direction = -1 if piece.isupper() else 1
        if y1 == y2 and board[x2][y2] == "." and (x2 == x1 + direction):
            return True
        if y1 == y2 and abs(x2 - x1) == 2 and x1 in (1, 6):  # Double move
            return True
        if abs(y2 - y1) == 1 and x2 == x1 + direction and board[x2][y2] != ".":
            return True

    # Simple movement for other pieces
    return True  # Assume valid for now (implement full rules later)

# Make a move
def make_move(board, start, end):
    x1, y1 = start
    x2, y2 = end
    board[x2][y2] = board[x1][y1]
    board[x1][y1] = "."
    return board

# Backtracking: Undo last move
def undo_move(board, history):
    if history:
        return history.pop()
    return board

# Main game loop
def play_chess():
    board = initialize_board()
    history = []  # Stack for backtracking (undo moves)
    turn = "white"

    while True:
        print_board(board)
        print(f"{turn.capitalize()}'s turn.")

        move = input("Enter move (e.g., 'e2 e4') or 'undo': ").strip().lower()
        if move == "undo":
            board = undo_move(board, history)
            turn = "white" if turn == "black" else "black"
            continue

        try:
            start, end = move.split()
            start = (8 - int(start[1]), ord(start[0]) - ord('a'))
            end = (8 - int(end[1]), ord(end[0]) - ord('a'))
        except:
            print("Invalid move format. Use 'e2 e4' format.")
            continue

        if is_valid_move(board, start, end, turn):
            history.append(copy.deepcopy(board))  # Save state for backtracking
            board = make_move(board, start, end)
            turn = "black" if turn == "white" else "white"
        else:
            print("Invalid move! Try again.")

play_chess()
