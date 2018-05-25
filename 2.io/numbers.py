def readInput():
    line1 = input()
    line2 = input()
    line3 = input()
    num1 = int(line1)
    num2 = int(line2)
    num3 = int(line3)
    print(num1 + 1)
    print(num2 + 1)
    print(num3 + 1)
    

def readInput2():
    line = input()
    cnt = int(line)
    for i in range(0,cnt):
        line = input()
        num = int(line)
        print(num+1)

readInput2()