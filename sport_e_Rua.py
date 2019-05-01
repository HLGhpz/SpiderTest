import requests
import time
from bs4 import BeautifulSoup
import xlwt
from fake_useragent import UserAgent

url_base = "http://211.69.129.116:8501/login.do"
url_second = "http://211.69.129.116:8501/stu/viewresult.do"

def get_session(url,header):
    sport_session = requests.Session()
    sport_session.get(url_base,header=header)

def get_html(url,header):
    sport_session.post(
        url,
        data = postData,
        headers = header,
    )
    res = sport_session.get(url_second)
