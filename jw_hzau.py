import requests
import tesserocr
from bs4 import BeautifulSoup
from PIL import Image

base_url = "http://jw.hzau.edu.cn/"
aspx_url = "http://jw.hzau.edu.cn/ChexkCode.aspx"
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"

header = {
    'User-Agent': ua,
    'Host': "localhost",
    'Accept-Language': "zh-CN,zh;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'Content-Type': "application/x-www-form-urlencoded",
    'Connection': "keep-alive",
}
r = requests.session()


def get_post_data(url_base, url_aspx):
    html = r.get(url_base, headers=header).text
    soup = BeautifulSoup(html, 'html.parser')
    viewState = soup.select('body.login_bg input')[0]['value']
    print(viewState)
    img = r.get(url_aspx, stream=True, headers=header)
    with open("checkcode.gif",'wb') as f:
        f.write(img.content)

    image = Image.open("checkcode.gif")
    image.show()

    user = input("学号")
    pwd = input("密码")
    checkCode = input("验证码")
    post_info = {

        "__VIEWSTATE": viewState,
        "txtUserName": user,
        "Textbox1": "",
        "TextBox2": pwd,
        "txtSecretCode": checkCode,
        "RadioButtonList1": "(unable to decode value)",
        "Button1": "",
        "lbLanguage": "",
        "hidPdrs": "",
        "hidsc": "",
    }


get_post_data(base_url, aspx_url)
