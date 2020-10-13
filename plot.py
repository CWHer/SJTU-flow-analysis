import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.dates import AutoDateLocator, DateFormatter
import numpy as np
import time

NAME_SET = [
    "图书馆主馆", "李政道图书馆", "包玉刚图书馆", "徐汇社科馆", "闵行第二餐厅", "闵行第四餐厅", "闵行第一餐厅",
    "闵行第三餐厅", "徐汇第二餐厅", "闵行第五餐厅", "闵行第六餐厅", "闵行哈乐餐厅", "徐汇研究生餐厅", "闵行第七餐厅",
    "闵行玉兰苑"
]
NAME = NAME_SET[4]
print(NAME)
week = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

plt.figure()
# plt.title(NAME)
plt.ylabel("number of people")
plt.xlabel("time in a day")
ax = plt.gca()
# ticker_spacing = 3600
# ax.xaxis.set_major_locator(ticker.MultipleLocator(ticker_spacing))
plt.xticks([i * 3600 for i in range(25)], [str(i) + ":00" for i in range(25)],
           rotation=45)

for day in week:
    with open(day + '.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(day)
    num = [[0, 0]]
    t = [0]
    for item in data:
        for moment in item:
            date = time.strptime(moment, "%Y-%m-%d %H:%M:%S")
            t.append(date.tm_hour * 3600 + date.tm_min * 60 + date.tm_sec)
            num.append(item[moment].get(NAME, num[-1]))

    num = np.array(num)
    plt.plot(t, num[:, 0])

plt.legend(week, loc='best')
plt.show()
