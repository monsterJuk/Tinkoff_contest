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
            f"Употребленная память : +\
{process.memory_info().rss / 1024 / 1024} Мб"
        )
        return value

    return wrapper


number_of_students = int(input())
height_of_students = list(map(int, input().split()))


@timemometr
def physical_training(height_of_students):
    students_for_change = []

    for index in range(0, len(height_of_students)):
        if (index + 1) % 2 != height_of_students[index] % 2:
            students_for_change.append(index + 1)

    if len(students_for_change) == 2 and sum(students_for_change) % 2:
        return students_for_change
    elif len(students_for_change) == 0 and len(height_of_students) >= 3:
        return [1, 3]
    else:
        return [-1, -1]


print("{0} {1}".format(*physical_training(height_of_students)))
