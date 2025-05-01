# tutorial-4.py

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

# FUNCTIONS
# no camel case, separate by underscpre instead
def game_board():
        print("   a  b  c")
        for count, row in enumerate(game):
                print(count, row)

game_board()

game[0][1] = 1

game_board()
    



