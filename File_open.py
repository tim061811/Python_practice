# 檔案讀取、寫入

# open("檔案路徑",mode"開啟模式")

# 絕對路徑 ex: C:/Users/LAI/Documents/Python/123.txt
# 相對路徑 以程式的位置做延伸 ex: 123.txt

# mode="r" 讀取
# mode="w" 覆寫
# mode="r+" 讀寫
# mode="a" 在原先的資料後寫東西


file = open("123.txt",mode="r")
print(file.read()) #印出全部文字

print(file.readline()) #印出檔案第一行
print(file.readline()) #印出檔案第二行

print(file.readlines()) #把每一行資料放到列表裡

for line in file: #印出每一行可用for迴圈
    print(line)


file = open("123.txt",mode="w")
file.write("hello") #複寫檔案內容


file = open("123.txt",mode="a")
file.write(" Mr.Lai")

file = open("123.txt",mode="a",encoding="utf-8")
     # open("檔案路徑",mode"開啟模式",encoding="編碼的方式")
     # 因編碼不支援中文，加入第三個參數 編碼的方式參數
file.write("\n你好") # \n換行

file.close() #關掉檔案

with open("123.txt",mode="a",encoding="utf-8") as file: #加上 with as 可自動關閉檔案
    data = file.write("\n你好")
print(data)

# 把檔案中的數字資料，一行一行的讀取出來，並計算總合
sum = 0
with open("num.txt",mode="r",encoding="utf-8") as file:
    for line in file: #一行一行讀取
        sum = sum + int(line) #轉換成數字
print(sum)

# 使用 JSON 格式讀取、複寫檔案
# 讀取到的資料=json.load(檔案物件)
import json
# 從檔案中讀取 JSON 資料，放入變數 data 裡面
with open("config.json",mode="r") as file:
    data = json.load(file) # data 是一個字典
print("name",data["name"])
print("version",data["version"])

data["name"] = ["New Nmae"] # 修改變數中的資料
# 把最近的資料複寫回檔案中
with open("config.json",mode="w") as file:
    json.dump(data,file)
