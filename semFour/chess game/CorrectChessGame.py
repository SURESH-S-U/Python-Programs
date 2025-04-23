import copy

class ChessGame:
    def __init__(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p'] * 8,
            [' '] * 8,
            [' '] * 8,
            [' '] * 8,
            [' '] * 8,
            ['P'] * 8,
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.current_player = 'white'
        self.white_king_pos, self.black_king_pos = (7, 4), (0, 4)
        self.game_over, self.winner = False, None

    def print_board(self):
        print("  a b c d e f g h")
        print(" +-----------------+")
        for i, row in enumerate(self.board):
            print(f"{8-i}| {' '.join(row)} |{8-i}")
        print(" +-----------------+")

    def is_valid_position(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8

    def get_piece_color(self, piece):
        return 'white' if piece.isupper() else 'black' if piece != ' ' else None

    def is_king_in_check(self, board, color):
        king_pos = self.white_king_pos if color == 'white' else self.black_king_pos
        return any(king_pos in self.get_valid_moves_for_piece(board, r, c, False)
                   for r in range(8) for c in range(8) if self.get_piece_color(board[r][c]) != color)

    def get_valid_moves_for_piece(self, board, r, c, check_check=True):
        piece, color, moves = board[r][c], self.get_piece_color(board[r][c]), []
        if piece == ' ': return moves
        
        dirs = {'p': [(1, 0), (1, -1), (1, 1)], 'r': [(0, 1), (1, 0), (0, -1), (-1, 0)],
                'b': [(1, 1), (1, -1), (-1, 1), (-1, -1)], 'q': [(0, 1), (1, 1), (1, 0),
                (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)], 'n': [(2, 1), (1, 2), (-1, 2),
                (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)], 'k': [(0, 1), (1, 1), (1, 0),
                (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]}
        
        if piece.lower() == 'p':
            d, start = (-1, 6) if color == 'white' else (1, 1)
            if self.is_valid_position(r + d, c) and board[r + d][c] == ' ': moves.append((r + d, c))
            for dc in [-1, 1]:
                if self.is_valid_position(r + d, c + dc) and self.get_piece_color(board[r + d][c + dc]) != color:
                    moves.append((r + d, c + dc))
        else:
            for dr, dc in dirs[piece.lower()]:
                for i in range(1, 8):
                    nr, nc = r + dr * i, c + dc * i
                    if not self.is_valid_position(nr, nc): break
                    if board[nr][nc] == ' ':
                        moves.append((nr, nc))
                    else:
                        if self.get_piece_color(board[nr][nc]) != color:
                            moves.append((nr, nc))
                        break
                    if piece.lower() in 'nk': break
        
        if check_check:
            moves = [m for m in moves if not self.is_king_in_check(self.simulate_move(board, r, c, m), color)]
        return moves

    def simulate_move(self, board, fr, fc, to):
        new_board = copy.deepcopy(board)
        new_board[to[0]][to[1]], new_board[fr][fc] = new_board[fr][fc], ' '
        return new_board

    def make_move(self, fr, to):
        if to not in self.get_valid_moves_for_piece(self.board, *fr): return False
        self.board[to[0]][to[1]], self.board[fr[0]][fr[1]] = self.board[fr[0]][fr[1]], ' '
        if self.board[to[0]][to[1]].lower() == 'k':
            if self.current_player == 'white': self.white_king_pos = to
            else: self.black_king_pos = to
        self.current_player = 'black' if self.current_player == 'white' else 'white'
        if self.is_king_in_check(self.board, self.current_player): self.game_over, self.winner = True, self.current_player
        return True

    def convert_notation(self, notation):
        return (8 - int(notation[1]), ord(notation[0]) - ord('a')) if len(notation) == 2 else None


def main():
    chess = ChessGame()
    print("Python Chess - Enter moves as 'e2e4' or 'quit'")
    
    while not chess.game_over:
        chess.print_board()
        move = input(f"{chess.current_player.capitalize()}'s move: ").strip().lower()
        if move == 'quit': break
        if len(move) != 4: continue
        fr, to = chess.convert_notation(move[:2]), chess.convert_notation(move[2:])
        if fr and to: chess.make_move(fr, to)
    
    chess.print_board()
    if chess.winner: print(f"Game Over: {chess.winner.capitalize()} wins!")

if __name__ == "__main__":
    main()