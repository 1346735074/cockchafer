# 京东金融黄金地址链接
# https://msfirm-gold.jd.com/stock/detail/28190809231854015693_21001001000001.do


def login(username, password, session, headers):
    # 处理登录 ,先用浏览器F12查看他要什么参数
    resp1 = session.get('http://msfirm-gold.jd.com', headers=headers)  # 拿cookie:_xsrf
    _xsrf = resp1.cookies['_xsrf']
    d_c0 = resp1.cookies['d_c0']
    x_udid = d_c0.split("|")[0].lstrip("\"")  # 获取 x_udid
    print('x_udid 为:' + x_udid)

    # 更新请求头，知乎防反爬真的很厉害。
    headers.update({
        "X-Xsrftoken": _xsrf,
        "X-UDID": x_udid,
        "X-ZSE-83": '3_1.1',
        "x-requested-with": "fetch"
    })


if __name__ == "__main__":
    # 设置headers
    headers = {
        # 'User-Agent': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/56.0.2924.87 Mobile Safari/537.36',
        # 'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
        # "Referer": "https://trade.jr.jd.com/centre/financing.action",
        # "Host": "msfirm-gold.jd.com"
    }

    print("开始执行登陆")
