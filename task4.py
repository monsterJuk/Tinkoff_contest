import psutil
import datetime

input_list = [9999]
number_of_attempts = 10
result_list = []

start_time = datetime.datetime.now().microsecond

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

print(result)

finish_time = datetime.datetime.now().microsecond
result_time = finish_time - start_time
print("Время выполнения: " + str(result_time) + " мкс")

process = psutil.Process()
print(f"Употребленная память : {process.memory_info().rss / 1024 / 1024} Мб")
