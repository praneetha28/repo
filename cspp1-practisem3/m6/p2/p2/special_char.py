"'# enter the input'"
S = input()
L = len(S)
for i in S:
    if i in '!@#$%^&*':
        S1 = " "
        print(S1)
    else:
        print(S)
