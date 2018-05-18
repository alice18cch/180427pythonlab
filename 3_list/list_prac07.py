#Python - 簡單 Bulls and Cows
#現在想進行 4 位數字的 Bulls and Cows 遊戲, 
#請你寫一個函數 result(answer, guess) 回傳 guess 和 answer 的比較結果.

#例如: result('1234', '4321') 回傳 '0A4B',
#result('4657', '9658') 回傳 '2A0B', result('9876', '6879') 回傳 '2A2B'

def result(answer, guess):
    A=0
    B=0
    for idx_ans, val_ans in enumerate(answer):
        for idx_gue, val_gue in enumerate(guess):
            #print(idx_ans, val_ans, idx_gue, val_gue)
            if val_ans==val_gue:#若值香等
                if idx_ans==idx_gue:#若位置相等
                    A+=1
                else:#若位置不等
                    B+=1
    return str(A)+"A"+str(B)+"B"

print(result('1234','4321'))
print(result('4657','9658'))
print(result('9876','6879'))

def result2(answer, guess):
    A=0
    B=0
    for idx_ans, val_ans in enumerate(answer):
        if answer[idx_ans]==guess[idx_ans]:#若值香等
                A+=1
        else:#若位置不等
            for idx_gue, val_gue in enumerate(guess):
                if val_ans == val_gue and idx_ans != idx_gue:
                    B+=1
    return str(A)+"A"+str(B)+"B"

print(result2('1234','4321'))
print(result2('4657','9658'))
print(result2('9876','6879'))