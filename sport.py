import requests
import time
from bs4 import BeautifulSoup
import xlwt

url = "http://211.69.129.116:8501/login.do"
url_second = "http://211.69.129.116:8501/stu/viewresult.do"
use_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) " \
            "Chrome/46.0.2490.86 Safari/537.36"

header = {
    'Host': "localhost",
    'Accept-Language': "zh-CN,zh;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'Content-Type': "application/x-www-form-urlencoded",
    'Connection': "keep-alive",
    'User-Agent': use_agent,
}

sport_session = requests.Session()
sport_session.get(url, headers=header)

for i in range(1, 2):
    if i < 10:
        num = '0' + str(i)
    else:
        num = str(i)
    postData = {
        'username': '20173072102' + num,
        'password': '888888',
        'btnlogin.x': '42',
        'btnlogin.y': '15'
    }
    sport_session.post(url, data=postData, headers=header)
    res = sport_session.get(url_second, headers=header)
    html = res.content
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.select('table.fcb tr td.fd')
    for Info in info:
        print(Info.get_text())
    time.sleep(1)
