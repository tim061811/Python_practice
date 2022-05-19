# 函式定義
def hello():         #函式名字
    print("hello")   #函式輸出

# 函式呼叫
hello()

# 範例
def hello(name,age):
    print("hello" + name + "你今年" + age + "歲")   
hello("政廷","87") #字串與數字無法相加，故87用字串

# 延伸
def hello(name,age):
    print("hello" + name + "你今年" + str(age) + "歲")   
hello("政廷",87) #字串與數字無法相加，故用str()將數字轉換成字串

# 練習
def add(number1,number2):
    print(number1 + number2)
add(1,2)

# return 回傳值
def add(number1,number2):
    print(number1 + number2)
    return 10    
value = add(1,2) #相加為3
print(value)     #return 10回傳後覆蓋原先的變數value，故輸出為10

# 延伸
def add(number1,number2):
    print(number1 + number2)
                 #return None，若函式沒有輸入return，系統會預設為None
value = add(1,2) #相加為3
print(value)     #因沒有輸入return，故None預設輸出None

# 延伸2
def add(number1,number2):
    print(number1 + number2)
    return 10
    print("你好") #當函式遇到return，系統就會直接結束，不會再繼續運行下面的程式   
value = add(1,2) 
print(value)

# 函式可用來做程式的包裝:同樣的邏輯可以重複利用
def calculate(max):
    sum = 0
    for n in range(1,max+1):
        sum = sum + n
    print(sum)

#------------------------------------------------------------

# 參數的預設資料
# 次方
def power(base_num,pow_num=0):
                   #預設值=0
    print(base_num**pow_num)

power(3,2)
power(4)    #沒輸入參數，預設值=0
 
# 使用參數名稱對應
# 除法
def divid(n1,n2):
    print(n1/n2)

divid(2,4)
divid(n2=2,n1=4)

# 無限/不定 參數資料
# 平均數
def avg(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print(sum/len(num))

avg(3,4)
avg(3,5,10) 
avg(1,4,-1,-8)

# 預設加總函式 sum()
score = [88,90,76]
print(sum(score))

# 排序函式 sorted()
print(sorted(score))

# .lower() 字串變小寫 .upper() 字串變大寫
# .islower() 確認是否為小寫 .isupper() 確認是否為大寫
# print(字串+ .lower())
phrase = "Hello Mr.Lai"
print(phrase.lower())
#函式可疊加
phrase = "Hello Mr.Lai"
print(phrase.lower().islower())

#[]中括號用法 字串後加上[數字] 裡面輸入數字 意指字串第一個位置是誰
phrase = "Hello Mr.Lai"
         #012345678...
print(phrase[0])

# .replace(替換,被替換) 替換字串中的文字
phrase = "Hello Mr.Lai"
print(phrase.replace("a","A"))