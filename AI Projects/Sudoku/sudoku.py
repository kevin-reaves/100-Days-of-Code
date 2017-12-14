from createBoard import board


def verifyBoard(board):
    if not board:
        return false
    if len(board) != 9:
        return False

    for row in board:
        if len(row) != 9:
            return False
    return True

def printBoard(board):

    for row in range(9):
        if row % 3 == 0:
            print("\n")
        print(str(board[row][:3]) + "  " +
              str(board[row][3:6]) + "  " +
              str(board[row][6:]))



if verifyBoard(board):
    printBoard(board)
else:
    print("Your board isn't structured correctly")