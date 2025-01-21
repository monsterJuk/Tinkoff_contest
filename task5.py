import psutil
import datetime

start_time = datetime.datetime.now().microsecond


finish_time = datetime.datetime.now().microsecond
result_time = finish_time - start_time
print("Время выполнения: " + str(result_time) + " mcs")

process = psutil.Process()
print(f"Употребленная память : {process.memory_info().rss / 1024 / 1024} Мб")
