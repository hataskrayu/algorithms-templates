# ID 90570161

# Проверяет нас python 3.7.3. На нём с обычным list не работает.
from typing import List


def print_result(result: List[int]) -> None:
    print(" ".join(map(str, result)))


def to_nearest_zero(length: int, number_list: List[int]) -> List[int]:
    result = []
    zero_counter = None
    # Прямой проход, расстояние до нуля слева.
    # До первого нуля оставляем None
    for i in range(0, length):
        if number_list[i] == 0:
            zero_counter = 0
        else:
            if zero_counter is not None:
                zero_counter += 1
        result.append(zero_counter)
    # Обратный проход, расстояние до нуля справа.
    # Оставяем наименьшее значение, заменяем None
    for i in reversed(range(0, length)):
        if number_list[i] == 0:
            zero_counter = 0
        else:
            zero_counter += 1
        if result[i] is None or result[i] > zero_counter:
            result[i] = zero_counter
    return result


def main() -> None:
    length = int(input())
    number_list = list(map(int, input().strip().split()))
    print_result(to_nearest_zero(length, number_list))


if __name__ == '__main__':
    main()
