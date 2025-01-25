def timemometr(func):
    from time import time
    import psutil

    def wrapper(*args):
        start_time = time()
        value = func(*args)
        end_time = time()
        print(f'Время выполнения: {end_time - start_time} сек')
        process = psutil.Process()
        print(f"Употребленная память : +\
              {process.memory_info().rss / 1024 / 1024} Мб")
        return value
    return wrapper


number_of_students = input("\nВведите количество учеников: ")
number_of_students = number_of_students.split(" ")
number_of_students = list(map(int, number_of_students))

height_of_students = input("\nВведите рост учеников: ")
height_of_students = height_of_students.split(" ")
height_of_students = list(map(int, height_of_students))


@timemometr
def physical_training(number_of_students, height_of_students):
    students_for_change = []
    for index in range(0, len(height_of_students)):
        if index + 1 % 2 == height_of_students[index] % 2:
            continue
        else:
            students_for_change.append(str(index + 1))

    if len(students_for_change) != 2:
        students_for_change = ['-1', '-1']

    return students_for_change


print(' '.join(physical_training(number_of_students, height_of_students)))
