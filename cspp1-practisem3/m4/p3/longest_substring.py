"'#enter string'"
S = input()
S1 = S[0]
L = ' '
for i in range(1, len(S)):
    if S1[-1] <= S[i]:
        S1 = S1 + S[i]
    else:
        if len(S1) > len(L):
            L = S1
        S1 = S[i]
if len(S1) > len(L):
    L = S1
print(L)
