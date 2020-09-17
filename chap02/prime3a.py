counter = 0
prime = [2, 3]

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime += [n]
        counter += 1

for i in prime:
    print(i)
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')
