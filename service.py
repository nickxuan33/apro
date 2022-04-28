from data import urls

import requests
import re
import random
from PyQt5.QtCore import QThread, pyqtSignal


ua_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        ]



class SendUrlsThread(QThread):
    progress_signal = pyqtSignal(int,int,str)

    def __init__(self,domain):
        super(SendUrlsThread,self).__init__()
        self.domain = domain

    def run(self):
        total = len(urls)
        print(total,self.domain)
        i = 0
        for url in urls:
            pcount = len(re.findall('{}',url))
            args = [self.domain for i in range(pcount)]
            url = url.format(*args)
            self.send(url)
            i = i + 1
            current = int(i/total * 100)
            if current == 100:
                url = '完成'
            self.progress_signal.emit(current, i, url)


    def send(self,url):
        try:
            user_agent = random.choice(ua_list)
            headers = {'User-Agent': user_agent}
            res = requests.get(url, headers=headers , timeout=3, verify=False)
            if res.status_code == 200:
                return True
        except Exception as e:
            print(e)
