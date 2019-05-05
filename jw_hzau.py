import requests
import tesserocr
from bs4 import BeautifulSoup
from PIL import Image



base_url = "http://jw.hzau.edu.cn/"
aspx_url = "http://jw.hzau.edu.cn/CheckCode.aspx"
aspx_default2 = "http://jw.hzau.edu.cn/default2.aspx"
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


def get_post_data(url_base, url_aspx, aspx_2):
    html = r.get(url_base, headers=header).text
    soup = BeautifulSoup(html, 'html.parser')
    viewState = soup.select('body.login_bg input')[0]['value']
    print(viewState)
    img = r.get(url_aspx, stream=True, headers=header)
    with open("checkcode.png", 'wb') as f:
        f.write(img.content)

    image = Image.open("checkcode.png")
    image.show()
    print(tesserocr.image_to_text(image))

    checkCode = input("验证码")
    # user = input("学号")
    # pwd = input("密码")
    user = "2017307211017"
    pwd = "2017kshzkjdx"
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
    html_main = r.post(aspx_2, data=post_info, headers=header).text
    soup_main = BeautifulSoup(html_main, 'html.parser')
    post_xk = {
        "xh" : user,
        "xm" : "jkj".encode('gb2312'),
        "gnmkdm" : "N121603"
            }
    url_kb = "http://jw.hzau.edu.cn/xskbcx.aspx"
    html_kb = r.get(url_kb,params=post_xk,headers= header)
    soup_kb = BeautifulSoup(html_kb.content,'html.parser')
    print(soup_kb)


get_post_data(base_url, aspx_url, aspx_default2)
