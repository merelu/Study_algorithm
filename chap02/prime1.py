# 1,000이하의 소수를 나열하기
# 소수 2부터 n-1까지 어떤 정수로도 나누어 떨어지지 않는다.
counter = 0  # 나눗셈 횟수를 카운트

for i in range(2, 18):
    for j in range(2, i):
        counter += 1
        if i % j == 0:
            break
    else:
        print(i)

print(f'나눗셈을 실행한 횟수: {counter}')
