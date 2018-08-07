"'# Exercise: Assignment-1'"
# Write a Python function, factorial(n),

def factorial(num):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if num == 0:
        return 1
    return num * factorial(num-1)

def main():
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    a_n = input()
    print(factorial(int(a_n)))

if __name__ == "__main__":
    main()
