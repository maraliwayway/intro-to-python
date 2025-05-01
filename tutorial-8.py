# tutorial-8.py

# strings are immutable 
# can't reassign entire list in a function, but can modify things in list
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

def game_board(game_map, player=0, row=0, column=0, just_display=False):
        print("   a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
                print(count, row)
        return game_map

gane = game_board(game, just_display=True)
game = game_board(game, player=1, row=2, column=0)