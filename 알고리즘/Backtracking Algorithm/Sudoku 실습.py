def print_sudoku(board):  # 점검용
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")


def solve_sudoku(A):
    row, col = find_empty_cell(A)
    if row == None:
        return True
    for num in range(1, 10):
        if is_safe(A, row, col, num):
            A[row][col] = num
            if solve_sudoku(A):
                return True
    A[row][col] = 0
    return False


def find_empty_cell(A):
    for row in range(9):
        for col in range(9):
            if A[row][col] == 0:
                return row, col
    return None, None


def is_safe(A, row, col, num):
    return not is_in_row(A, row, num) and not is_in_col(A, col, num) and not is_in_box(A, row//3, col//3, num)


def is_in_row(A, row, num):
    return num in A[row]


def is_in_col(A, col, num):
    for row in range(9):
        if A[row][col] == num:
            return True
    return False


def is_in_box(A, r, c, num):
    row, col = r*3, c*3
    for i in range(3):
        for j in range(3):
            if A[row+i][col+j] == num:
                return True
    return False

    # A를 sudoku 규칙에 맞게 채운다
