"""
Tic Tac Toe solver using minimax. 

Starting with invent with python's game, 
making improvements once I have a working board.


I want to move to an oop model, clean up some
functions, and use minimax instead of random

https://inventwithpython.com/invent4thed/chapter10.html
"""

import random

def main():
    def chooseXY(choice):
        choice = choice.upper().strip()
        if choice in ["X", "O"]:  
            if choice == "X":
                playerSymbol = "X"
                cpuSymbol = "O"
            else:
                playerSymbol = "O"
                cpuSymbol = "X"
        else:
            playerSymbol = "O"
            cpuSymbol = "X"
            print("Please choose either X or O next time.")
            
        print("You chose", playerSymbol)
        return playerSymbol

    def printBoard(explain=False):
        if explain:
            print("This is the way the columns are named.")
            print("7 8 9 \n4 5 6 \n1 2 3\n")
            
        print(board[7] + '|' + board[8] + '|' + board[9])
        print('-+-+-')
        print(board[4] + '|' + board[5] + '|' + board[6])
        print('-+-+-')
        print(board[1] + '|' + board[2] + '|' + board[3])

    def goesFirst():
        #if 0 cpu goes first, if 1 player goes first
        index = random.randint(0, 1)
        first = ["player", "cpu"]
        return first[index]

    def makeMove(board, letter, move):
        board[move] = letter

    def isWinner(b, x):
        return ((b[7] == x and b[8] == x and b[9] == x) or # Across the top
        (b[4] == x and b[5] == x and b[6] == x) or # Across the middx
        (b[1] == x and b[2] == x and b[3] == x) or # Across the bttom
        (b[7] == x and b[4] == x and b[1] == x) or # Down the xft side
        (b[8] == x and b[5] == x and b[2] == x) or # Down the middx
        (b[9] == x and b[6] == x and b[3] == x) or # Down the right side
        (b[7] == x and b[5] == x and b[3] == x) or # Diagonal
        (b[9] == x and b[5] == x and b[1] == x))   # Diagonal
            

    def getPlayerMove(board):
        move = " "
        possible = "1 2 3 4 5 6 7 8 9".split()
        while move not in possible or not isSpaceFree(board, int(move)):
                move = input("What is your next move (1-9)? ")
        return int(move)

    def isSpaceFree(board, move):
        return board[move] == " "


    def chooseRandomMove(board, movesList):
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) > 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getBoardCopy(board):
        boardCopy = []
        for i in board:
            boardCopy.append(i)
        return boardCopy


    def getComputerMove(board, cpuSymbol):
        #check if cpu can win with next move
        for i in range(1, 10):
            boardCopy = getBoardCopy(board)
            if isSpaceFree(boardCopy, i):
                makeMove(boardCopy, cpuSymbol, i)
                if isWinner(boardCopy, cpuSymbol):
                    return i
        
        for i in range(1, 10):
            #check if player can win with next move
            boardCopy = getBoardCopy(board)
            if isSpaceFree(boardCopy, i):
                makeMove(boardCopy, playerSymbol, i)
                if isWinner(boardCopy, playerSymbol):
                    return i
        #center
        if isSpaceFree(board, 5):
            return 5
        #corners
        move = chooseRamdomMove(board, [1, 3, 7, 9])
        if move != None:
            return move
        #sides
        return chooseRandomMove(board, [2, 4, 6, 8])


    def isBoardFull(board):
        for i in range(1, 10):
            if isSpaceFree(board, i):
                return False
            else:
                return True


    while True:
        playerSymbol = ""
        cpuSymbol = ""
        board = [" "] * 10
        
        symbol = input("Would you like to be X or O?  ")
        chooseXY(symbol)
        #printBoard(True) tells the user the names of the slots
        printBoard(True)

        turn = goesFirst()
        print(turn, "will go first")
                

    

main()
