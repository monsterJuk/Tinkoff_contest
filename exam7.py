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


n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))


@timemometr
def func(n, k, numbers):
    for p in range(1, k + 1):
        numbers = sorted(numbers)
        result = []
        for i, num1 in enumerate(numbers):
            for num2 in numbers[i + 1 :]:
                if num1 < num2:
                    result.append((num1, num2))

        result = list(map(sum, result))
        result = list(map(lambda x: x**p, result))
        result = sum(result)
        result = result % 998244353

        print(result)


func(n, k, numbers)
