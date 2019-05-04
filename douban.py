import re
import requests
import time


def get_idcode(session, login_url, head, data):
    try:
        htmls = session.get(login_url, headers = head).text 
        captcha_img = re.findall(img_pattern, htmls)[0]
        captcha_id = re.findall(id_pattern, htmls)[0]

        with open('idcode.jpg','wb') as f:
            captcha_img = session.get(captcha_img)
            f.write(captcha_img.content)
        captcha_id = input('输入验证码')
        data['captcha-solution'] = captcha
        data['captcha-id'] = captcha_id
    except Exception as e:
