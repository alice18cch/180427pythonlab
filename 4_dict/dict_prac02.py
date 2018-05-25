#請讀取輸入並建立一個 dictionary, 用來儲存學校的名稱和對應的總人數.
#每行輸入為學校名稱, 一年級人數, 二年級人數, 三年級人數和四年級人數.
#請依查詢印出對應的學校和年級人數.
#例如: 查詢 NCTU-1, 請印出 NCTU 一年級的人數.
#output
#NCTU-4 4000
#NCTU-1 7000
#NTHU-2 7000
#NTHU-3 5000
#NTU-4 6000
#NTU-3 7500
students = {}

def prSTnum(schgra):
    if (students.get(schgra)):
        print(schgra, students.get(schgra))
    else:
        print("N/A")
def test():
    num = int(input())
    for i in range(0, num):
        line = input()
        tokens = line.strip().split()
        '''
        students[tokens[0]+"-1"] = int(tokens[1])
        students[tokens[0]+"-2"] = int(tokens[2])
        students[tokens[0]+"-3"] = int(tokens[3])
        students[tokens[0]+"-4"] = int(tokens[4])'''
        for j in range(1,5):
            num = int(tokens[j])
            students[tokens[0]+"-"+str(j)] = num
    print(students)
    num = int(input())
    for i in range(0, num):
        line = input()
        #print(line, students[line])
        prSTnum(line)
        #36/37皆為查詢
test()