'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 sudoku with digits so that
    each column, each row, and each of the nine 3×3 subsudokus that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    if len(sudoku) == 9:
        numsinrow = 0
        for i in range(9):
            if len(sudoku[i]) == 9:
                numsinrow += 1
        if numsinrow == 9:
            if checkrow(sudoku):
                if checkcol(sudoku):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def checkrow(sudoku):
    for i in range(9):
        rowoccurence = [0,0,0,0,0,0,0,0,0,0]
        for j in range(9):
            rowoccurence[int(sudoku[i][j])] += 1
        temprow = rowoccurence[1:10]
        for q in range(9):
            if temprow[q] == 1 or temprow[q] == 0:
                continue
            else:
                return False
    return True
def checkcol(sudoku):
    for num in range(9):
        coloccurence = [0,0,0,0,0,0,0,0,0,0]
        for i in range(9):
            coloccurence[int(sudoku[i][num])] += 1
        tempcol = coloccurence[1:10]
        for q in range(9):
            if tempcol[q] == 1 or tempcol[q] == 0:
                continue
            else:
                return False
    return True

        #ninrows = 0
        #for i in range(9):
         #   if len(sudoku[i]) == 9:
          #      ninrows += 1
        #if ninrows == 9:
         #   for i in range(9):
          #      row = [0,0,0,0,0,0,0,0,0]
           #     for j in range(9):
            #        row[int(sudoku[i][j])] += 1
             #   temprow = row[1:10]
                 

    

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()