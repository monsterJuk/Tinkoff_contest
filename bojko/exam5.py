# n, s = [int(i) for i in input().split()]
# a = [int(i) for i in input().split()]
n, s = 10, 10
# n, s = 3, 3
a = [int(i) for i in "2 1 9 1 9 1 9 1 8 1".split()]
"""
2 1 9 1 9 1 9 1 8 1

2191919181 = 30

2
21
21 9
21 91
21 91 9
21 91 91
21 91 91 9
21 91 91 91
21 91 91 91 8
21 91 91 91 81

191919181 = 24
1
19
19 1
19 19
19 19 1
19 19 19
19 19 19 1
19 19 19 18
19 19 19 181

91919181 = 20

9
91
91 9
91 91
91 91 9
91 91 91
91 91 91 8
91 91 91 81

1919181 = 15

1
19
19 1
19 19
19 19 1
19 19 18
19 19 181

919181 = 12

9
91
91 9
91 91
91 91 8
91 91 81

19181 = 8

1
19
19 1
19 18
19 181

9181 = 6

9
91
91 8
91 81

181 = 3

1
18
181

81 = 2

8
81

1 = 1


"""
# a = [int(i) for i in "1 2 3".split()]

def exam5_dicted(n: int, s: int, a: list[int]):
    d = dict()
    total = 0
    for m in range(n):
        for r in range(m, n):
            if (m, r) in d:
                total += d[m, r]
            else:
                local_total = 0
                b = [b for b in a[m:r + 1]]
                tail = 0
                while b:
                    bpop = b.pop()
                    if tail + bpop > s:
                        local_total += 1
                        tail = bpop
                    else:
                        tail += bpop
                if tail:
                    local_total += 1
                d[m, r] = local_total
                total += local_total
    return total
print("\n")
print(exam5(n, s, a))
"""
s = 10
10 10

27 171 9 1 9 1 8 1
271 71 1

21 91 91 91 81

2 19 19 19 181

123 45 4321
1234 5

10

251 27 27 19

25 127 27 19 


34 361 1 54 
343 61  154
"""