#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    s = input("enter string")
    VOWELS = 0
    "'#CHECKING THE THE RANGE'"
    for char in s:
     if char in'aeiou':
      VOWELS = VOWELS + 1

    print('number of vowels:', VOWELS)
 

if __name__== "__main__":
	main()
