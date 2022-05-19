# 判斷資料是否存在 in 或 not in
S1 = {1,2,3}
print(3 in S1)

# 集合

# & 交集，取兩個集合中，相同的資料
S2 = {2,3,4}
S3 = S1 & S2
print(S3)

# | 聯集，取兩個集合中的所有資料，但不重複
S3 = S1 | S2
print(S3)

# - 差集，從S1中，減去和S2重疊的部分
S3 = S1 - S2
print(S3)

# ^ 反交集，取兩個集合中，不重疊的部分
S3 = S1 ^ S2
print(S3)

# set(字串) 將字串中的字母拆解成集合
S = set("Hello")
print(S)
print("H" in S) 

# 字典
# key   value
# 鍵    值

dic = {"蘋果":"apple","香蕉":"banana","貓":"cat","狗":"dog"}
print(dic["狗"])

dic = {"0":"apple","1":"banana","2":"cat","3":"dog"}
print(dic["3"])

print("0" in dic) #判斷key是否存在
del dic["0"] #刪除字典中的鍵值對(key-value)
print(dic)

# 新增資料至字典中
# 字典變數名字[新增的鍵（key）]=新增的值（value）
dic ["豬"] = "pig"
print(dic)

# 刪除字典的key
# 字典變數名字.pop(欲刪除鍵（key）的名字)
rename = dic.pop("豬")
print(dic)
print(rename)


# 延伸學習
# dic = {變數:變數 for 變數 in 列表}
dic = {x:x*2 for x in [2,3,4]}
# 從列表中產生字典
print(dic)