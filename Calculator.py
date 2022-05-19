# 建立基本計算機

# input(字串) 提示用戶應該做甚麼
# 提示用戶輸入名字後，系統會放到變數name
name = input("請輸入你的名字： ")
# 輸入互動後輸出下列
print("哈囉" + name)

# 範例練習
name = input("請輸入你的名字： ")
age = input("請輸入你的年紀： ")
print("哈囉" + name + "你今年" + age + "歲")

# int() 字串轉換成整數
# float() 字串轉換成小數點的數字

# --------------------------------------------------

# 建立一個計算機

number1 = float(input("請輸入第一個數： "))
# input會預設所有輸入的都當成字串，故用float使其轉換成有小數點的數字
operator = input("請輸入運算符號： ")
# 運算符號為字串
number2 = float(input("請輸入第二個數： "))

# 判斷用戶輸入的運算符號
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("不支援的運算")
