#_*_ coding:utf-8 _*_

from random import Random
from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from Mxonline.settings import EMAIL_FROM


def send_reister_email(email,send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type=='register':
        email_title = u"慕学在线网注册激活链接"
        email_body = u"请点击下面的连接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass
    elif send_type=='forget':
        email_title = u"慕学在线网密码重置链接"
        email_body = u"请点击下面的连接重置你的账号：http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str

