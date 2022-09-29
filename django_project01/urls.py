"""django_project01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from firstApp import views

handler404 = 'firstApp.views.page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("first_request/", views.my_first_request),
    path("login/", views.login),
    path("get_settings_config/", views.get_setting_config),
    path("first_app/", include("firstApp.urls"))  # import all app urls with keyword "include"
]
