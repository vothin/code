# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 构建附件模块
from email.mime.multipart import MIMEMultipart


send_user = 'as449235763lp@163.com'
send_password = '135315lp1314'
receiver = '85642914@qq.com'

smtp_server = 'smtp.163.com'

# 构建邮件
msg = MIMEMultipart()
# 内容
msg.attach(MIMEText("这是一个带附件的主题内容", 'plain', 'utf-8'))
msg['From'] = Header(send_user)
msg['to'] = Header(receiver)

# 构建附件
att_1= MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
# base64指的是 a-z A-z 0-9 这些基础字符的加减除=的几个进制流编码

# 文件类型
att_1["Content-Type"] = 'application/octet-stream'
att_1["Content-Disposition"] = "attachment;filename = 'text.txt'"  # 附近头部的标识

msg.attach(att_1)
# 附近上传的动作

try:
    # 主题
    msg['Subject'] = '我就是主题呀'

    # 创建邮件发送对象
    server = smtplib.SMTP(smtp_server, 25)

    # 连接邮件服务器
    # server.connect(smtp_server, 25)

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
