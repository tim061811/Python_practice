# if 判斷句

# 1.
# 如果 我肚子餓
#      我就去吃飯
hungry = True
if hungry:
    print("我就去吃飯")


# 2.
# 如果 今天下雨
#      我就開車去上班
# 否則
#      我就走路去上班
rainy = True
if rainy:
    print("我就開車去上班")
else:
    print("我就走路去上班")


# 3.
# 如果 你考100分
#      我給你1000元
# 或是如果 你考80分以上
#      我給你500元
# 或是如果 你考60分以上
#      我給你100元
# 否則
#      你給我300元
score = 100
if score == 100:
    print("我給你1000元")
elif score >= 80:
    print("我給你500元")
elif score >= 60:
    print("我給你100元")
else:
    print("你給我100元")


# 4.
# 如果 你考100分 且 今天下雨
#      我給你1000元
# 否則
#      你給我100元
score = 100
rainy = True
if score == 100 and rainy:
    print("我給你1000元")
else:
    print("你給我100元")


# 5.
# 如果 你考100分 或 今天下雨
#      我給你1000元
# 否則
#      你給我100元
score = 100
rainy = True
if score == 100 or rainy:
    print("我給你1000元")
else:
    print("你給我100元")


# 6.
# 如果 你考100分 或 沒有下雨
#      我給你1000元
# 否則
#      你給我100元
score = 100
rainy = True
if score == 100 or not(rainy):
                  #是不是沒有下雨，如果沒有的話就是Ture，有的話就是False
    print("我給你1000元")
else:
    print("你給我100元")


# 6-1.
# 如果 你沒有考100分 或 今天下雨
#      我給你1000元
# 否則
#      你給我100元
score = 100
rainy = True
if score != 100 or rainy:
  #score這個值是不是不等於100，如果是不等於的話就是Ture，等於的話就是False
    print("我給你1000元")
else:
    print("你給我100元")


# 練習題
# 定義一個函式為 max_number，函式要傳入三個參數三個數字，功能是回傳三個數字那個數字是最大的
def max_number(number1,number2,number3):
    if number1 >= number2 and number1 >= number3:
        return number1
    elif number2 >= number1 and number2 >= number3:
        return number2
    else:
        return number3

print(max_number(1,2,3))

#--------------------------------------------------------

# while 迴圈

i = 1
while i <= 5:
    print(i)
    i += 1 #等於 i = i + 1

print("迴圈結束")


# 練習 猜數字遊戲

gold = 5
guess = None

#因為沒有猜對，所以會一直執行
while guess != gold:
    guess = int(input("輸入數字： "))
    if guess > gold:
        print("小一點")
    elif guess < gold:
        print("大一點")
print("恭喜贏了")


# 練習2 猜數字遊戲(限制遊戲次數，超過3次就輸了)

gold = 5
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False #猜測是否有超過3次，一開始沒有所以是False

while guess != gold and not(out_of_limit):
    # 玩家沒有猜中 且 "沒有"超過3次 才可以繼續猜
    guess_count += 1
    # 玩家遊玩次數
    if guess_count <= guess_limit:
    # 判斷玩家遊玩次數是否超過3次
        guess = int(input("輸入數字： "))
        if guess > gold:
            print("小一點")
        elif guess < gold:
            print("大一點")
    else:
        out_of_limit = True
        # 是否超過3次 = 是

if out_of_limit:
    print("抱歉，你輸了")
else:
    print("恭喜贏了")

# 練習3 數字加總
n = 1
sum = 0 #紀錄累加的結果
while n <= 10:
    sum = sum + n
    n += 1
print(sum)

#------------------------------------------------------------

# for 變數 in 字串or列表:
#     要重複執行的程式碼

for letter in "小白你好": #字串
    print(letter)

for number in [0,1,2,3,4]: #列表
    print(number)

for number in range(4): # range(4) = [0,1,2,3,4]
    print(number)

for number in range(1,5): # range(1,5) = [1,2,3,4]
    print(number)


# 練習1 數字累加
sum = 0
for num in range(11):
    sum = sum + num
print(sum)

# 練習2 數字相乘
# 1,2,3,4,5 = 120
sum = 1
for num in range(1,6):
    sum = sum * num
print(sum)

# 練習3 次方
def poower(base_num,pow_num): #自訂函數
    result = base_num
    for index in range(pow_num):
        result = result * base_num
    return result
print(poower(2,2)) 

#----------------------------------------------

# break
n = 0
while n < 5:
    if n == 3:
        break # Ture直接跳出迴圈，忽略後面的程式碼
    print(n) #印出迴圈中的 n
    n += 1
print("最後的n: " + str(n)) #印出迴圈結束後的 n 

# continue
n = 0
for x in [1,2,3,]:
    if x % 2 == 0: # x是偶數 
        continue # Ture直接進入迴圈，忽略後面的程式碼
    print(x)
    n += 1
print("最後的n:" + str(n))

# else
sum = 0
for n in range(11):
    sum = sum + n
else:
    print(sum) #印出0+1+2+3+...+10 的總和 #結束迴圈前印出n

# 範例：找出整數平方根
# 使用者輸入 9 得到 3
# 輸入 11 得到【沒有】整數的平方根
n = int(input("輸入一個正整數： ")) #字串變整數
for i in range(n+1): # i從 0~n-1
    if i * i == n:
        print("整數平方根：" + str(i))
        break #用break強制結束迴圈時，不會執行else區塊
else:
    print("沒有整數平方根")