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


s = input()


@timemometr
def three_letters(s):
    if s.index("R") < s.index("M"):
        return "Yes"
    else:
        return "No"


print(three_letters(s))
