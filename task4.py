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


first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")

input_list = second_string.split()
number_of_attempts = int(first_string.split()[1])


@timemometr
def get_max_diff(input_list, number_of_attempts):
    result_list = []

    for number in input_list:
        divisor = 1
        number_list = []
        for number in str(number):
            number_list.append(number)

        result = 0
        while len(number_list) > 0:
            if int(number_list[-1]) < 9:
                result = (9 - int(number_list[-1])) * divisor
            del number_list[-1]
            divisor *= 10

        result_list.append(result)

    result_list.sort(reverse=True)

    result = 0
    for _ in range(0, len(result_list)):
        if _ <= number_of_attempts - 1:
            result += result_list[_]

    return result


print(get_max_diff(input_list, number_of_attempts))
