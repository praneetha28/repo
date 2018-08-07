# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    bisect = len(aStr)//2
    if len(aStr) == 1:
        if aStr[0] == char:
            return "True"
        return "False"
    if len(aStr) == 0:
        return "False"
    if aStr[bisect] == char:
        return "True"
    else:
        if aStr[bisect] > char:
            return isIn(char, aStr[0:bisect])
        else:
            return isIn(char, aStr[bisect:len(aStr)])
   
def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))


if __name__ == "__main__":
    main()
