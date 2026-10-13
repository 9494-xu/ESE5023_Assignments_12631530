"""
Created on Sun Oct 11 22:16:00 2026

@author: 87727
"""

#ask the user to give a number to count
x = int(input("get a number from 1-100:"))


def Least_moves(x):


    # Count how many moves we have made
    moves = 0
    "the logic is that we can only +1 or double from 1,"
    "and the least moves from 1 to a specific number is to do the most doubles."
    "so we can devide the aim number with 2, and if can't, -1 until the number get to 1"

    # Work backwards from x down to 1.
    # Going forward:  *2  or  +1
    # Going backward: /2  (only if even)  or  -1
    while x > 1:
        if x % 2 == 0:
            # If x is even, the last forward move could have been *2,
            # so we reverse it by dividing by 2.
            # Dividing is better than subtracting because it reduces
            # the number faster, which keeps the move count minimal.
            x = x // 2
        else:
            # If x is odd, we cannot divide by 2 exactly,
            # so the last forward move must have been +1.
            # We reverse it by subtracting 1.
            x = x - 1

        # One reverse step means one forward move
        moves = moves + 1

    # When x reaches 1, we are back at the start
    print(moves)

#show the least moves
Least_moves(x)
