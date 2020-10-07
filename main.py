from lib_crawler import LibCrawler
from canteen_crawler import CanteenCrawler
import time
import json

L = LibCrawler()
C = CanteenCrawler()
while True:
    t_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    data_now = {}
    log_now = {}

    data = L.get(t_now)
    if data != None:
        data_now.update(data)
    data = C.get(t_now)
    if data != None:
        data_now.update(data)
    log_now[t_now] = data_now

    with open("log.json", "a+", encoding="utf-8") as f:
        f.write(json.dumps(log_now, ensure_ascii=False) + ',\n')
    time.sleep(5)
