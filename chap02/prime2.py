# 1,000이하의 소수를 나열하기(알고리즘 개선1)

counter = 0
ptr = 0
prime = [None] * 500  # 소수를 저장하는 배열

prime[0] = 2
ptr += 1

# 홀수만을 대상으로 2는 이미 소수임을 알기 때문에 2로 나눠지는 짝수는 소수가 될 수 없다.
for n in range(3, 1001, 2):
    for i in range(1, ptr):
        counter += 1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])
print(f'나눗셈을 실행한 횟수: {counter}')
