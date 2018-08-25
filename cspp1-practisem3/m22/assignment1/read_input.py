'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''main function'''
    num = int(input())
    lines = ""
    for _ in range(num):
        lines += input() + "\n"
    print(lines)

if __name__ == '__main__':
    main()
