# 列表有順序、可動的列表 list

# []中括號中可加入數字、字串、布林值
scores = [90,70,30,40,50]
friends = ["小賴","小林","吟潔"]
things = [90,"小林",True]
print(scores[0])

# 元組 有順序、不可動的列表 touple 
scores = (90,80,70,50,60)
print(scores[0])

# len 知道元組或列表內有多少個值
print(len(scores))

# 集合 一群資料，無順序的列表 set
{3,4,5}

# []中括號中加入:冒號 取列表的順序
print(scores[0:4]) #取第一位到第三位(不包含第四位)
print(scores[0:]) #取第一位到最後
                  #python開始是從0開始計算

# 將第一位數字更改成30
scores[0] = 30
print(scores)
print(scores[0])

# .extend() 延伸列表
scores.extend(friends)
print(scores)

# .append() 列表後加上一個
scores.append(100)
print(scores)

# .insert(位置,) 插入
scores.insert(2,87)
print(scores)

# .remove() 移除
scores.remove(30)
print(scores)

# del 串列 [] 刪除指定位置資料
del scores[1]

# .pop() 移除最後一位 小括號無須填入
scores.pop()
print(scores)

# .sort() 由小到大排列 小括號無須填入
scores.sort()
print(scores)

# .reverse() 反轉列表 小括號無須填入
scores.reverse()
print(scores)

# .index(值) 找出值的位置 若有重複則會跳出第一位
print(scores.index(70))

# .count(值) 數列表有幾個
print(scores.count(70))

# .clear() 列表清空 小括號無須填入
scores.clear()
print(scores)

