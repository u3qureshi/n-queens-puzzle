# START OF CLASS ----------------

totalSolutions = 0

class Puzzle:

    def __init__(self,N):
        self.N = N
    
    def displayBoard(self, BOARD):
        print('------------')
        for i in range(self.N):
            for j in range(self.N):
                print(BOARD[i][j], end=' ')
            print('')

    # Method to check if a position is safe to place a queen
    def isSafe(self, BOARD, row, column):

        # Check the column of the queen
        for i in range(self.N):
            if (BOARD[i][column] == 1):
                return False

        # Check the left side of the row
        for j in range(self.N):
            if (BOARD[row][j] == 1):
                return False

        # Check the left side upper diagonal
        for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
            if (BOARD[i][j] == 1):
                return False

        # Check the left side lower diagonal
        for i, j in zip(range(row, self.N, 1), range(column, -1, -1)):
            if (BOARD[i][j] == 1):
                return False
        
        # Check the right side upper diagonal
        for i, j in zip(range(row, -1, -1), range(column, self.N, 1)):
            if (BOARD[i][j] == 1):
                return False

        # Check the right side lower diagonal
        for i, j in zip(range(row, self.N, 1), range(column, self.N, 1)):
            if (BOARD[i][j] == 1):
                return False

        # Return true if all tests are passed and queen can safely be placed
        return True

    def placeQueen(self,BOARD, row):
        
        global totalSolutions

        # Base case
        if (row == self.N):
            self.displayBoard(BOARD)
            totalSolutions += 1
            return True
        
        for c in range(self.N):
            if (self.isSafe(BOARD, row, c)):
                # If the queen is safe to place without attack, then place queen at current location
                BOARD[row][c] = 1
                    
                # Recurse to the next row ++
                self.placeQueen(BOARD, row + 1)

                # Backtrack and undo queen placement
                BOARD[row][c] = 0
        return False

# END OF CLASS ----------------

# MAIN SECTION
while(True):
    try:
        N = int(input("Enter the value of N between 1 - 10: "))
    except:
        print('Please enter a valid integer between 1-10')
        continue

    if (N>=1 and N<=10 and type(N)==int):
        loop = False
        break
    
    print('Please enter a valid integer between 1-10')


BOARD = [[0 for i in range(N)] for j in range(N)]
Puzzle(N).placeQueen(BOARD, 0)
print(f'There exists {totalSolutions} total solutions to the {N}-Queens puzzle.')
