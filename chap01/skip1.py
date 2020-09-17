# 1~12까지 8을 건너뛰고 출력하기1

for i in range(1, 13):
    if(i == 8):
        continue

    print(f'{i}', end=' ')
