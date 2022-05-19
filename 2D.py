# 2維列表、巢狀迴圈
# row = 行
# column = 列

nums = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [9]
]

# 取值
print(nums[0][2]) #[行][列] #從0開始

for row in nums:
    for col in row:
        print(col)


