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
workbook = xlwt.Workbook(encoding='utf8')

for i_1 in range(20173042101, 20173042102):
    worksheet = workbook.add_sheet(str(i_1))
    for i_2 in range(1, 33):
        if i_2 < 10:
            num = '0' + str(i_2)
        else:
            num = str(i_2)
        UASER = str(i_1) + num
        print(UASER)
        postData = {
            'username': UASER,
            'password': '888888',
            'btnlogin.x': '42',
            'btnlogin.y': '15'
        }
        sport_session.post(url, data=postData, headers=header)
        res = sport_session.get(url_second, headers=header)
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        info = soup.select('table.fcb tr td.fd')
        j = 0
        for i_need in [0, 1, 2, 3, 5, 8]:
            print(info[i_need].text)
            worksheet.write(i_2, j, info[i_need].text)
            j += 1
        time.sleep(1)

workbook.save('test_1.xls')
