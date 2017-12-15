from createBoard import board


def verifyBoard(board):
    # Tries to make sure the board is the proper 9x9 shape
    if not board:
        return false

    if len(board) != 9:
        return False

    for row in board:
        if len(row) != 9:
            return False

    return True


def printBoard(board):
    # Prints the board to screen
    for row in range(9):
        # Newline to seperate a "box" every 3 lines
        if row % 3 == 0:
            print("\n")
            # Prints first 3, middle 3, last 3
        print(str(board[row][:3]) + "  " +
              str(board[row][3:6]) + "  " +
              str(board[row][6:]))


def usedInRow(board, row, num):
    for i in range(9):
        if board[row][i] == num:
            return True

    return False


def usedInColumn(board, column, num):
    for i in range(9):
        if board[i][column] == num:
            return True

    return False


def usedInBox(board, row, column, num):
    # Checks to make sure each number in the 3x3 box is only used once
    for i in range(3):
        for j in range(3):
            if (board[i + row][j + column] == num):
                return True

    return False


def isSafe(board, row, column, num):
    # Checks to make sure row/column/box rules are followed
    # row - row % 3 is going to pass either 0, 3, or 6. Box will add 0, 1, or 2
    if not usedInRow(board, row, num) and \
            not usedInColumn(board, column, num) and \
            not usedInBox(board, (row - row % 3), (column - column % 3), num):
        return True

    return False


def findEmpty(board, check):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                check["row"] = row
                check["column"] = column
                return True

    return False


def solveBoard(board):
    # Check allows backtracking by keeping track of the last spot
    check = {"row": 0, "column": 0}

    if not findEmpty(board, check):
        return True

    row = check["row"]
    column = check["column"]

    # Python's in range operator returns exclusive [start, finish)
    for num in range(1, 10):
        if isSafe(board, row, column, num):

            board[row][column] = num

            if solveBoard(board):
                return True

            board[row][column] = 0
    return False


if verifyBoard(board):
    printBoard(board)

    if solveBoard(board):
        print("\n Here is your solution")
        printBoard(board)

    else:
        print("\n I don't think this board is solvable")

else:
    print("Your board isn't structured correctly")
