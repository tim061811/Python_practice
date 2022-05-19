# 定義類別，在透過類別建立實體物件
# 先建立實體物件，才能使用實體屬性

# 建立實體語法
# class 類別名稱:
    # 定義初始化函式
#     def __init__(self):
#         透過操作 self 來定義實體屬性
# 建立實體物件，放入變數 obj 中
# obj = 類別名稱() # 呼叫初始化函式

# 範例1-1
class Point:
    def __init__(self):
        self.x = 3
        self.y = 4
# 建立實體物件
# 此實體物件包含 x 和 y 兩個實體屬性
p = Point()

# 範例1-2
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
# 建立實體物件
# 建立時，可直接傳入參數資料
p = Point(1,5)


# 使用實體語法
# 實體物件.實體屬性名稱

# 範例2-1
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
# 建立實體物件，並取得實體屬性資料
p = Point(1,5)
print(p.x + p.y)

# 範例1-1
# Point 實體物件的設計，平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
# 建立第一個實體物件
p1 = Point(3,4)
print(p1.x,p1.y)
# 建立第二個實體物件
p2 = Point(5,6)
print(p2.x,p2.y)

# 範例1-2
# FullName 實體物件的設計: 分開紀錄姓、名資料的全名
class FullName:
    def __init__(self,first,last):
        self.first = first
        self.last = last
name1 = FullName("tim","lai")
name2 = FullName("mumu","lin")

print(name1.first, name1.last)

# -------------------------------------------------

# 實體屬性 - 封裝在實體物件中的變數
# 實體方法 - 封裝在實體物件中的函式

# class 類別名稱:
      # 定義初始化函式
#     def __init__(self):
#         定義實體屬性(封裝在實體物件中的變數)
      # 定義實體方法/函式
#     def 方法名稱(self,更多自訂參數):
#         方法主體，透過 self 操作實體物件
# 建立實體物件，放入變數 obj 中
# obj = 類別名稱() # 呼叫初始化函式

# 使用方法語法
# 實體物件.實體方法名稱(參數資料)

# 範例2-1
# Point 實體物件的設計，平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    # 定義實體方法
    def show(self):
        print(self.x,self.y)
    def distance(self, targetX, targetY):
        return(((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
p = Point(3,4) # 建立實體物件
p.show() # 呼叫實體方法/函式
result = p.distance(0,0) # 計算座標 3,4 和座標 0,0 之間的距離
print(result)

# 範例2-2
# File 實體物件的設計：包裝檔案讀取的程式
class File:
    # 初始化函式
    def __init__(self, file_name):
        self.file_name = file_name # 欲打開的檔案名稱
        self.file = None # 尚未開啟檔案：初期是 None
    # 定義實體方法
    def open(self): 
        self.file = open(self.file_name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
# 讀取第一個檔案
file1 = File("123.txt")
file1.open()
data = file1.read()
print(data)
# 讀取第二個檔案
file2 = File("num.txt")
file2.open()
data = file2.read()
print(data)