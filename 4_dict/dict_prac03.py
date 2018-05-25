'''請由輸入讀取班上每個同學的出生月份, 然後將每個月份的人數印出.
輸入的每一行代表一個學生的座號和生日月份.
output
1 3
2 4
3 1
4 2
5 1
6 None
7 None
8 1
9 2
10 2
11 2
12 2
'''
import sys

birth = {}

def test():
    for line in sys.stdin:
        line = line.strip()
        tokens = line.split()
        print(tokens)
        m = int(tokens[1])
        if birth.get(m):
            birth[m] += 1
        else:
            birth[m] = 1
    for i in range(1, 13):
        print(i, birth.get(i))

test()