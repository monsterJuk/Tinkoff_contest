from collections import defaultdict
# n, m = [int(i) for i in input().split()]
# a = [int(i) for i in input().split()]

m = 4
a = [int(i) for i in "2 4 8 6 1 5 5 1".split()]
a = [int(i) for i in "4 2 3 8 6 1 5 5 1".split()]
# a = [3, 4, 6, 5, 1, 2, 4, 4]
# a = [3, 4, 4, 4, 1, 1]

def exam3(m: int, a: list) -> int:
    low = a[0]
    high = a[1]

    d = defaultdict(int)

    for i in sorted(a[2:]):
        to_low = i - low
        to_high = high - i
        
        if to_low >= 0 and to_high >= 0:
            m -= 1
        else:
            key = (abs(min(0, to_low)), abs(min(0, to_high)))
            d[key] += 1
        
        if m <= 0:
            return 0

    steps = set([k[0] + k[1] for k in d.keys()])
    # add max step 40 11 04 = 8
    
    
    for s in steps:
        
        for i in range(s + 1):
            to_low = i
            to_high = s - i
            
            if m - sum([d[key] for k in d.keys() if k[0] >= to_low and k[1] <= to_high]) <= 0:
                return s
            
print(exam3(m, a))