# *을 n개 출력하되 w개마다 줄바꿈 하기

print('*을 출력합니다.')
n = int(input('몇 개를 출력할까요? : '))
w = int(input('몇 개마다 줄바꿈할까요? : '))

for _ in range(n//w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)
