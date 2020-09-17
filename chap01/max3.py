# 세 정수를 입력받아 최댓값 구하기

print('세 정수를 입력하세요')
a = int(input('정수 a의 값을 입력하세요 : '))
b = int(input('정수 b의 값을 입력하세요 : '))
c = int(input('정수 c의 값을 입력하세요 : '))

maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c

print('최댓값은 {0} 입니다.'.format(maximum))
