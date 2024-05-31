def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]
def display_board(board):
    print("---------")
    for row in board:
        print("|".join(row))
        print("---------")
def check_win(board, player):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        if all(board[x][y] == player for x, y in condition):
            return True
    return False
def check_draw(board):
    return all(board[x][y] != " " for x in range(3) for y in range(3))
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                raise ValueError
            x, y = divmod(move - 1, 3)
            if board[x][y] == " ":
                board[x][y] = "X"
                break
            else:
                print("This cell is already taken!")
        except ValueError:
            print("Invalid move. Please enter a number between 1 and 9.")
            import random

def ai_move(board):
    # Check if AI can win in the next move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if check_win(board, "O"):
                    return
                board[i][j] = " "

    # Block player's winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if check_win(board, "X"):
                    board[i][j] = "O"
                    return
                board[i][j] = " "

    # Take the center if available
    if board[1][1] == " ":
        board[1][1] = "O"
        return

    # Take a random available corner
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    available_corners = [corner for corner in corners if board[corner[0]][corner[1]] == " "]
    if available_corners:
        x, y = random.choice(available_corners)
        board[x][y] = "O"
        return

    # Take any remaining space
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty_cells:
        x, y = random.choice(empty_cells)
        board[x][y] = "O"
def play_game():
    board = create_board()
    display_board(board)
    
    while True:
        player_move(board)
        display_board(board)
        if check_win(board, "X"):
            print("You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move(board)
        display_board(board)
        if check_win(board, "O"):
            print("AI wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
