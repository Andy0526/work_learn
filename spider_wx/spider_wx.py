#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import cookielib
import urllib

import urllib2

# 设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
# 创建一个请求，原理同urllib2的urlopen
params = {
    "Host": "mp.weixin.qq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
data = urllib.urlencode(params)
url = "http://mp.weixin.qq.com/mp/getmasssendmsg?__biz=MzA4MjEyNTA5Mw==&uin=&key=NQhdsgfxyYyS_J6NH7fuyu8hUfbDJhbJqDblADWlqleZXf8L_4-mFxxmxZSK_2fiAADDEkHdtfqnGsZB6T6zz4IDAAA~&f=json&frommsgid=1000000266&count=10&uin=&key=NQhdsgfxyYyS_J6NH7fuyu8hUfbDJhbJqDblADWlqleZXf8L_4-mFxxmxZSK_2fiAADDEkHdtfqnGsZB6T6zz4IDAAA~&pass_ticket=&wxtoken=&x5=0&f=json"
url += '?' + data
request = urllib2.Request(url)
response = opener.open(request)

print response.read()
