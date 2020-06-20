# A Backtracking program in Python to solve Sudoku puzzles(standard 9x9 format)

# TO PRINT SUDOKU
def printGrid(A):
    print("\nSOLUTION IS")
    for i in range(9):
        print(" ".join(str(x) for x in A[i]))

#TO FIND ALL EMPTY LOCATIONS MARKED BY '0'
# Function to Find the entry in the Grid that is still not used 
# Searches the grid to find an entry that is still unassigned(0). If 
# found, the reference parameters for row, col will be set the location 
# and true is returned, otherwise false is returned. 
def findEmptyLocation(A,l):
    for row in range(9):
        for col in range(9):
            if(A[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False

#CHECKS WHETHER NUMBER ALREADY EXISTS IN ROW
# Returns a boolean which indicates whether any assigned entry 
# in the specified row matches the given number.
def usedInRow(A,row,num):
    for i in range(9):
        if(A[row][i] == num):
            return True
    return False

#CHECKS WHETHER NUMBER ALREADY EXISTS IN COLUMN
# Returns a boolean which indicates whether any assigned entry 
# in the specified column matches the given number. 
def usedInCol(A,col,num):
    for i in range(9): 
        if(A[i][col] == num):
            return True
    return False

#CHECKS WHETHER NUMBER ALREADY EXISTS IN MINIGRID
# Returns a boolean which indicates whether any assigned entry 
# within the specified 3x3 grid matches the given number
def usedInMiniGrid(A,row,col,num):
    for i in range(3):
        for j in range(3):
            if(A[i+row][j+col] == num):
                return True
    return False

#CHECKS IF A LOCATION IS SAFE
# Checks whether it will be legal to assign num to the given row, col 
# Returns a boolean which indicates whether it will be legal to assign 
# num to the given row, col location.
def check(A,row,col,num):
    # Check if 'num' is not already placed in current row, 
	# current column and current 3x3 grid
    return not usedInRow(A,row,num) and not usedInCol(A,col,num) and not usedInMiniGrid(A,row - row%3,col
- col%3,num)

#MAIN SOLVING FUNCTION
# Takes a partially filled-in grid and attempts to assign values to 
# all unassigned locations in such a way to meet the requirements 
# for Sudoku solution (non-duplication across rows, columns, and boxes)
def solveSudoku(A):
    
    l=[0,0]

    if(not findEmptyLocation(A,l)):
        return True
    
    row=l[0]
    col=l[1]
    
    for num in range(1,10):
        if(check(A,row,col,num)):
            A[row][col]=num
            
            if(solveSudoku(A)):
                return True
                
            A[row][col] = 0
    return False
    # this triggers backtracking

sudoku = []

for i in range(9):
    temp = list(map(int,input().split()))
    sudoku.append(temp)

#IF SUCCESS THEN PRINT SUDOKU
if(solveSudoku(sudoku)):
    printGrid(sudoku)
else:
    print ("No solution exists")