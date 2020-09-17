from typing import Any, Sequence

# 건네받는 매개변수 a의 자료형은 Sequence입니다.
# 반환하는 것은 임의의 자료형인 Any입니다.
# 아래처럼 표시해 주는 것을 annotation:주석달기 라고 한다. typescript방식 비슷


def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num  # 원소 수가 num인 리스트를 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

    print(f'최댓값은 {max_of(x)}입니다.')
