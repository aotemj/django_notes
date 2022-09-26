from firstApp import views
from django.urls import path

urlpatterns = [
    path("login/", views.first_app_login),
    path("article/", views.article_list),
    # dynamic parameter
    path("article/<int:article_id>/", views.article),
    # multiple dynamic parameter
    path("article/<int:article_id>/<str:section_name>", views.article_section),
    # slug type: word、number and _ -
    path("article/<slug:slug_parameter>", views.article_search)
]
