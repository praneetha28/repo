def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    res = [[0 for row in range(len(m1))] for col in range(len(m1[0]))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            for k in range(len(m2)):
                res[i][j] += m1[i][k]*m2[k][j]
    return res

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    res = [[0 for row in range(len(m1))] for col in range(len(m1[0]))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res[i][j] = m1[i][j]+m2[i][j]
    return res
    


def read_matrix(matrix,row):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    for i in range(row[0]):
        a= input().split(' ')
        if len(a) == row[1]:
            matrix.append(list(map(int, a)))
        else:
            print('Error: Invalid input for the matrix')
            return None
    
def main():
    row=list(map(int,input().split(',')))
    matrix1=[]
    if read_matrix(matrix1,row):
        exit
    
    row1=list(map(int,input().split(',')))
    matrix2=[]
    if read_matrix(matrix2,row1):
        exit
    
    #print(add_matrix(matrix1, matrix2))
    #print(mult_matrix(matrix1, matrix2))


   
if __name__ == '__main__':
    main()
