# 網路連線
# 載入模組 urllib.request
# import urllib.request as request

# 下載特定網址資料
# import urllib.request as request
# with request.urlopen(網址) as response:
#   data = response.read()
# print(data)

# 讀取台大首頁資料
# import urllib.request as request
# src = "https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#    data = response.read().decode("utf-8") # 取得臺灣大學網站的原始碼(HTML.CSS.JSON)
# print(data)


# -------------------------------------------------------

# 串接、擷取公開資料
# 台北市公開資料抓取範例
import urllib.request as request
import json

# 台北市公開資料內湖科技廠商資料API
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"

with request.urlopen(src) as response:
    data = json.load(response)  # 利用 json 模組處理 json資料格式

# 將公司名稱列表出來
clist = data["result"]["results"]
for company in clist:
    print(company["公司名稱"]+"\n")


# 篩選資料輸出資料
clist = data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")
