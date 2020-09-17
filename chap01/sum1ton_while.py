# 1부터 n까지 정수의 합 구하기 1(while문)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력해주세요. : '))

i = 0
sum = 0

while(i <= n):
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합: {sum}')
print(f'i값은 {i} 입니다')
