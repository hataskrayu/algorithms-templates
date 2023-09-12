from typing import List

def factorize(number: int) -> List[int]:
    result = []
    divider = 2
    while divider * divider <= number:
        if number % divider == 0:
            result.append(divider)
            number = int(number / divider)
        else:
            divider += 1
    if number > 1:
        result.append(number)
    return result

result = factorize(int(input()))
print(" ".join(map(str, result)))
