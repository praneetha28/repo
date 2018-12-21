"'# enter the input'"
s = input()
L = len(s)
s1 = ''
for i in s:
    if i in '!@#$%^&*':
        i = " "
    s1 += i
print(str(s1))
