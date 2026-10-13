# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:45:33 2026

@author: 87727
"""


import random

# 2.1 create the 2 matrixes with randint
M1 = [[random.randint(0, 50) for _ in range(10)] for _ in range(5)]

M2 = [[random.randint(0, 50) for _ in range(5)] for _ in range(10)]

# 2.2 definition of the multiplication of 2 matrixes
def Matrix_multip(A, B):
    # the rows of A
    rows_A = len(A)
    # the columes of A
    cols_A = len(A[0])
    # the columes of B
    cols_B = len(B[0])

    # determine a matrix of the result , get the number of rows of A and columes of B
    result = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            row.append(0)
        result.append(row)

    # multiplication
    #rols of result
    for i in range(rows_A):
        # columes of the result
        for j in range(cols_B):
            # determine the result of each element 
            total = 0
            # do the math
            for k in range(cols_A):
                total = total + A[i][k] * B[k][j]
            result[i][j] = total

    return result


# result test
print("M1:")
for row in M1:
    print(row)
    
print("M2:")
for row in M2:
    print(row)

print("M1 * M2:")
answer = Matrix_multip(M1, M2)
for row in answer:
    print(row)