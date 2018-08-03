"'# enter the string'"
NUM = int(input())
N = 0.01
G = 0.0
INCREMENT = 0.1
while abs(G**2 - NUM) >= N:
    G += INCREMENT

if abs(G**2 - NUM) >= N:
    print(' failed ')
else:
    print(G)
