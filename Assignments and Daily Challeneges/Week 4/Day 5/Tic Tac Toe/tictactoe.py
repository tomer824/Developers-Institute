board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]

player1 = ""
player2 = ""

def update_display():
    print("    1    2    3")
    for count, row in enumerate(board):
        print(count, row)

update_display()

