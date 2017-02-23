#__*__coding:utf-8__*__
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders


class Mail:
    """设置邮件的头、尾部、正文附件"""
    def __init__(self):
            self.root = MIMEMultipart()

# 设置打开文件的方法
    def open_file(self,filename):
        f = open(filename)
        return f

#得到所有收件人
    def get_acceptor(self):
        f = self.open_file("to.txt")
        for element in f.readlines():
            s = element.strip("\n").strip(";")
            res = s.split(";")
            for i in res:
                yield i
        f.close()

#获取邮件的内容文本
    def body_context(self):
        f = self.open_file("context.txt")
        content = f.read()
        f.close()
        return content

#设置邮件的正文
    def get_main_text(self):
        message_content = MIMEText(self.body_context(),"plain","utf-8")
        self.root.attach(message_content)

#设置邮件附件
    def get_basement(self):
        f = self.open_file("to.txt")
        files = MIMEBase('application', 'octet-stream')
        files.set_payload(f.read())
        Encoders.encode_base64(files)
        files.add_header('Content-Disposition', 'attachment; filename="to.txt"')
        self.root.attach(files)
        f.close()

#整合邮件所有内容
    def integration(self):
        username = "ywx435658"
        password = "yaofeng-796"
        sender = "yaofengjie@huawei.com"
        server = smtplib.SMTP("mail.huawei.com")
        try:
            server.login(username, password)
        except Exception as e:
            print e
        self.get_main_text()
        self.get_basement()
        for one in self.get_acceptor():
            self.root["From"] = sender
            self.root["To"] = one
            self.root['Subject'] = "来自Python的测试邮件"
            try:
                server.sendmail(sender, one, self.root.as_string())
            except Exception as e:
                print e
            # finally:
            #     with open("Failed_name_list.txt","w+") as f:
            #         f.write(e)
            #         f.write("\n")
        server.close()