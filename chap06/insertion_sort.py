# 단순 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence


def insertion_sort(a: MutableSequence) -> None:
    """단순 삽입 정렬 """
    n = len(a)
    # 비교할 대상이 필요하다 0번째 인덱스의 값과 비교하기 때문에 1~n까지 범위로 반복한다.
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp


if __name__ == "__main__":
    print("단순 삽입 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.:"))
    x = [None] * num  # 원소수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    insertion_sort(x)  # 배열 x를 단순 삽입정렬

    print("오름차순으로 정렬했습니다.")

    for i in range(num):
        print(f"x[{i}] = {x[i]}")
