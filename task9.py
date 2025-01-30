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
            f"Употребленная память : \
{process.memory_info().rss / 1024 / 1024} Мб"
        )
        return value

    return wrapper


n = int(input())
dinner_costs = []

for _ in range(n):
    dinner_costs.append(int(input()))


@timemometr
def func(dinner_costs):
    total_cost = sum(dinner_costs)
    saving = []
    for index, cost in enumerate(dinner_costs):
        if cost > 100 and cost - 100 < max(dinner_costs[index:]):
            saving.append(max(dinner_costs[index + 1 :]))
            dinner_costs.remove(max(dinner_costs[index:]))

    return total_cost - sum(saving)


print(func(dinner_costs))
