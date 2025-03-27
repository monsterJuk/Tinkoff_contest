from pprint import pprint
from collections import defaultdict
from collections import namedtuple
def exam4():
    pass

"""
6 10 20 30
8 17 5 28 39 13
3


6 99 100 101
"""
# n, x, y, z = [int(i) for i in input().split()]
# a = [int(i) for i in input().split()]


n, b = [i for i in "6 10 20 30".split(maxsplit=1)]
n = int(n)
b = [int(i) for i in b.split()]
b = list(set(b))
a = [int(i) for i in "8 17 5 28 39 13".split()]

def get_indexes(i: int) -> list[int]:
    index = 0
    indexes = list()
    while i > 0:
        if i & 1:
            indexes.append(index)
        index += 1
        i = i >> 1
    return indexes

indexes = list()
for i in range(1, 2 ** len(b)):
    indexes.append(tuple(get_indexes(i)))
indexes = dict(zip(indexes, [[]] * len(indexes)))

print(indexes)

d = dict()

Stat = namedtuple('Stat', ['diff', 'index'])

for number_index, number in enumerate(a):
    mods = [- number % i for i in b]
    print(mods)
    
    for i in indexes.keys():
        # print(i, i == tuple([index for index in i if mods[index] == mods[i[0]]]))
        if i == tuple([index for index in i if mods[index] == mods[i[0]]]):
            # print('done' + str(mods[i[0]]))
            if i not in d:
                d[i] = [Stat(mods[i[0]], number_index)]
            else:
                if len(d[i]) < len(b) or d[i][-1].diff > mods[i[0]]:
                    d[i].append(Stat(mods[i[0]], number_index))
                d[i] = sorted(d[i], key=lambda x: x.diff)[:len(b)]
            
            # indexes[i].append(
            #     Stat(mods[i[0]], number_index)
            # )
        # if len(i) == len([index for index in i if mods[index] == mods[i[0]]]):
        #     indexes[i].append(
        #         Stat(mods[i[0]], number_index)
        #     )
    
pprint(d)

diffs = list()
for i, val in enumerate(indexes):
    print(i, val)
    
if indexes[6] in d:
    diffs.append(d[indexes[6][0]].diff)

if indexes[5] in d and indexes[0] in d:
    if indexes[5][0] 



        
"""

big_list = list()
base = b
a = list()
tail = b
while base != 0:
    if tail >= base:
        a.append(base)
        tail -= base
    
    a.append(tail)
    
    if tail == 0 or len(a) == n:
        big_list.append(a)
        base -= 1
        tail = b
        break
"""
# 7

# 6 1

# 5 2
# 5 1 1


# 4 3
# 4 2 1
# 4 1 1 1



# 3 3 1
# 3 2 2
# 3 2 1 1

# 2 2 2 1

"""
3 7

7

6 1

5 2
5 1 1

4 3
4 2 1

3 3 1
3 2 2

"""



"""
# n = 4
# b = 9

9

8 1

7 2
7 1 1

6 3

6 2 1

5 4

5 3 1

5 2 2

4 4 1

4 3 2

4 3 1 1

4 2 2 1

3 3 3

3 3 2 1

3 2 2 2

"""


# n = 3
# b = 3
# 1 1 1
# 1 2
# 3


# for i in range(2 ** 5):
    # print(bin(i))
    

# for i in range(max((1, len(b) - n)), 2 ** len(b)):
    
    # print(bin(i))
    
    # indexes_for_i = list()

# for i in a:
#    mods = -i % x, -i % y, -i % z
        
#    print(mods)
    # return 0
    


def get_multiples(a: int) -> list[int]:
    m = list()
    i = 2
    while i <= a:
        if a % i == 0:
            m.append(i)
            a /= i
            i = 2
        else:
            i += 1
    return m
    
    
# 4 6 = 24
# 22 23
# 2 23 = 12
# 4 10
# 22 25
# 2 25 = 20
# 99 44 121
# 11 9411



# for i in range(99 * 100 * 101 + 1):
#     # if not (i % 99 and i % 100 and i % 101):
#     # if i % 99 == 0 and i % 100 == 0 and i % 101 == 0:
#     if i % 99 == 0 and i % 100 == 0:
#        print(i)
    
