import psutil
import datetime

# first_string = "5, 5"
# second_string = "1, 4, 9, 16, 25"
# third_string = "2"

first_string = "6, 4"
second_string = "1, 2, 3, 6, 8, 25"
third_string = "5"

first_list = first_string.split(",")
second_list = second_string.split(",")
third_list = third_string.split(",")

first_list = list(map(int, first_list))
second_list = list(map(int, second_list))
third_list = list(map(int, third_list))


def get_min_time():
    if (
        second_list[third_list[0] - 1] - second_list[0] <= first_list[1]
        or second_list[-1] - second_list[third_list[0] - 1] <= first_list[1]
    ):
        min_time = second_list[-1] - second_list[0]
    elif (
        second_list[third_list[0] - 1] - second_list[0]
        < second_list[-1] - second_list[third_list[0] - 1]
    ):
        min_time = (second_list[third_list[0] - 1] - second_list[0]) * 2 + (
            second_list[-1] - second_list[third_list[0] - 1]
        )
    elif (
        second_list[third_list[0] - 1] - second_list[0]
        > second_list[-1] - second_list[third_list[0] - 1]
    ):
        min_time = (second_list[third_list[0] - 1] - second_list[0]) + (
            second_list[-1] - second_list[third_list[0] - 1] * 2
        )

    return min_time


start_time = datetime.datetime.now().microsecond

min_time = get_min_time()
print(min_time)

finish_time = datetime.datetime.now().microsecond
total_time = finish_time - start_time
print("Время выполнения: " + str(total_time) + " mcs")

process = psutil.Process()
print(f"Употребленная память: {process.memory_info().rss / 1024 / 1024} Мб")
