# a부터 b까지 정수의 합 구하기

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('a의 값을 입력하세요 : '))
b = int(input('b의 값을 입력하세요 : '))

if (a > b):
    a, b = b, a
sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end='')
sum += b

print(sum)
