# 2자리 양수(10~99) 입력받기

print('2자리 양수를 입력하세요')

while True:
    num = int(input('양수를 입력하세요. : '))
    if num >= 10 and num <= 99:
        break

print(f'입력받은 숫자는 {num}입니다.')
