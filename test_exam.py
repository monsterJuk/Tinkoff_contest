def timemometr(func):
    from time import time
    import psutil

    def wrapper(*args):
        start_time = time()
        value = func(*args)
        end_time = time()
        print(f'Время выполнения: {end_time - start_time} сек')
        process = psutil.Process()
        print(f"Употребленная память : +\
              {process.memory_info().rss / 1024 / 1024} Мб")
        return value
    return wrapper


number1 = int(input())
number2 = int(input())


@timemometr
def get_sum(number1, number2):
    return number1 + number2


print(get_sum(number1, number2))
