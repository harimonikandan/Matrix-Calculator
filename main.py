import numpy as np


def matrix_creator(rows, columns):
    matrix = []

    for i in range(rows):
        print(f"Please enter all elements in Row {i + 1} of the 1st matrix")
        row_list = []
        for j in range(columns):
            num = int(input(f"Please enter the element ({i + 1},{j + 1}) of the 1st matrix\n"))
            row_list.append(num)
        matrix.append(row_list)

    matrix = np.array(matrix)

    return matrix

def second_matrix_creator(rows, columns):
    matrix = []

    for i in range(rows):
        print(f"Please enter all elements in Row {i + 1} of the 2nd matrix")
        row_list = []
        for j in range(columns):
            num = int(input(f"Please enter the element ({i + 1},{j + 1}) of the 2nd matrix\n"))
            row_list.append(num)
        matrix.append(row_list)

    matrix = np.array(matrix)

    return matrix


def add():
    matrix1 = matrix_creator(rows, columns)
    matrix2 = second_matrix_creator(rows, columns)

    for row in range(rows):
        for column in range(columns):
            matrix1[row][column] += matrix2[row][column]

    print(matrix1)


def subtract():
    matrix1 = matrix_creator(rows, columns)
    matrix2 = matrix_creator(rows, columns)

    for row in range(rows):
        for column in range(columns):
            matrix1[row][column] -= matrix2[row][column]

    print(matrix1)


def multiply_helper(matrix1, matrix2, row, column):
    num = 0
    for i in range(len(matrix2)):
        num += matrix1[column - 1][i] * matrix2[i][row]
    return num


def multiply():
    matrix1 = matrix_creator(rows, columns)

    new_rows = int(input("How many rows in the second matrix?\n"))
    if new_rows != columns:
        print("Number of rows in 2nd matrix should match number of columns of the 1st")
        print("Please try again")
        exit()
    new_columns = int(input("How many columns in the second matrix?\n"))
    matrix2 = matrix_creator(new_rows, new_columns)

    final_matrix = [[sum(x * y for x,y in zip(row,col)) for col in zip(*matrix2)] for row in matrix1]

    print(np.array(final_matrix))

def transpose():
    matrix = matrix_creator(rows, columns)
    print(matrix.T)


def power_helper(matrix, orig_matrix):
    if rows == columns:
        final_matrix = []
        for row in range(rows):
            row_list = []
            for column in range(columns):
                num = multiply_helper(matrix, orig_matrix, row, column)
                row_list.append(num)
            final_matrix.append(row_list)

        final_matrix = np.array(final_matrix)
        return final_matrix

    else:
        print("The number of rows and columns should match")


def power():
    matrix = matrix_creator(rows, columns)
    final_matrix = matrix
    power = int(input("What power do you want to raise the matrix to?\n"))

    while power > 1:
        final_matrix = power_helper(final_matrix, matrix)
        power -= 1

    print(final_matrix)


# Operations: Addition, Subtraction, Transpose, Power, Multiplication
print("Welcome to Matrix calculator!")

operation_list = {
    'a': 'addition',
    's': 'subtraction',
    'm': 'multiplication',
    't': 'transpose',
    'p': 'power'
}

operation = input("Please select the type of operation you'd like: Addition(A), Subtraction(S), Multiplication(M), "
                  "Transpose(T), Power(P)\n").lower()
valid_operation = False

while operation.isdigit():
    operation = input("Please enter a valid input!\n")

while not valid_operation:
    if len(operation) == 1:
        operation = operation_list[operation]
        valid_operation = True
    else:
        print("Sorry, your input isn't one of the options. Please enter a valid input")
        operation = input("Please select the type of operation you'd like: Addition(A), Subtraction(S), Multiplication(M), "
                    "Transpose(T), Power(P)\n").lower()

try:
    rows = int(input("How many rows in the matrix?\n"))
    columns = int(input("How many columns in the matrix?\n"))
except ValueError:
    print("Invalid input. Please try again")
    exit()

if operation == 'addition':
    add()
elif operation == 'subtraction':
    subtract()
elif operation == 'multiplication':
    multiply()
elif operation == 'transpose':
    transpose()
elif operation == 'power':
    power()
