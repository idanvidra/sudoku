import numpy as np

# input: board, location to check (column, row) and number
# output: True if placement is possible False if not
def check_if_valid_placement(baord, colmun, row, number):
    # check column
    for i in range(9):
        if board[i][column] == number and row != i:
            return False

    # check row
    for i in range(9):
        if board[row][i] == number and column != i:
            return False

    # check box
    # by box I mean 3x3 sub board to which the location is alocated
    box_row = row // 3 # divison with floor to find the correct box assosiated with the given location
    box_column = column // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_column * 3, box_column * 3 + 3):
            if board[i][j] == number and (i, j) != (row, column):
                return False

    return True

# input: board
# output: location of next empty spot (from top left)
# if no empty spot left return None
def find_unused(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return (row, column)
    return None

# input: board
# ouput: True if solution possible False if not
# uses recursion and backtracking to find possible solution
def solve_sudoku(board):
    find = find_unused(board)
    if not find: # if no empty spots are left on the board the sudoku is done
        return True
    else:
        row, column = find

    for number in range(1,10):
        if check_if_valid_placement(board, column, row, number):
            board[row][column] = number

            if solve_sudoku(board): # if proposed solution works it moves to the next empty spot
                return True

            board[row][column] = 0 # backtracking in case proposed solution is not valid

    return False

def print_board(board):
    for row in range(9):
        for column in range(9):
            print(str(board[row][column]) + " ", end = '')
        print('\n')

# board = np.zeros((9,9), dtype=int)
# board = np.random.randint(10, size=(9, 9))

board = [[1,2,3,4,5,6,7,8,9],
          [7,8,9,1,2,3,4,5,6],
          [0,5,6,7,8,9,1,2,3],
          [3,1,2,8,4,5,9,6,7],
          [6,9,7,3,1,2,8,4,5],
          [8,4,0,6,9,7,3,1,0],
          [2,3,1,5,7,4,6,9,8],
          [9,6,8,2,3,1,5,7,4],
          [0,7,4,9,6,8,2,3,0]]


'''
board = [[1,2,3,4,5,6,7,8,9],
          [7,8,9,1,2,3,4,5,6],
          [4,5,6,7,8,9,1,2,3],
          [3,1,2,8,4,5,9,6,7],
          [6,9,7,3,1,2,8,4,5],
          [8,4,5,6,9,7,3,1,2],
          [2,3,1,5,7,4,6,9,8],
          [9,6,8,2,3,1,5,7,4],
          [5,7,4,9,6,8,2,3,0]]'''
# board[4][5] = 5
print_board(board)
flag = solve_sudoku(board)
print_board(board)
if flag:
    print("sudoku solved")
else:
    print("no solutioun")


