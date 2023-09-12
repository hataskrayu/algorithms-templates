def to_binary(number: int) -> str:
    binary = str()
    modulo = 0
    if number == 0:
        return '0'
    while number > 0:
        modulo = number % 2
        binary += str(modulo)
        number = int(number / 2)
    return binary[::-1]

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))
