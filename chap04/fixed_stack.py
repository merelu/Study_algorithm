from typing import Any


class FixedStack:
    """고정 길이 스택 클래스"""

    class Empty(Exception):
        """비어 있는 FixedStack에 팝 또는 피크할 때 내보내는 예외 처리"""

        pass

    class Full(Exception):
        """가득 찬 FixedStack에 푸시할 때 내보내는 예외 처리 """

        pass

    def __init__(self, capacity: int = 256) -> None:
        """스택 초기화"""
        self.stk = [None] * capacity  # 스택의 본체
        self.capacity = capacity  # 스택의 크기
        self.ptr = 0  # 스택 포인터

    def __len__(self) -> int:
        """스택에 쌓여 있는 데이터 개수를 반환 """
        return self.ptr

    def is_empty(self) -> bool:
        """스택이 비어있나 판단"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """스택이 가득 차 있는지 판단"""
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        """함수가 실행되게 되면 ptr값이 증가하여 예기치 않은 오류를 발생가능하다
        따라서 값이 유효한지 테스트할 필요가 있다."""
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """함수가 실행되게 되면 ptr값이 감소하여 예기치 않은 오류를 발생가능하다(그냥 실행되면 ptr값이 음수가 될 수 있음)
        따라서 값이 유효한지 테스트할 필요가 있다."""
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0

    def find(self, value: Any) -> bool:
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> bool:
        c = 0
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def dump(self) -> None:
        if self.is_empty():
            print("스택이 비어 있습니다.")
        print(f"{self.stk[:self.ptr]}")
