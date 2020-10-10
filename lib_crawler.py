import requests
import json
import re
import time


class LibCrawler():
    def __init__(self):
        self.__url = "http://zgrstj.lib.sjtu.edu.cn/cp?callback=CountPerson&_=1602036327221"
        self.__error_msg = "get library's flow data fail\n"

    def __write_fail_log(self, text):
        with open("fail_log.txt", "a+") as f:
            f.write(text)

    # t_now is a string of current time
    def get(self, t_now):
        log = {}
        for _ in range(5):
            try:
                response = requests.get(self.__url, timeout=4)
                if response.status_code == 200:
                    self.content = json.loads(
                        re.findall('{.*}', response.text, re.S)[0])
                    for lib in self.content['numbers']:
                        log.update(
                            {lib['areaName']: (lib['inCounter'], lib['max'])})
                    return log

            except Exception as e:
                print(e)
                time.sleep(0.05)
                
        self.__write_fail_log(t_now + '  ' + self.__error_msg)
        return None
