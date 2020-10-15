# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type

import hashlib


class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        # key값이 int형이면
        if isinstance(key, int):
            return key % self.capacity
        #
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]  # 노드를 주목

        while p is not None:
            if p.key == key:
                return p.value  # 검색성공
            p = p.next  # 뒤쪽 노드를 주목

        return None  # 검색 실패

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)  # 추가하는 key의 해시값
        p = self.table[hash]  # 노드를 주목

        while p is not None:
            if p.key == key:
                return False  # 추가실패
            p = p.next  # 뒤쪽 노드를 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp  # 노드를 추가
        return True  # 추가 성공

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)  # 삭제할 key의 해시값
        p = self.table[hash]  # 노드를 주목
        pp = None  # 바로 앞의 노드를 주목

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True  # key 삭제 성공
            pp = p
            p = p.next  # 뒤쪽 노드를 주목
        return False  # 삭제 실패(key가 존재하지 않음)

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end="")
            while p is not None:
                print(f" -> {p.key} ({p.value})", end="")
                p = p.next
            print()
