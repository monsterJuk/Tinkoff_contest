# from random import randint


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

# n = 10**2
# k = 300

# numbers = [randint(1, 10**8) for _ in range(n)]


@timemometr
def func(k, numbers):
    for p in range(1, k + 1):
        # numbers = sorted(numbers)
        result = []
        for i, num1 in enumerate(numbers):
            for num2 in numbers[i + 1 :]:
                if num1 < num2:
                    result.append((num1 + num2) ** p)

        result = sum(result)
        result = result % 998244353

        print(result)


func(k, numbers)
