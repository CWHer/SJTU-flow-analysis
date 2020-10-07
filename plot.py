import json
import matplotlib.pyplot as plt

# "图书馆主馆", "李政道图书馆", "包玉刚图书馆",
# "徐汇社科馆", "闵行第二餐厅", "闵行第四餐厅",
# "闵行第一餐厅", "闵行第三餐厅", "徐汇第二餐厅",
# "闵行第五餐厅", "闵行第六餐厅", "闵行哈乐餐厅",
# "徐汇研究生餐厅", "闵行第七餐厅", "闵行玉兰苑"
NAME = "图书馆主馆"
with open("log.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

t = []
num = []
for item in data:
    for moment in item:
        t.append(moment)
        num.append(item[moment][NAME])

plt.figure()
plt.plot(num, '-x')
plt.title("flow in main library")
plt.legend(['current', 'capacity'], loc='best')
plt.ylabel("number")
plt.xlabel("time")
plt.show()
