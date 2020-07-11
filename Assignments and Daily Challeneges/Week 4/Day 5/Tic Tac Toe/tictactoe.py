board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

wins = [
    [(0,0), (0,1), (0,2)],
    [(1,0), (1,1), (1,2)], 
    [(2,0), (2,1), (2,2)], 
    [(0,0), (1,0), (2,0)], 
    [(0,1), (1,1), (2,1)], 
    [(0,2), (1,2), (2,2)],
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)]
]



# display_board() – To display Tic Tac Toe board (GUI).
# player_input(player) – To get input position from the player.
# check_win() – To check winner of the game.
# play() – More like the main function, which calls above function for gameplay.

def display_board():
    print("    0   1   2")
    for count, row in enumerate(board):
        print(count, row)

def player_input(letter):
    choice = input("Please enter the space for your entry: ")
    for i in range(3):
        for j in range(3):
            if choice == board[i][j]:
                board[i][j] = letter
    display_board()
    if check_win():
        return True
    else:
        return False

def check_win():
    for condition in wins:
        if board[condition[0][0]][condition[0][1]] == board[condition[1][0]][condition[1][1]] == board[condition[2][0]][condition[2][1]]:
            print(f'Player {board[condition[0][0]][condition[0][1]]} wins!!')
            return True
    return False

def play():
    display_board()
    turns = 0
    while True:
        if turns > 8:
            print("It's a tie.")
            break
        if turns % 2 == 0:
            win = player_input("X")
        else:
            win = player_input("O")
        turns += 1
        if win:
            break

play()