"'# enter the input'"
NUM = int(input())
SUM = 0
while SUM**3 < abs(NUM):
    SUM = SUM + 1

if SUM**3 != abs(NUM):
    print(str(NUM) + ' is not a perfect cube')
else:
    if NUM < 0:
        SUM = - SUM
    print(str(NUM) + ' is a perfect cube')
