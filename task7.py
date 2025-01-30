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


number_of_students = int(input())
list_of_students = list(map(int, input().split()))


@timemometr
def func(number_of_students, list_of_students):
    uniq_students = set(range(1, number_of_students + 1))
    repeating_students = []
    result = []

    for index in range(0, len(list_of_students)):
        if list_of_students[index] == index + 1:
            repeating_students.append(index + 1)
        if list_of_students[index] in uniq_students:
            uniq_students.remove(list_of_students[index])

    if len(repeating_students) == 1 and len(uniq_students) == 1:
        result.append(repeating_students[0])
        result.append(list(uniq_students)[0])
        list_of_students[result[0] - 1] = result[1]
        for index in range(0, len(list_of_students)):
            if (
                index < len(list_of_students) - 1
                and list_of_students[index] == index + 2
            ):
                continue
            elif index == len(list_of_students) - 1 and list_of_students[index]:
                return " ".join(map(str, result))
            else:
                return " ".join(map(str, [-1, -1]))
    else:
        return " ".join(map(str, [-1, -1]))


print(func(number_of_students, list_of_students))
