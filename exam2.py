def timemometr(func):
    from time import time
    import psutil

    def wrapper(*args):
        start_time = time()
        value = func(*args)
        end_time = time()
        print(f"Время выполнения: {end_time - start_time} сек")
        process = psutil.Process()
        print(
            f"Употребленная память : +\
    {process.memory_info().rss / 1024 / 1024} Мб"
        )
        return value

    return wrapper


n = int(input())
max_i = len(bin(10**18)) - 3

@timemometr
def get_cost(a: int) -> int:
    
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


numbers = [get_cost(int(input())) for _ in range(n)]

for i in numbers:
    print(i)
