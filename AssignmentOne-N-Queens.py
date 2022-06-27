# START OF CLASS ----------------
class Puzzle:

    def __init__(self,N):
        self.N = N
        self.BOARD = [[0 for i in range(self.N)] for j in range(self.N)]
    
    def displayBoard(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.BOARD[i][j], end=' ')
            print('')

    # Method to check if a position is safe to place a queen
    def isSafe(self, row, column):

        # Check the column of the queen
        for i in range(self.N):
            if (self.BOARD[i][column] == 1):
                return False

        # Check the left side of the row
        for j in range(self.N):
            if (self.BOARD[row][j] == 1):
                return False

        # Check the left side upper diagonal
        for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
            if (self.BOARD[i][j] == 1):
                return False

        # Check the left side lower diagonal
        for i, j in zip(range(row, self.N, 1), range(column, -1, -1)):
            if (self.BOARD[i][j] == 1):
                return False
        
        # Check the right side upper diagonal
        for i, j in zip(range(row, -1, -1), range(column, self.N, 1)):
            if (self.BOARD[i][j] == 1):
                return False

        # Check the right side lower diagonal
        for i, j in zip(range(row, self.N, 1), range(column, self.N, 1)):
            if (self.BOARD[i][j] == 1):
                return False

        # Return true if all tests are passed and queen can safely be placed
        return True

    def placeQueen(self, queenCount):

        # Base case
        if (queenCount == self.N):
            return True
        
        for row in range(self.N):
            for col in range(self.N):
                if (self.isSafe(row, col)):
                    self.BOARD[row][col] = 1
                    queenCount += 1
                    if (self.placeQueen(queenCount) == True):
                        return True
                    else:
                        self.BOARD[row][col] = 0
                        queenCount -= 1
        return False

# END OF CLASS ----------------

puzzle = Puzzle(int(input("Enter the value of N: ")))
puzzle.placeQueen(0)
puzzle.displayBoard()