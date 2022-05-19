# 封裝變數或函式，封裝的變數或函式統稱類別的屬性
# 要先定義(建立)類別，才能使用類別中封裝的屬性

# 建立類別語法
# class 類別名稱:
#   定義封裝的變數
#   定義封裝的函式

# 範例 1
# 定義 Test 類別
class Test: #首字大寫
    x = 3 #定義變數
    def say(): #定義函式
        print("Hello")


# 使用類別語法
# 類別名稱.屬性名稱

# 範例 2
class Test: 
    x = 3 
    def say(): 
        print("Hello")
# 使用 Test 類別
Test.x+3 #取得屬性 x 的資料 3
Test.say() #呼叫屬性 say 函式

# ----------------------------------------

# 定義一個類別 IO，有兩個屬性 supportedSrcs 和 read
class IO:
    supportedSrcs = ["console","file"]
    def read(src):
        print("read from",src)

print(IO.supportedSrcs)
IO.read("file")