import requests
import time
from bs4 import BeautifulSoup
import xlwt
from fake_useragent import UserAgent

url_base = "http://211.69.129.116:8501/login.do"
url_second = "http://211.69.129.116:8501/stu/viewresult.do"


def main():
    