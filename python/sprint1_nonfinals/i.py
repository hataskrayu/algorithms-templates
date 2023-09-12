def is_power_of_four(number: int) -> bool:
    while number > 1:
        if number % 4:
            return False
        number = int(number / 4)
    return True

print(is_power_of_four(int(input())))
