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


def first_app_login(request):
    return HttpResponse("This is a example that import urls from the app")


def article_list(request):
    return HttpResponse("This is a example of fetch the article list")


def article(request, article_id):
    return HttpResponse(
        f"This is a example of fetch the specific article by articleId, current articleId is : {article_id}")


def article_section(request, article_id, section_name):
    return HttpResponse(
        f"This is a example of dynamic multiple parameter: first parameter is article_id:{article_id}, second parameter is section_name: {section_name}")


def article_search(request, slug_parameter):
    return HttpResponse(
        f"This is a example of the slug parameter, a slug parameter means the parameter contains 'number' 、'word'、'-' 、'_',and the slug parameter is : {slug_parameter}")


def article_path(request, path):
    return HttpResponse(f"This is a example of the path type, the path is: {path}")


def article_str(request, str):
    return HttpResponse(f"This is a example of the str type, the str is: {str}")


def article_uuid(request, uuid):
    return HttpResponse(f"This is a example of the uuid, the uuid is:{uuid}")


def custom_year_converter(request, year):
    return HttpResponse(f"This is a example of the custom converter, the year is:{year}")
