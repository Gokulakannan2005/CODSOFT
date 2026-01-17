import math

HUMAN = 'X'
COMPUTER = 'O'
EMPTY = ' '


def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):
    return all(cell != EMPTY for row in board for cell in row)


def minimax(board, is_computer_turn):
    if check_winner(board, COMPUTER):
        return 1
    if check_winner(board, HUMAN):
        return -1
    if is_draw(board):
        return 0

    if is_computer_turn:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = COMPUTER
                    score = minimax(board, False)
                    board[i][j] = EMPTY
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    score = minimax(board, True)
                    board[i][j] = EMPTY
                    best_score = min(best_score, score)
        return best_score


def computer_move(board):
    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = COMPUTER
                score = minimax(board, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move


def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]

    print("Tic-Tac-Toe")
    print("You are X")
    print("Computer is O")

    while True:
        print_board(board)

        # Human turn
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == EMPTY:
                    board[row][col] = HUMAN
                    break
                else:
                    print("That cell is already occupied.")
            except:
                print("Invalid input. Please enter numbers between 0 and 2.")

        if check_winner(board, HUMAN):
            print_board(board)
            print("You win!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Computer turn
        row, col = computer_move(board)
        board[row][col] = COMPUTER

        if check_winner(board, COMPUTER):
            print_board(board)
            print("Computer wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
