def is_palindrome(line: str) -> bool:
    line = [i.lower() for i in line if i.isalpha() or i.isdigit()]
    b = 0
    e = len(line)-1
    if e == 0:
        return True
    while b < e:
        if line[b] != line[e]:
            return False
        e -= 1
        b += 1
    return True
    

print(is_palindrome(input().strip()))
