from typing import List, Tuple

def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    neighbours = list()
    coord_list = list()
    coord_list.append((row-1, col))
    coord_list.append((row+1, col))
    coord_list.append((row, col-1))
    coord_list.append((row, col+1))
    for i in coord_list:
        if i[0] >= 0 and i[0] < len(matrix) and i[1] >= 0 and i[1] < len(matrix[0]):
            neighbours.append(matrix[i[0]][i[1]])
    neighbours.sort()
    return neighbours


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col

matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
