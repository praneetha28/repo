'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 sudoku with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    length = 9
    for row in range(length):
        if row != length:
            return False
    for row in range(length):
        for i in row:
            if i > length:
                return False
    while length > 0:
        for row in range(length):
            for i in row:
                if row.count(i) > 1:
                    return False;
                else:
                    length -= 1
    length = 9
    eachRow = []
    while length > 0:
        for row in range(length):
            eachRow.append(row[length-1])
        for i in eachRow:
            if i > length:
                return False
            elif eachRow.count(i) > 1:
                return False
            else:
                eachRow = []
                length -= 1
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