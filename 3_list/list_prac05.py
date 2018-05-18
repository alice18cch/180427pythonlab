#請實作以下函數:

#squareList(nums): 回傳一個 list, 其中的元素為 nums 中每個數字的平方, 例如: squareList([3, 4, 5]) 回傳 [9, 16, 25]
#absList(nums, x): 回傳一個 list, 其中的元素為 nums 中絕對值小於 x 的數字, 例如: absList([3, 4, -1, -2, 2, 7, 1], 3) 回傳 [-1, -2, 2, 1]
#piList(n): 回傳一個 list, 其中的元素為從小數第 1 位到第 n 位的 pi 值, 例如 : piList(5) 回傳 [3.1, 3.14, 3.142, 3.1416, 3.14159]
#可以使用 math.pi 得到 pi 值, 像是:

#from math import pi
#pi  # 3.141592653589793
from math import pi
def squareList(nums):
    squares = [x ** 2 for x in nums]
    print(squares)
def absList(nums, x):
    abslist = [abs(y) for y in nums if abs(y)<x]
    print(abslist)
def piList(n):
    pilist = [round(pi, i) for i in range(1, n+1)]
    print(pilist)


def test():
    squareList([0,1,2,3,4])
    absList([-3,-1,1,3], 2)
    piList(5)

test()

#def squareList(nums):
#    return [x**2 for x in nums]
#print("01", squareList([3,4,5]))