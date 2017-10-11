#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:lewsan

import logging
import os
import smtplib
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(send_to, title, content, files=None, mail_user='yunwei@peiwo.cn', mail_password='Peiwo123'):
    mail_server = 'smtp.mxhichina.com'
    # mail_port = 25
    mail_port = 465

    # connect
    # server = smtplib.SMTP()
    server = smtplib.SMTP_SSL()
    server.connect(mail_server, mail_port)
    server.login(mail_user, mail_password)

    msg = MIMEMultipart()
    msg['Subject'] = title
    msg['From'] = mail_user
    msg['To'] = ','.join(send_to)
    msg["Accept-Language"] = "zh-CN"
    msg["Accept-Charset"] = "ISO-8859-1,utf-8"

    html = MIMEText(content, 'html', 'utf-8')
    msg.attach(html)

    try:
        if files:
            for filename in files:
                att = MIMEText(file(filename, 'rb').read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                att["Content-Disposition"] = 'attachment; filename="%s"' % os.path.basename(filename)
                msg.attach(att)

        server.sendmail(mail_user, send_to, msg.as_string())
    except:
        logging.error(traceback.format_exc())
