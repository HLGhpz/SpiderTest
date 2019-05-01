import requests
import xlwt
from bs4 import BeautifulSoup


def get_news():

    url = "http://news.hzau.edu.cn/"
    header = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    r = requests.get(url, headers=header)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    new = soup.select('ul.txt-list li')
    return (new)


def main():
    # workbook = xlwt.Workbook(encoding='utf8')
    # worksheet = workbook.add_sheet('news')
    news_list = get_news()
    for i in range(len(news_list)):
        herf = news_list[i]
        print(news_list[i])
        # worksheet.write(i, 0, news_list[i].text)
    # workbook.save('new.xls')
    


main()
