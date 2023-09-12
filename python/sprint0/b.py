from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    l = list()
    for i in range(0, len(a)):
        l.append(a[i])
        l.append(b[i])
    return l


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
