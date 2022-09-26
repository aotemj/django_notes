from firstApp import views
from django.urls import path

urlpatterns = [
    path("login/", views.first_app_login)
]
