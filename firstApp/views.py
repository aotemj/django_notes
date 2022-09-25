from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def my_first_request(request):
    return HttpResponse("第一个请求")
