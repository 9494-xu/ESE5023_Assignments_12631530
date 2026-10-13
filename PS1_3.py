# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 22:06:07 2026

@author: 87727
"""

def Pascal_triangle(k):
   
    # the first line: [1]
    line = [1]

    # If k is 0, just print [1]
    if k == 0:
        print(line)
        return

    # Build the line step by step until we reach row k
    # Each new line is built from the previous one
    for i in range(1, k + 1):
        # Create a new list that starts with 1
        new_line = [1]

        # For every pair of neighbours in the old line,
        # add them together to get the middle values
        for j in range(len(line) - 1):
            new_line.append(line[j] + line[j + 1])

        # The new line also ends with 1
        new_line.append(1)

        # The new line becomes the current line for the next round
        line = new_line

    # After the loop, 'line' is the k-th line
    print(line)


# Report the required lines
print("Pascal_triangle(100):")
Pascal_triangle(100)

print("Pascal_triangle(200):")
Pascal_triangle(200)

x = int(input("which line you would like to know in Pascal trangle:"))
Pascal_triangle(x)