def timemometr(func):
    from time import time
    import psutil

    def wrapper(*args):
        start_time = time()
        value = func(*args)
        end_time = time()
        print(f'Время выполнения: {end_time - start_time} сек')
        process = psutil.Process()
        print(f"Употребленная память : \
              {process.memory_info().rss / 1024 / 1024} Мб")
        return value
    return wrapper


count, t = [int(i) for i in input().split()]
levels = [int(i) for i in input().split()]
index_employee = int(input()) - 1


@timemometr
def get_min_time(t, levels, index_employee):
    if (
        levels[index_employee] - levels[0] <= t
        or levels[-1] - levels[index_employee] <= t
    ):
        min_time = levels[-1] - levels[0]
    else:
        min_time = levels[-1] - levels[0] + min(levels[-1] - levels[index_employee], levels[index_employee] - levels[0])

    return min_time


print(get_min_time(t, levels, index_employee))
