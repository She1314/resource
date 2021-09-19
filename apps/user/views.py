from django.shortcuts import render
import re
import random
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail
from django_redis import get_redis_connection
from django.utils.decorators import method_decorator
# Create your views here.
from utils.verfyUtil import verifyParam
from utils.resRormatUtil import Email
from resource.settings import EMAIL_HOST_USER


class EmailVerificationTest(View):
    DURATION = 3

    @method_decorator(verifyParam('email'))
    def post(self, request):
        email = request.POST['email']

        re_email = r'^(\w+)@(\w+)\.(\w+)'
        if not re.match(re_email, email):
            return Email('PARAM_ERROR').JsonResponse()
        verify_code = random.randint(100000, 999999)


        # 发送邮件
        self.send_email_task(email, verify_code=verify_code, duration=self.DURATION)
        return Email().JsonResponse()

    def send_email_task(self, email, verify_code, duration):
        email_format = {
            'subject': 'sjnmall验证码',
            'message': '',
            'html_message': f'''
                <h3>欢迎注册小俊男商城, 祝您购物愉快！！！</h3>
                <p>您的验证码是：{verify_code}</p>
                <p>注意你的验证码有效时间长度为：{duration}分钟</p>
            ''',
            'from_email': EMAIL_HOST_USER,
            'recipient_list': [email],
        }
        response = send_mail(**email_format)
        return response
