import numpy as np
import math
import random

ROW_COUNT = 6
COL_COUNT = 7

PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

def create_board():
    return np.zeros((ROW_COUNT, COL_COUNT))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print("\n")
    print(np.flip(board, 0))
    print(" 0  1  2  3  4  5  6")

def winning_move(board, piece):
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT - 3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    return False

def evaluate_window(window, piece):
    score = 0
    opp = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

def score_position(board, piece):
    score = 0

    center = [int(i) for i in list(board[:, COL_COUNT//2])]
    score += center.count(piece) * 3

    for r in range(ROW_COUNT):
        row = [int(i) for i in list(board[r, :])]
        for c in range(COL_COUNT - 3):
            score += evaluate_window(row[c:c+4], piece)

    for c in range(COL_COUNT):
        col = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT - 3):
            score += evaluate_window(col[r:r+4], piece)

    for r in range(ROW_COUNT - 3):
        for c in range(COL_COUNT - 3):
            score += evaluate_window([board[r+i][c+i] for i in range(4)], piece)
            score += evaluate_window([board[r+3-i][c+i] for i in range(4)], piece)

    return score

def get_valid_locations(board):
    return [c for c in range(COL_COUNT) if is_valid_location(board, c)]

def is_terminal_node(board):
    return (winning_move(board, PLAYER_PIECE) or
            winning_move(board, AI_PIECE) or
            len(get_valid_locations(board)) == 0)

def minimax(board, depth, alpha, beta, maximizing):
    valid = get_valid_locations(board)
    terminal = is_terminal_node(board)

    if depth == 0 or terminal:
        if terminal:
            if winning_move(board, AI_PIECE):
                return None, 1000000000
            elif winning_move(board, PLAYER_PIECE):
                return None, -1000000000
            else:
                return None, 0
        return None, score_position(board, AI_PIECE)

    if maximizing:
        value = -math.inf
        best_col = random.choice(valid)
        for col in valid:
            row = get_next_open_row(board, col)
            temp = board.copy()
            drop_piece(temp, row, col, AI_PIECE)
            new_score = minimax(temp, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value

    else:
        value = math.inf
        best_col = random.choice(valid)
        for col in valid:
            row = get_next_open_row(board, col)
            temp = board.copy()
            drop_piece(temp, row, col, PLAYER_PIECE)
            new_score = minimax(temp, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value


# 🎮 Game loop
board = create_board()
game_over = False
turn = random.randint(PLAYER, AI)

print("Welcome to Connect Four!")
print_board(board)

while not game_over:

    if turn == PLAYER:
        col = int(input("Your move (0-6): "))

        if 0 <= col <= 6 and is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, PLAYER_PIECE)

            if winning_move(board, PLAYER_PIECE):
                print_board(board)
                print("🎉 You win!")
                game_over = True

            turn = AI
            print_board(board)
        else:
            print("Invalid move, try again.")

    else:
        print("AI is thinking...")
        col, _ = minimax(board, 4, -math.inf, math.inf, True)

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, AI_PIECE)

            if winning_move(board, AI_PIECE):
                print_board(board)
                print("🤖 AI wins!")
                game_over = True

            turn = PLAYER
            print_board(board)

    if len(get_valid_locations(board)) == 0:
        print("It's a draw!")
        game_over = True