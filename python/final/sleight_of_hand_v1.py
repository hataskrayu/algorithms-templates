length = int(input())
number_list = list(map(int, input().strip().split()))


k = int(input())
matrix = []
for i in range(4):
    matrix.append(list(map(int, input().strip().split())))

print_result(to_nearest_zero(length, number_list))