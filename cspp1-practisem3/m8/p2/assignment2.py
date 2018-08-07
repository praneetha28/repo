"'# Exercise: Assignment-2'"
# Write a Python function, sumofdigits, that takes in one number
def sumofdigits(num):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of num.
    '''
    if num == 0:
        return 0
    return num%10 + sumofdigits(num//10)

def main():
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of num.
    '''
    a_n = input()
    print(sumofdigits(int(a_n)))

if __name__ == "__main__":
    main()
