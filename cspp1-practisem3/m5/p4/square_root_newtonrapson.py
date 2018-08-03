"'#enter the input'"
N = 0.01
NUM = int(input())
G = NUM/2.0
while abs(G*G - NUM) >= N:
    G = G - (((G**2) - NUM)/(2*G))

print(G)
