"' #enter the string'"
S = input()
COUNT = 0
L = int(len(S))
i = 0
j = 3
"'#CHECKING THE RANGE'"
while j <= L:
    Z = S[i:j]
    if Z == "bob":
        COUNT = COUNT + 1
    i = i+1
    j = j+1

print(COUNT)
