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
number_of_students = int(number_of_students)

gifted_students = input("\nВведите рост учеников: ")
gifted_students = gifted_students.split(" ")
gifted_students = list(map(int, gifted_students))


count = 1


@timemometr
def get_student_number(number_of_students, gifted_students):
    for index in range(0, len(gifted_students)):
        if index + 1 == gifted_students[index]:
            count += 1
            result = index + 1


print(get_student_number(number_of_students, gifted_students))
