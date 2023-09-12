from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
    long_str = list(longer)
    for i in range(0, len(shorter)):
        long_str.pop(long_str.index(shorter[i]))
  
    return long_str[0]

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
