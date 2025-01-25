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


input_data = input("\nВведите данные: ")
input_data = input_data.split(" ")
input_data = list(map(int, input_data))


@timemometr
def get_number_of_tests(input_data):
    divisor = 1
    while input_data[1] // divisor > 1:
        divisor *= 10

    divisor = int('1' * len(str(divisor)))

    result = 0
    while len(str(divisor)) > 1:

        for number in range(input_data[1], input_data[0] - 1, -1):
            if number % divisor == 0:
                result += 1

        divisor = int(str(divisor)[:-1])

    digit = input_data[0]
    while len(str(digit)) == 1 and digit <= input_data[1]:
        result += 1
        digit += 1

    return result


print(get_number_of_tests(input_data))
