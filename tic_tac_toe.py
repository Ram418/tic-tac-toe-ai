import random as r


# This is a nested list for the board of the game
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]



# This function prints the board
def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# This is user play function
def user_play():

    while True:
        row = int(input("Enter the row u want to play "))
        coloum = int(input("Enter the coloum u want to play "))
        if board[row][coloum] == ' ':
            board[row][coloum] = 'X'
            break
        else:
            print("Hey its taken")
    print_board()


# This is Agent play function
def agent_play():

    while True:
        row = r.randint(0, 2)
        coloum = r.randint(0, 2)
        if board[row][coloum] == ' ':
            board[row][coloum] = 'O'
            break
        else:
            print("Hey its taken")
    print_board()


# This will check for winning in row
def check_win_row(player):

    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
    return False


# This will check for winning in coloum
def check_win_col(player):

    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

# This will check for winning in diagonally
def check_win_diag(player):
    if board[0][0] == player and board[1][1]== player and board[2][2]==player:
        return True
    if board[0][2] == player and board[1][1]== player and board[2][0]== player:
        return True
    return False

#Combining all the three cases
def check_all(player):
    if check_win_row(player) or check_win_col(player) or check_win_diag(player):
        return True
    return False

#A draw function
def is_draw():
    return all(cell != ' ' for row in board for cell in row)

#Game Playyyyyyyyyyyyyyyyyyy
def play_game():
    while True:
        user_play()
        if check_all('X'):
            print("You win!")
            break
        if is_draw():
            print("Its a draw")
            break

        agent_play()
        if check_all('O'):
            print("Agent wins!")
            break
        if is_draw():
            print("Its a draw")
            break

play_game()
        
