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
        row = 0
        for i in range(9):
            if len(sudoku[i]) == 9:
                row += 1
        if row == 9:
            if checkrow(sudoku):
                if checkcol(sudoku):
                    return True
                return False
            else:
                return False
        else:
            return False
    else:
        return False

def checkrow(sudoku):
    for i in range(9):
        rowlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(9):
            rowlist[int(sudoku[i][j])] += 1
        temprow = rowlist[1:10]
        for q in range(9):
            if temprow[q] == 1 or temprow[q] == 0:
                continue
            return False
    return True
def checkcol(sudoku):
    for num in range(9):
        rowlist1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            rowlist1[int(sudoku[i][num])] += 1
        temprow1 = rowlist1[1:10]
        for q in range(9):
            if temprow1[q] == 1 or temprow1[q] == 0:
                continue
            return False
    return True

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