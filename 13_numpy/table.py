'''請實作函數 table(m, n) 產生一個 array 物件並回傳, 內容為 mxn 的乘法表,

請測試你的 table() 函數, 印出回傳 array 物件的: 內容, 維度 (ndim), 每個維度的元素個數 (shape)

例如: table(4, 5) 回傳一個乘法表, 請印出:
[[ 1  2  3  4  5]
 [ 2  4  6  8 10]
 [ 3  6  9 12 15]
 [ 4  8 12 16 20]]
2
(4, 5)'''
import numpy as np

def table(m, n):
    arr = []
    for i in range(0, m):
        arr.append([1, 2, 3])
    return np.array(arr)

def test():
    #arr = table(4,5)
    arr = [
        [[1, 2, 3], [4, 5, 6]],
        [[10, 20, 30], [40, 50, 60]],
        [[2, 3, 4], [7, 8, 9]]
    ]
    print(arr)
    nparr = np.array(arr)
    #print(arr.ndim)
    #print(arr.shape)
    print(nparr.ndim)
    print(nparr.shape)
    print(nparr * 2)

def table2(m, n):
    arr = []
    for i in range (1, m+1):
        sub = []
        for j in range(1, n+1):
            sub.append(i*j)
        arr.append(sub)
    return np.array(arr)

def table3(m, n):
    arr = [[i*j for j in range(i, n+1)] for i in range(i, m+1)]
    return np.array(arr)

def test2():
    nparr = table2(3, 7)
    print(nparr)
    print(nparr.ndim)
    print(nparr.shape)

test2()