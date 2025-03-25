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
# n, s = [int(i) for i in input().split()]
# a = [int(i) for i in input().split()]
# n, s = 10, 10
# n, s = 3, 3
# a = [int(i) for i in "2 1 9 1 9 1 9 1 8 1".split()]
# a = [int(i) for i in "1 2 3".split()]
n = 500
s = random.randint(10**8, 10**15)
lengths = a = [random.randint(1, min(s, 10**9)) for _ in range(n)]


@timemometr
def exam5(n: int, s: int, a: list[int]):
    total = 0
    for m in range(n):
        for r in range(m, n):
            b = [b for b in a[m : r + 1]]
            tail = 0
            while b:
                bpop = b.pop()
                if tail + bpop > s:
                    total += 1
                    tail = bpop
                else:
                    tail += bpop
            if tail:
                total += 1
    return total


@timemometr
def exam5_dicted(n: int, s: int, a: list[int]):
    d = dict()
    total = 0
    for m in range(n):
        for r in range(m, n):
            if (m, r) in d:
                total += d[m, r]
            else:
                local_total = 0
                b = [b for b in a[m : r + 1]]
                tail = 0
                while b:
                    bpop = b.pop()
                    if tail + bpop > s:
                        local_total += 1
                        tail = bpop
                    else:
                        tail += bpop
                if tail:
                    local_total += 1
                d[m, r] = local_total
                total += local_total
    return total


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


print(exam5(n, s, a))
print(exam5_dicted(n, s, a))
print(func(n, s, lengths))
