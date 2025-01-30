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


n, x, y, z = list(map(int, input().split()))
numbers = list(map(int, input().split()))


@timemometr
def func(n, x, y, z, numbers):
    delimeters_list = []
    result = []

    for num in numbers:
        if not num % x:
            delimeters_list.append(0)
        else:
            delimeters_list.append(min(num % x, x - (num % x)))

        if not num % y:
            delimeters_list.append(0)
        else:
            delimeters_list.append(min(num % y, y - (num % y)))

        if not num % z:
            delimeters_list.append(0)
        else:
            delimeters_list.append(min(num % z, z - (num % z)))

        result.append(delimeters_list.copy())
        delimeters_list.clear()

        # for res in result:
        #     if res[1] == res[0] or res[1] == res[2]:
        #         res[1] = 0
        #     if res[2] == res[0]:
        #         res[2] = 0
    for i in range(len(result)):
        res_copy = result[i].copy()
        if result[i][0] == result[i][1]:
            result[i][0] = 0
            res_copy[1] = 0
        if result[i][0] == result[i][2]:
            result[i][0] = 0
            res_copy[2] = 0
        if result[i][1] == result[i][2]:
            result[i][1] = 0
            res_copy[2] = 0
        result.append(res_copy)

    no_zero = []
    one_zero = []
    two_zero = []
    three_zero = []
    for res in result:
        if 0 not in res:
            no_zero.append(res)
        elif 0 in res and res.count(0) == 1:
            one_zero.append(res)
        elif 0 in res and res.count(0) == 2:
            two_zero.append(res)
        elif 0 in res and res.count(0) == 3:
            three_zero.append(res)

    total_count = []
    if three_zero:
        total_count.append(0)
    if no_zero:
        total_count.append(min(list(map(sum, no_zero))))
    if two_zero:
        total_count.append(min(list(map(sum, two_zero))))
    if one_zero:
        for res in one_zero:
            index_max = res.index(max(res))
            min_count = 10**18
            for ress in one_zero:
                if ress[index_max] < min_count and ress[index_max] != 0:
                    min_count = ress[index_max]
            res[index_max] = min_count

        total_count.append(min(list(map(sum, one_zero))))

    return min(total_count)


print(func(n, x, y, z, numbers))
