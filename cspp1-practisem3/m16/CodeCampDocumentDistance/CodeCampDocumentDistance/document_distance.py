'''
    Document Distance - A detailed description is given in the PDF'''
import re
import math
FILE = "stopwords.txt"
def cleanup_words(input1):
    reg = re.compile('[^a-z]')
    input1 = input1.lower()
    input1 = [reg.sub('',w.strip())for w in input1.split(' ')]
    return input1

def remove_wordsdict(input1,input2):
    list3 = cleanup_words(input1) + cleanup_words(input2)
    dic = {}
    for word in list3:
        if word not in load_stopwords(FILE).keys() and len(word) > 0:
            dic[word] = (cleanup_words(input1).count(word), cleanup_words(input2).count(word))
    return dic

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    d1 = {}
    d1 = remove_wordsdict(dict1,dict2)
    num = 0
    denom = 0
    sum0 = 0
    sum1 = 0
    for d1 in d1.values():
        num = num + (d1[0]*d1[1])
        sum0 = sum0 + (d1[0]**2)
        sum1 = sum1 + (d1[1]**2)
    denom = math.sqrt(sum0) * math.sqrt(sum1)
    return (num/denom)


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
