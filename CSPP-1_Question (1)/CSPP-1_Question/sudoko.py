def print_grid(arr): 
    for i in range(9): 
        print(arr[i]) 
def create_set(g, row, col):
    lis= set()
    for i in range(9):
        if g[row][i] != '0':
            lis.add(g[row][i])
        if g[i][col] != '0':
            lis.add(g[i][col])
    return lis

def possibilities(g):
    for i in range(9):
        for j in range(9):
            res = ""
            s = set()
            if g[i][j] == '0':
                s = create_set(g, i, j)
                # print(s)
            if len(s) != 0:
                for each in "123456789":
                    if each not in s:
                        res += each
                print(res)

if __name__=="__main__": 
      
    # creating a 2D array for the grid 
    grid=[['0' for x in range(9)]for y in range(9)] 
    print_grid(grid)
      
    given_input = input()
    k = 0
    for i in range(9):
        for j in range(9):
            if given_input[k] != '.':
                grid[i][j] = given_input[k]
            k += 1
    print_grid(grid)
    possibilities(grid)
