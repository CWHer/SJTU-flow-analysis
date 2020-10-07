import requests
import re
import json
import time


class CanteenCrawler():
    def __init__(self):
        self.__url = "https://canteen.sjtu.edu.cn/CARD/Ajax/Place"
        self.__error_msg = "get canteen's flow data fail\n"

    def __write_fail_log(self, text):
        with open("fail_log.txt", "a+") as f:
            f.write(text)

    # t_now is a string of current time
    def get(self, t_now):
        log = {}
        for _ in range(5):
            response = requests.get(self.__url, timeout=4)
            if response.status_code == 200:
                self.content = json.loads(response.text)
                for canteen in self.content:
                    log.update({
                        canteen['Name']: (canteen['Seat_u'], canteen['Seat_s'])
                    })
                return log
            time.sleep(0.05)
        self.__write_fail_log(t_now + '  ' + self.__error_msg)
        return None
