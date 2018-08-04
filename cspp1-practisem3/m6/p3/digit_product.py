"'# enter input'"
N = int(input())
SUM = 1
while abs(N) > 0:
    SUM = SUM * (abs(N) % 10)
    N = int(abs(N)/10)
SUM = -SUM
print(SUM)
