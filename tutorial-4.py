# tutorial-4.py

# Continuation of the tictactoe game

# 0's are the default game map
# Square braces for lists so we can change the elements
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

# Proof it's a list
print(type(game))

# Display
print("   a  b  c")

for count, row in enumerate(game):
    ''' multi-line comment
    '''
    print(count, row)



