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


# n = int(input())
day_total_cost = [10**18 - i for i in range(10)]

# day_total_cost = [int(input()) for i in range(n)]


@timemometr
def get_cost(day_total_cost):
    for cost in day_total_cost:
        flowers = []
        i = 0
        while cost > 0:
            if cost & 1:
                flowers.append(i)
            i += 1
            cost = cost >> 1

        if len(flowers) > 2:
            print(sum([2**i for i in flowers[-3:]]))
        else:
            print(-1)


get_cost(day_total_cost)
