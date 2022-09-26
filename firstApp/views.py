from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


# Create your views here.

def my_first_request(request):
    return HttpResponse("第一个请求")


def login(request):
    print(dir(request))
    return HttpResponse("登录成功")


def get_setting_config(request):
    return HttpResponse(f"当前值为获取 settings 中的 DEBUG 值：${settings.DEBUG}")
