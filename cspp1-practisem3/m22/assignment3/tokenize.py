'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    '''token function'''
    input1 = re.split(r'[^a-zA-Z0-9]', string.strip())
    while '' in input1:
        input1.remove('')
    dict1 = {}
    for word in input1:
        dict1[word] = input1.count(word)
    return dict1

def main():
    '''main function'''
    num = int(input())
    input1 = ""
    for _ in range(num):
        input1 += input()
    print(tokenize(input1))

if __name__ == '__main__':
    main()
