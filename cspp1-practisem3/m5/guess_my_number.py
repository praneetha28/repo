i = input(" Please think of a number between 0 and 100!")
low = 0
high = 100
ans = int((low + high)/2)
print(" Is this your secret number " + str(ans) + "?" )
inpt = input("Enter 'h' to indicate the guess is too high . Enter 'l' to indicate the guess is to low. Enter 'c' to indicate I guessed correctly.")
while inpt != 'c':
    if inpt == 'h':
        high = ans
        ans =int((low + high)/2)
        print(" Is this your secret number " + str(ans) + "?" )
        inpt = input("Enter 'h' to indicate the guess is too high . Enter 'l' to indicate the guess is to low. Enter 'c' to indicate I guessed correctly.")

    if inpt == 'l':
        low = ans
        ans = int((low + high)/2)
        print(" Is this your secret number " + str(ans) + "?" )
        inpt = input("Enter 'h' to indicate the guess is too high . Enter 'l' to indicate the guess is to low. Enter 'c' to indicate I guessed correctly.")
    else:
        print("Sorry, I did not understand your input.")
        print(" Is this your secret number " + str(ans) + "?" )
        inpt = input("Enter 'h' to indicate the guess is too high . Enter 'l' to indicate the guess is to low. Enter 'c' to indicate I guessed correctly.")


if inpt == 'c':
    print(" Game over. Your secret number was:" + str(ans))
