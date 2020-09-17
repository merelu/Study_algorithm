# *를 n개마다 줄 바꿈을 하는 프로그램

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요? : '))
w = int(input('몇 개 마다 줄바꿈 할 까요? : '))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()

if n % w:
    print()
