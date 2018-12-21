def create_set(g, r, c):
    lis = set()
    for i in range(9):
        if g[r][i] != '0':
            lis.add(g[r][i])
        if g[i][c] != '0':
            lis.add(g[i][c])
    return lis

def possibilities(mat):
    for i in range(9):
        for j in range(9):
            res = ""
            s = set()
            if mat[i][j] == '0':
                s = create_set(mat, i, j)
                # print(s)
            if len(s) != 0:
                for each in "123456789":
                    if each not in s:
                        res += each
                print(res)

def checkSudoku(sudoku):
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
    input1 = input()
    grid=[['0' for x in range(9)]for y in range(9)]
    if len(input1) != 81:
        print("Invalid input")
    else:
        k = 0
        count = 0
        for i in range(9):
            for j in range(9):
                if input1[k] != '.':
                    grid[i][j] = input1[k]
                else:
                    count += 1
                k += 1
    # print(count)
    if count == 0:
        if checkSudoku(grid):
            print("Given sudoku is solved")
        else:
            print("Invalid Sudoku:Duplicate values")
    else:
        possibilities(grid)

if __name__ == '__main__':
    main()