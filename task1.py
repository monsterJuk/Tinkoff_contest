import psutil
import datetime

start_time = datetime.datetime.now().microsecond

input_data = [100, 10, 12, 15]

internet_tariff_cost = input_data[0]
internet_tariff_limit = input_data[1]
over_limit_cost = input_data[2]
over_limit_quantity = input_data[3]

over_limit = over_limit_quantity - internet_tariff_limit

if over_limit > 0:
    result_cost = internet_tariff_cost + over_limit * over_limit_cost
else:
    result_cost = internet_tariff_cost

print(result_cost)

finish_time = datetime.datetime.now().microsecond
result_time = finish_time - start_time
print("Время выполнения: " + str(result_time) + " mcs")

process = psutil.Process()
print(f"Употребленная память : {process.memory_info().rss / 1024 / 1024} Мб")
