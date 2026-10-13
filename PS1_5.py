# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 22:08:07 2026

@author: 87727
"""

# 5.1

target = int(input("Give 1 number from 1-100:"))

def Find_expression(target):
    digits = "123456789"
    results = []

    # op1 controls gap between 1 and 2, op2 between 2 and 3, ..., op8 between 8 and 9
    for op1 in range(3):
        for op2 in range(3):
            for op3 in range(3):
                for op4 in range(3):
                    for op5 in range(3):
                        for op6 in range(3):
                            for op7 in range(3):
                                for op8 in range(3):

                                    # Store the 8 choices in a list for easy access
                                    ops = [op1, op2, op3, op4, op5, op6, op7, op8]

                                    # build the expression step by step
                                    # 'total'   : sum of all finished terms
                                    # 'current' : the number currently being built
                                    # 'expr'    : the expression string (for printing)

                                    total = 0
                                    current = int(digits[0])       # start with the first digit '1'
                                    expr = "1"

                                    # Walk through each gap and apply the chosen operation
                                    for i in range(8):
                                        # the digit after this gap: 2,3,...,9
                                        d = i + 2
                                        choice = ops[i]

                                        if choice == 0:
                                            # join: extend the current number
                                            current = current * 10 + d
                                            expr = expr + str(d)
                                        elif choice == 1:
                                            # plus: finish current term, start a new positive term
                                            total = total + current
                                            current = d
                                            expr = expr + "+" + str(d)
                                        else:
                                            # minus: finish current term, start a new negative term
                                            total = total + current
                                            current = -d
                                            expr = expr + "-" + str(d)

                                    # After all gaps, the final value is total + current
                                    value = total + current

                                    # If it matches the target, save the expression
                                    if value == target:
                                        results.append(expr)

    # Print all solutions found
    for e in results:
        print(e + "=" + str(target))

    return results

print(Find_expression(target))

# 5.2 


def count_all():
    counts = [0] * 101   # counts[v] = number of expressions equal to v (v = 1..100)

    for op1 in range(3):
        for op2 in range(3):
            for op3 in range(3):
                for op4 in range(3):
                    for op5 in range(3):
                        for op6 in range(3):
                            for op7 in range(3):
                                for op8 in range(3):

                                    ops = [op1, op2, op3, op4, op5, op6, op7, op8]

                                    total = 0
                                    current = 1

                                    # Apply each gap's operation
                                    for i in range(8):
                                        d = i + 2
                                        choice = ops[i]

                                        if choice == 0:
                                            current = current * 10 + d
                                        elif choice == 1:
                                            total = total + current
                                            current = d
                                        else:
                                            total = total + current
                                            current = -d

                                    value = total + current

                                    # Only count values in the range 1..100
                                    if 1 <= value <= 100:
                                        counts[value] = counts[value] + 1

    return counts


# Run and report

counts = count_all()
Total_solutions = counts[1:101]

print("Total_solutions =", Total_solutions)

maximum = max(Total_solutions)
minimum = min(Total_solutions)

max_numbers = []
min_numbers = []
for i in range(100):
    if Total_solutions[i] == maximum:
        max_numbers.append(i + 1)
    if Total_solutions[i] == minimum:
        min_numbers.append(i + 1)

print("Max count =", maximum, "at number(s):", max_numbers)
print("Min count =", minimum, "at number(s):", min_numbers)


# Plot
import matplotlib.pyplot as plt

numbers = list(range(1, 101))
plt.plot(numbers, Total_solutions, marker="o", markersize=3)
plt.xlabel("Target number (1 to 100)")
plt.ylabel("Number of solutions")
plt.title("Total_solutions for targets 1..100")
plt.grid(True)
plt.show()