from collections import defaultdict


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


n = int(input())
a = []
for _ in range(n):
    a.append(([int(i) for i in input().split()]))
print(a)


@timemometr
def get_max_triangles(n, a):
    d_y = defaultdict(set)
    d_x = defaultdict(set)
    d_kx = defaultdict(set)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i][1] == a[j][1]:
                key = (None, a[i][1])
                d_y[key].add(i)
                d_y[key].add(j)
            elif a[i][0] == a[j][0]:
                key = (a[i][0], None)
                d_x[key].add(i)
                d_x[key].add(j)
            else:
                y = a[j][1] - a[i][1]
                x = a[j][0] - a[i][0]
                k = y / x
                b = a[i][1] - k * a[i][0]
                key = (k, b)
                d_kx[key].add(i)
                d_kx[key].add(j)

    max_len_d_y = max(list(map(len, d_y.values())))
    max_len_d_x = max(list(map(len, d_x.values())))
    max_len_d_kx = max(list(map(len, d_kx.values())))
    max_len = max(max_len_d_y, max_len_d_x, max_len_d_kx)

    free_points = n - max_len
    two_points = max_len // 2
    t = min(two_points, free_points)
    if free_points <= two_points:
        return free_points
    else:
        return (n - t * 3) // 3 + t


print(get_max_triangles(n, a))
