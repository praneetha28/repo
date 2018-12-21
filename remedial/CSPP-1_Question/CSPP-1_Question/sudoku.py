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


def main():
    input1 = input()
    print(len(input1))
    grid=[['0' for x in range(9)]for y in range(9)]
    if len(input1) != 81:
        print("Invalid input")
    else:
        k = 0
        for i in range(9):
            for j in range(9):
                if input1[k] != '.':
                    grid[i][j] = input1[k]
                k += 1
    # if k == 9:
    #     checkSudoku(grid)
    # else:
        possibilities(grid)

if __name__ == '__main__':
    main()