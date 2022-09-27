from firstApp import views
from django.urls import path, register_converter
from . import conventers

# register custom converter
register_converter(conventers.MyYearConverter, 'yyyy')

urlpatterns = [
    path("login/", views.first_app_login),
    path("article/", views.article_list),
    # dynamic parameter
    path("article/<int:article_id>/", views.article),
    # multiple dynamic parameter
    path("article/<int:article_id>/<str:section_name>/", views.article_section),
    # slug type: word、number and _ -
    path("article/<slug:slug_parameter>/", views.article_search),
    # path type: include /
    path("article/path/<path:path>/", views.article_path),
    # str type: not include /
    path("article/<str:str>/", views.article_str),
    # uuid type
    path("article/<uuid:uuid>", views.article_uuid),
    #     use the custom converter
    path("<yyyy:year>", views.custom_year_converter)
]
