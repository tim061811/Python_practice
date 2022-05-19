# 模組的引用
import practice_tool
# 模組的使用 模組名稱.變數 or .函式()
print(practice_tool.max_number(2,3,8))

import numpy as np #模組改名


# 使用Python內建模組
import sys
print(sys.platform)
print(sys.maxsize)

import sys as s
print(s.platform)
print(s.maxsize)


# 建立 geometry 模組，載入使用
import geometry
result = geometry.distanece(1,1,5,5)
print(result)
result = geometry.slop(1,2,5,6)
print(result)


# 調整搜尋模組的路徑
import sys
sys.path.append("資料夾") # 在模組的搜尋路徑列表中【新增路徑】
print(sys.path) #印出模組的搜尋路徑