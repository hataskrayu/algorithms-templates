from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    first_number = first_number[::-1]
    second_number = second_number[::-1]
    length1 = len(first_number)
    length2 = len(second_number)
    size = max(length1, length2)
    first_number += str('0' * (size - length1))
    second_number += str('0' * (size - length2))
    carry = False
    result = ''
    for i in range(0, size):
        if first_number[i] == second_number[i] == '0':
            if carry:
                result += '1'
                carry = False
            else:
                result += '0'
        elif first_number[i] == second_number[i] == '1':
            if carry:
                result += '1'
            else:
                result += '0'
                carry = True
        else:
            if carry:
                result += '0'
            else:
                result += '1'
                carry = False
        
    if carry:
        result += '1'
    return result[::-1]
            
                    

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))
