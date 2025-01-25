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


input_data = input("\nВведите данные: ")
input_data = input_data.split(" ")
input_data = list(map(int, input_data))


@timemometr
def get_tariff_cost(input_data):
    internet_tariff_cost = input_data[0]
    internet_tariff_limit = input_data[1]
    over_limit_cost = input_data[2]
    over_limit_quantity = input_data[3]

    over_limit = over_limit_quantity - internet_tariff_limit

    if over_limit > 0:
        result_cost = internet_tariff_cost + over_limit * over_limit_cost
    else:
        result_cost = internet_tariff_cost

    return result_cost


print(get_tariff_cost(input_data))
