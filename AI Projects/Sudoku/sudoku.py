from createBoard import board


def verifyBoard(board):
    if not board:
        return false
    if len(board) % 3 != 0:
        return False
    else:
        checkLen = len(board)

    for row in board:
        if len(row) != checkLen:
            return False
    return True

def printBoard(board):
    checkLen = len(board)

    for row in range(len(board)):
        if row % 3 == 0:
            print("\n")
        print(str(board[row][:3]) + "  " +
              str(board[row][3:6]) + "  " +
              str(board[row][6:]))



if verifyBoard(board):
    printBoard(board)
else:
    print("Your board isn't structured correctly")