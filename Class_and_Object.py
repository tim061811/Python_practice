# 類別Class、物件Object
# 假設要定義一個手機(作業系統、型號、是否防水)
class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

Phone1 = Phone("ios",123,True)
print(Phone1.os)
Phone2 = Phone("android",456,False)
print(Phone2.number)

# 延伸
class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

         # 新增判斷手機作業系統是不是ios
    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False
        
        # 新增相加的功能
    def add(self,num1,num2):
        return num1 + num2


Phone1 = Phone("ios",123,True)
print(Phone1.is_ios())
print(Phone1.add(2,4))