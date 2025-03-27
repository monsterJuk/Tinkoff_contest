from collections import defaultdict
from collections import namedtuple
Point = namedtuple('point', ('x', 'y'))

n = int(input())
a = list()
for _ in range(n):
    a.append(Point(*[int(i) for i in input().split()]))
    
def exam6(n: int, a:list[Point]) -> int:
    d = defaultdict(set)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i].y == a[j].y:
                key = (None, a[i].y)
                d[key].add(i)
                d[key].add(j)
            elif a[i].x == a[j].x:
                key = (a[i].x, None)
                d[key].add(i)
                d[key].add(j)
            else:
                y = a[j].y - a[i].y
                x = a[j].x - a[i].x
                k = y / x
                b = a[i].y - k * a[i].x
                key = (k, b)
                d[key].add(i)
                d[key].add(j)
                
    max_len = 0
    for key in d.keys():
        if max_len < len(d[key]):
            max_len = len(d[key])
            
    
                    
    free = n - max_len
    pairs = max_len // 2
    t = min(pairs, free)
    if free <= pairs:
        return free
    else:
        return (n - t * 3 ) // 3 + t

print(exam6(n, a))