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


number = input("\nВведите данные: ")
number = int(number)


@timemometr
def get_number_of_cuts(number):
    number_of_cuts = 0
    _ = 0
    while number // 2 > 0:
        if number % 2 > 0 and _ == 0:
            number_of_cuts += 1
            _ += 1
        number_of_cuts += 1
        number = number // 2
    return number_of_cuts


print(get_number_of_cuts(number))
