#平方
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x**2)
print(squares)

#平方
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares) # prints [0, 1, 4, 9, 16]

#小於2的絕對值
nums = [-2, -1, 0, 1, 2]
ds = [abs(x) for x in nums if abs(x) < 2]
print(ds)      # prints [1, 0, 1]

#
from math import pi
print(pi)             # pi 3.141592653589793
print(round(pi, 3))  # 四捨五入到小數點後第三位 3.142
print([str(round(pi, i)) for i in range(1, 6)])
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']