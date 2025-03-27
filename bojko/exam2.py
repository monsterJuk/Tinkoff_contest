n = int(input())

max_i = len(bin(10**18)) - 3

def exam(a: int) -> int:
    
    counter = 0
    c = 0
    i = max_i
    while i >= 0:
        b = 1 << i
        i -= 1
        if a & b:
            c |= b
            counter += 1
            if counter == 3:
                return c
    return -1


numbers = [exam(int(input())) for _ in range(n)]

for i in numbers:
    print(i)
