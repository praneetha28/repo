"'#enter the output'"
N = int(input())
i = 1
for i in range(1, N+1):
    if i == 1:
        print(i)
for i in range(2, N+1):
    if i%3 == 0 and i%5 == 0:
        print('Fizz')
        print('Buzz')
    elif i%5 == 0:
        print('Buzz')
    elif i%3 == 0:
        print('Fizz')
    else:
        print(i)
