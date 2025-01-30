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


i = "10 5"
# i = input()
x, y = [float(c) for c in i.split()]

i = "3.0  2.5  1.0  2.5  1.0  1.5  3.0  1.5"
# i = input()
c = [float(c) for c in i.split()]


@timemometr
def test8(x: float, y: float, c: list[float]):
    room_center = (x / 2, y / 2)
    plan_center = ((c[0] + c[4]) / 2, (c[1] + c[5]) / 2)

    x_slide = abs((room_center[0] - plan_center[0]) / x)
    y_slide = abs((room_center[1] - plan_center[1]) / y)
    x_slide_plan = abs(c[0] - c[4]) * x_slide
    y_slide_plan = abs(c[1] - c[5]) * y_slide

    if room_center[0] < plan_center[0]:
        x_result = plan_center[0] - x_slide_plan
    else:
        x_result = plan_center[0] + x_slide_plan
    if room_center[1] < plan_center[1]:
        y_result = plan_center[1] - y_slide_plan
    else:
        y_result = plan_center[1] + y_slide_plan

    return [f"{x_result:.4f}", f"{y_result:.4f}"]


print(test8(x, y, c))
