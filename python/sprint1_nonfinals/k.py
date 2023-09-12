from typing import List, Tuple

def get_sum(number_list: List[int], k: int) -> List[int]:
    number_list = number_list[::-1]
    k_list = []
    result = []
    carry = 0
    while k > 0:
        modulo = k % 10
        k_list.append(modulo)
        k = int((k - modulo) / 10)
    len1 = len(number_list)
    len2 = len(k_list)
    max_len = max(len1, len2)
    number_list += [0] * (max_len - len1)
    k_list += [0] * (max_len - len2)
    for i in range(0, max_len):
        temp_res = number_list[i] + k_list[i] + carry
        carry = int(temp_res / 10)
        result.append(temp_res % 10)
    if carry:
        result.append(carry)
    return result[::-1]

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k

number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
