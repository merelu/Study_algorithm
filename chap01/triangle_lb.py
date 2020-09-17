# 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
num = int(input('짧은 변의 길이를 입력하세요. : '))

for i in range(num):
    for _ in range(i):
        print('*', end='')
    print()
