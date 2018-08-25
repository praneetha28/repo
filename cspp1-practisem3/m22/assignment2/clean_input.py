'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''function to remove special characters'''
    input1 = string.lower()
    input1 = re.sub('[^a-zA-Z0-9]+', '', input1)
    return input1

def main():
    '''main function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
