"'# enter input'"
N = int(input())
SUM = 1
if N == 0:
    print(N)
elif N < 0:
    while abs(N) > 0:
        SUM = SUM * (abs(N) % 10)
        N = int(abs(N)/10)
    SUM = -SUM
    print(SUM)

else:
    while N > 0:
        SUM = SUM * (N % 10)
        N = int(N/10)
    print(SUM)
