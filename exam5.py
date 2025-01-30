import random


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


# n, s = list(map(int, input().split()))
# lengths = list(map(int, input().split()))
n = 1000
s = random.randint(10**8, 10**15)
lengths = [random.randint(1, min(s, 10**9)) for _ in range(n)]


@timemometr
def func(n, s, lengths):
    values_list = []
    for num1 in range(n):
        for num2 in range(num1, n):
            values_list.append([lengths[i] for i in range(num1, num2 + 1)])

    segments = []
    segment = []
    seg = []
    val = 0
    for val in values_list:
        for i, item in enumerate(val):
            if sum(seg) + item <= s:
                seg.append(item)
            else:
                segment.append(seg.copy())
                seg.clear()
                seg.append(item)
            if i == len(val) - 1:
                segment.append(seg.copy())
                segments.append(segment.copy())
                seg.clear()
                segment.clear()

    summa = 0
    for i in segments:
        summa += len(i)

    return summa


print(func(n, s, lengths))
