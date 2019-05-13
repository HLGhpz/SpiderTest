import requests
import tesserocr
from bs4 import BeautifulSoup
from PIL import Image
from pprint import pprint
from ZFCheckCode import recognizer

base_url = "http://jw.hzau.edu.cn/"
aspx_url = "http://jw.hzau.edu.cn/CheckCode.aspx"
aspx_default2 = "http://jw.hzau.edu.cn/default2.aspx"
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
link_base = "http://jw.hzau.edu.cn/xskbcx.aspx"
header = {
    'User-Agent': ua,
    'Host': "jw.hzau.edu.cn",
    'Accept-Language': "zh-CN,zh;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'Content-Type': "application/x-www-form-urlencoded",
    'Connection': "keep-alive",
}
xh = input("请输入学号\n>>>")
pprint(xh)
mm = input("请输入密码\n>>>")
r = requests.Session()


def get_viewState():
    html = r.get(base_url, headers=header)
    soup = BeautifulSoup(html.content, 'html.parser')
    viewState = soup.select('body.login_bg input')[0]['value']
    pprint(viewState)
    return viewState


def get_captcha():
    image = r.get(aspx_url, headers=header)
    with open('CheakCode.png', 'wb') as f:
        f.write(image.content)
    image = Image.open("CheakCode.png")
    image.show()
    code = recognizer.recognize_checkcode('CheakCode.png')
    print(code)
    checkcode = input("请输入验证码")
    return checkcode


def get_html(viewState, cheskcode):
    post = {
        "__VIEWSTATE": viewState,
        "txtUserName": xh,
        "Textbox1": "",
        "TextBox2": mm,
        "txtSecretCode": cheskcode,
        "RadioButtonList1": "",
        "Button1": "",
        "lbLanguage": "",
        "hidPdrs": "",
        "hidsc": "",
    }
    html = r.post(aspx_default2, data=post, headers=header)
    soup = BeautifulSoup(html.content, 'html.parser')
    link = "http://jw.hzau.edu.cn/xskbcx.aspx?xh=" + xh
    header_my = {
        'User-Agent': ua,
        'Host': "jw.hzau.edu.cn",
        'Accept-Language': "zh-CN,zh;q=0.8",
        'Accept-Encoding': "gzip, deflate",
        'Content-Type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive",
        'Referer' : link
        # 'Referer':"http://jw.hzau.edu.cn/xskbcx.aspx?xh=2017307211017",
    }
    html = r.get(link, headers = header_my)
    soup = BeautifulSoup(html.content,'html.parser')
    pprint(soup)


def main():
    viewState = get_viewState()
    checkcode = get_captcha()

    get_html(viewState, checkcode)


main()
