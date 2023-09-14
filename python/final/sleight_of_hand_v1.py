def game_score(k: int, matrix: list[list[int]]) -> int:
    pass


k = int(input())
matrix = list()
for i in range(4):
    matrix.append(map(int, input().strip().replace('.', '0').split()))

print(matrix)

print(game_score(k, matrix))