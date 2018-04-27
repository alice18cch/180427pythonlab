#str = "Stone Campus", 請印出以下內容:

#這個字串的長度
#位置 6 的字母 (使用 [])
#從位置 3 到 9 的子字串 "ne Camp" (使用util.slice())
#從位置 3 到 最後的子字串 "ne Campus" (使用util.slice())
#從位置 0 到 9 的子字串 "Stone Camp"  (使用util.slice())

s = "Stone Campus"

print(len(s))

print(s[6])

print(s[3:10])

print(s[3:])

print(s[:10])