from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
# Create your views here.
from utils.verfyUtil import verifyParam


class EmailVerificationTest(View):
    @method_decorator(verifyParam('email'))
    def post(self, request):
        return HttpResponse("测试成功")