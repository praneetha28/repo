"'# enter input'"
N = int(input())
SUM = 1

if N == 0:
    print(N)
else:
    while abs(N) > 0:
        SUM = SUM * (abs(N) % 10)
        N = int(abs(N)/10)
        SUM = -SUM
    print(SUM)
