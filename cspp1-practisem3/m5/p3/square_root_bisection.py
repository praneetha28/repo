"'# enter the input'"
NUM = int(input())
N = 0.01
LOW = 0
HIGH = NUM
G = (LOW + HIGH)/2.0
while abs(G**2 - NUM) >= N:
    if G**2 < NUM:
        LOW = G
    else:
        HIGH = G
    G = (LOW + HIGH)/2.0
print(G)
