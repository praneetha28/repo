'''
    Document Distance - A detailed description is given in the PDF
'''
import math
stopwords = "stopwords.txt"
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    list1 = dict1.split(' ')
    list2 = dict2.split(' ')
    list3 = list1 + list2
    dict3 = {}
    for word in list3:
    	if word not in load_stopwords(stopwords).keys():
    		dict3[word] = (dict1.count(word), dict2.count(word))
    num = 0
    sum0 = 0
    sum1 = 0
    for i in dict3:
    	num += dict3[i][0]*dict3[i][1]
    	sum0 += dict3[i][0]**2
    	sum1 += dict3[i][1]**2
    	denom = math.sqrt(sum0)*math.sqrt(sum1)
    return round(num//denom, 1)


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
