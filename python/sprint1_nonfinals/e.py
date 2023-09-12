def get_longest_word(line: str) -> str:
    current_word = (0, 0)
    j=0
    i=0
    length = len(line)
    current_length = 0
    for i in range(0, length):
        if line[j] == ' ':
            j += 1
        if line[i] == ' ':
            temp_length = i - j
            if current_length < temp_length:
                current_length = temp_length
                current_word = (j, i)
            j = i
    if current_length < i - j + 1:
        current_word = (j, i + 1)
    return line[current_word[0]:current_word[1]]

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))
