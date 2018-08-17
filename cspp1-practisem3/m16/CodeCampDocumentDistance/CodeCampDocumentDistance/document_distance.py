'''
    Document Distance - A detailed description is given in the PDF
'''
import math
STOP_WORDS = "stopwords.txt"
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    lis1 = ''
    lis2 = ''
    for i in dict1:
        for j in i:
            if j not in '!@#$%^&*()_-+=,.?0123456789':
                if j not in "'":
                    lis1 = lis1 + j
    for i in dict2:
        for j in i:
            if j not in '!@#$%^&*()_-+=,.?0123456789':
                if j not in "'":
                    lis2 = lis2 + j

    list1 = lis1.split(' ')
    list2 = lis2.split(' ')
    list3 = list1 + list2
    dict3 = {}
    for word in list3:
        if word not in load_stopwords(STOP_WORDS).keys():
            dict3[word] = (dict1.count(word), dict2.count(word))
    num = 0
    sum0 = 0
    sum1 = 0
    for i in dict3:
        num = num + dict3[i][0]*dict3[i][1]
        sum0 = sum0 + dict3[i][0]**2
        sum1 = sum1 + dict3[i][1]**2
    denom = math.sqrt(sum0) * math.sqrt(sum1)
    return num / denom


def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity functions
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
