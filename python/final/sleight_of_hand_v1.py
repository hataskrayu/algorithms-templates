# ID 90573370

# Проверяет нас python 3.7.3. На нём с обычным list не работает.
from typing import List, Tuple

FIELD_SIZE = 4
MAX_NUMBER = 10


def game_score(k: int, matrix: List[int]) -> int:
    # Сразу определим количество нажатий
    k *= 2
    score = 0
    # Создадим список с количеством кнопок каждого вида
    buttons_list = [0] * MAX_NUMBER
    for i in range(0, FIELD_SIZE * FIELD_SIZE):
        buttons_list[matrix[i]] += 1
    # Считаем баллы. "Нулевую" игру игнорируем.
    for i in range(1, MAX_NUMBER):
        if (0 < buttons_list[i] <= k):
            score += 1
    return score


def read_input() -> Tuple[int, List[int]]:
    k = int(input())
    matrix = list()
    # Так как по задаче, структура именно матрицы нам не нужна,
    # считаем её построчно, но сохраним сразу в удобном виде:
    # одномерный массив int, "." приводим к 0.
    for i in range(FIELD_SIZE):
        matrix += (
            list(
                    map(int, ''.join(input().rstrip().replace(
                        '.',
                        '0',
                    ).split())),
                )
        )
    return (k, matrix)


def main() -> None:
    k, matrix = read_input()
    print(game_score(k, matrix))


if __name__ == '__main__':
    main()
