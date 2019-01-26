import requests
import re
import user_agent
from pyquery import PyQuery
import time



class IpChi():
    def __init__(self):
        self.headers = {"User_Agent": user_agent.generate_user_agent()}
        self.proxies = {"http": "82.117.247.134:49561"}
        self.list = []
        self.get_url = "https: // www.kuaidaili.com / free / inha / {} /"

    def ip_one(self, num):  # 爬取第一页的IP
        respons = requests.get(self.get_url.format(num), headers=self.headers, proxies=self.proxies)
        html = respons.content.decode()
        doc = PyQuery(html)
        catalog = doc("#list > table > tbody > tr > td").text()
        ip = re.findall(r'\d*\.\d*\.\d*\.\d*\s\d*', catalog)
        for i in ip:
            n = re.sub(r'\s', ":", i)
            proxy = {"http": i}
            self.yanzheng(proxy, n)
            # print(n, type(n))
            print(self.list)

    def yanzheng(self, proxy, n):  # 对ip进行有效性核对
        try:
            ip_respons = requests.get(url="https://www.baidu.com", headers=self.headers, proxies=proxy, timeout=5)
            time.sleep(5)
            respons = ip_respons.status_code
            if respons == 200:
                self.list.append(n)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def sure(self):
        i = 0
        while True:
            i += 1
            TRue_respons = requests.get(self.get_url.format(i), headers=self.headers, proxies=self.proxies)
            if TRue_respons.status_code == 200:
                self.ip_one(num=i)
            else:
                break


if __name__ == '__main__':
    m = IpChi()
    m.sure()







