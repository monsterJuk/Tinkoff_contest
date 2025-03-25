from random import randint


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


# n, m = list(map(int, input().split()))
# kilometers_per_day = list(map(int, input().split()))

n = 2 * 5000  # 3 <= n <= 2*10**5
# m = randint(1, n - 2)
m = n - 2
kilometers_per_day = [randint(1, n) for i in range(n + 1)]


@timemometr
def func(n, m, kilometers_per_day):
    n -= 2

    for index, day in enumerate(kilometers_per_day[2:]):
        if day < kilometers_per_day[0] or day > kilometers_per_day[1]:
            n -= 1
        elif day >= kilometers_per_day[0] and day <= kilometers_per_day[1]:
            try:
                kilometers_per_day.pop(index + 2)
            except IndexError:
                continue
    good_days_needed = m - n

    moves_down = 0
    moves_up = 0
    total_moves_down = 0
    total_moves_up = 0

    while good_days_needed > 0:
        kilometers_per_day[1] += 1
        moves_up += 1
        for index, day in enumerate(kilometers_per_day[2:]):
            if day >= kilometers_per_day[0] and day <= kilometers_per_day[1]:
                total_moves_up = moves_up
                good_days_needed -= 1
                try:
                    kilometers_per_day.pop(index + 2)
                except IndexError:
                    continue

        if good_days_needed > 0:
            kilometers_per_day[0] -= 1
            moves_down += 1
            for index, day in enumerate(kilometers_per_day[2:]):
                if day >= kilometers_per_day[0] and day <= kilometers_per_day[1]:
                    good_days_needed -= 1
                    total_moves_down = moves_down
                    try:
                        kilometers_per_day.pop(index + 2)
                    except IndexError:
                        continue
            if good_days_needed <= 0:
                break
        else:
            break

    return total_moves_down + total_moves_up


print(func(n, m, kilometers_per_day))
