import psutil
import datetime

N = 5


def get_number_of_cuts(number_of_people):
    number_of_cuts = 0
    _ = 0
    while number_of_people // 2 > 0:
        if number_of_people % 2 > 0 and _ == 0:
            number_of_cuts += 1
            _ += 1
        number_of_cuts += 1
        number_of_people = number_of_people // 2
    return number_of_cuts


start_time = datetime.datetime.now().microsecond

number_of_cuts = get_number_of_cuts(N)
print(number_of_cuts)

finish_time = datetime.datetime.now().microsecond
total_time = finish_time - start_time

print("Время выполнения: " + str(total_time) + " mcs")

process = psutil.Process()
print(f"Употребленная память : {process.memory_info().rss / 1024 / 1024} Мб")
