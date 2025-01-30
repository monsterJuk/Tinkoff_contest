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


input_data = list(map(int, input().split()))


@timemometr
def get_tests_number(input_data):
    result_list = []
    for digit in range(1, 10):
        result = digit
        while result <= 10**18:
            result_list.append(result)
            result = result * 10 + digit

    number_of_tests = 0
    for number in result_list:
        if number in range(input_data[0], input_data[1] + 1):
            number_of_tests += 1
    return number_of_tests


print(get_tests_number(input_data))
