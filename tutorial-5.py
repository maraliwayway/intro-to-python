# tutorial-5.py

# Continuation of the tictactoe game

'''l = [1, 2, 3, 4, 5]
print(l[1])
print(l[-1])
print(l[1:3]) # Doesn't include element 3
l[3] = 2
print(l[3])'''
 
# 0's are the default game map
# Square braces for lists so we can change the elements
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

game[0][1] = 1

# Proof it's a list
print(type(game))

# Display
print("   a  b  c")

for count, row in enumerate(game):

    print(count, row)