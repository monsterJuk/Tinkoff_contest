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


first_list = [int(i) for i in input().split()]
second_list = [i for i in input().split()]


@timemometr
def get_max_diff(first_list, second_list):
    result_list = []
    attempts = first_list[1]

    for number in second_list:
        delimeter = 1
        while number:
            digit = int(number[-1:])
            diff = (9 - digit) * delimeter
            result_list.append(diff)
            delimeter *= 10
            number = number[:-1]

    result_list = sorted(result_list, reverse=True)

    return sum(result_list[:attempts])


print(get_max_diff(first_list, second_list))
