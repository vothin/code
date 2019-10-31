# -*- coding: UTF-8 -*-

'''
一、python对SMTP的支持

SMTP（Simple Mail Transfer Protocol）是简单传输协议，它是一组用于用于由源地址到目的地址的邮件传输规则。

python中对SMTP进行了简单的封装，可以发送纯文本邮件、HTML邮件以及带附件的邮件。

1、python对SMTP的支持

①email模块：负责构建邮件
②smtplib模块：负责发送邮件


2、sendmail()方法的使用说明

①connect(host,port)方法参数说明

  host:指定连接的邮箱服务器

  port:指定连接的服务器端口

②login(user,password)方法参数说明

  user:登录邮箱用户名

  password:登录邮箱密码

③sendmail(from-addr,to_addrs,msg...)方法参数说明

  from_addr:邮件发送者地址

  to_addrs:字符串列表，邮件发送地址

  msg:发送消息

④quit()：结束当前会话

注意：因为采用的是SMTP协议，那么需要确保自己的发送优邮箱地址开启了SMTP服务，否则，会报错
password需要输入邮箱授权码，而非邮箱登录密码！！！
password需要输入邮箱授权码，而非邮箱登录密码！！！
password需要输入邮箱授权码，而非邮箱登录密码！！！ 重要的事情说三次

接收的邮件，将对方的地址设为白名单，否则只能在垃圾箱里面找
'''

# coding=utf-8
import smtplib
from email.mime.text import MIMEText  # txt
from email.header import Header  # 头部

# 账号,授权码
send_user = 'sbssqvfb@163.com'
send_password = 'a1234567'

# 接收地址
receiver = '85642914@qq.com'

# 服务器地址
smtp_server = 'smtp.163.com'

# 构建邮件

# 内容 plain代表txt类型信息
msg = MIMEText("这是我要发送的内容--TS", 'plain', 'utf-8')
msg['From'] = Header(send_user)
msg['to'] = Header(receiver)


try:
    # 主题
    msg['Subject'] = '我就是主题呀'

    # 创建邮件发送对象
    server = smtplib.SMTP()

    # 连接邮件服务器
    server.connect(smtp_server, 25)

    # 登陆到服务器
    server.login(send_user, send_password)

    # 发送邮件
    server.sendmail(send_user, receiver, msg.as_string())

    # 断开连接
    server.quit()

    print("邮件发送成功！")

except smtplib.SMTPException as error_sender:
    # 断开连接
    server.quit()
    print("邮件发送失败", error_sender)


