'''program'''
def mult_matrix(mat_m1, mat_m2):
    ''' check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(mat_m1[0]) == len(mat_m2) and len(mat_m1[0]) == len(mat_m2):
        res = [[0 for row in range(len(mat_m1))] for col in range(len(mat_m2[1]))]
        for i in range(len(mat_m1)):
            for j in range(len(mat_m2[1])):
                for k in range(len(mat_m2)):
                    res[i][j] += mat_m1[i][k]*mat_m2[k][j]
        return res
    print("Error: Matrix shapes invalid for mult")
    return None

def add_matrix(mat_m1, mat_m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(mat_m1) == len(mat_m2) and len(mat_m1[0]) == len(mat_m2[0]):
        res = [[0 for row in range(len(mat_m1[0]))] for col in range(len(mat_m1))]
        for i in range(len(mat_m1)):
            for j in range(len(mat_m1[0])):
                res[i][j] = mat_m1[i][j] + mat_m2[i][j]
        return res
    print("Error: Matrix shapes invalid for addition")
    return None

def read_matrix(row):
    ''' read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    for i in range(row[0]):
        input_a = list(map(int, input().split(' ')))
        if len(input_a) == row[1]:
            matrix.append(input_a)
        else:
            print('Error: Invalid input for the matrix')
            return None
    return matrix

def main():
    '''main function'''
    row = list(map(int, input().split(',')))
    matrix1 = read_matrix(row)
    row1 = list(map(int, input().split(',')))
    matrix2 = read_matrix(row1)
    if matrix1 is not None and matrix2 is not None:
        print(add_matrix(matrix1, matrix2))
        print(mult_matrix(matrix1, matrix2))


if __name__ == '__main__':
    main()
