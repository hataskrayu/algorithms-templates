def print_result(result):
    print(" ".join(map(str, result)))


def to_nearest_zero(length, number_list):
    result = []
    zero_counter = None
    for i in range(0, length):
        if number_list[i] == 0:
            zero_counter = 0
        else:
            if zero_counter is not None:
                zero_counter += 1
        result.append(zero_counter)
    for i in reversed(range(0, length)):
        if number_list[i] == 0:
            zero_counter = 0
        else:
            zero_counter += 1
        if result[i] is None or result[i] > zero_counter:
            result[i] = zero_counter
    return result


length = int(input())
number_list = list(map(int, input().strip().split()))

print_result(to_nearest_zero(length, number_list))
