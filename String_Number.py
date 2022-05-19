#字串、字串的用法
print("Hello Mr.White")

# \n 換行 or """字串"""
print("Hello \nMr.White")
print("""Hello


Mr.White""")

# \後可標示不是字串的結尾，是字串的一部份
print("Hello \"Mr.White")

# 變數搭配字串，可用+號形成字串
name = "Mr.Lai"
num = 8
print("Hello" + name)
print("Hello" , num)

#--------------------------------------

print(77)
# 加減乘除，也可連續運算
print(8+5)
print(8-5)
print(8*5)
print(8/5)
print(8+8*5) #先乘除後加減

# 整數除法 //
print(8//5) #1.3取1

# 取餘數 %
print(8%5) #1.3取3

# 絕對值 abs()

# 次方 pow(2,4) = 2**4 2的4次方

# 開根號 sqrt()

# max(20,30,100...) 取最大值100
# min(20,30,100...) 取最小值20

# 四捨五入 round()
# 無條件捨去 floor()
# 無條件進位 ceil()

# str 數字轉換字串
print("字串" + str(8))
#字串與數字無法相加

# int 字串轉換整數數字
# float 字串轉換成小數點數字