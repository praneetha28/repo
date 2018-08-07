# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
    


def main():
    data = input()
    data = data.split()
    print(gcdRecur(int(data[0]),int(data[1])))

if __name__== "__main__":
    main()
