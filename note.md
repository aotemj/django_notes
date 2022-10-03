pass# Environment

## python version: 3.8.*

## django version: 3.2.5

### install django

```bash
  # install with the latest version
  pip install django
  # install with the custom version
  pip install django==3.2.5 
```

# Project Manage

## create project:

```bash
    django-admin startprject projectName
```

## start project:

```bash
  # start with the default port
  python manage.py runserver   
  # start with the custom port
  python manage.py runserver 8002 
  # or 
  python manage.py runserver 127.0.0.1:8002 
```

## create app

```bash
    python manage.py startapp appName
```

## import all the app urls by using keyword "include"

```python
# step1 create urls.py in the app
# firstApp/urls.py
from firstApp import views
from django.urls import path

urlpatterns = [
    path("login/", views.first_app_login)
]

# step2 add firstApp to the project settings
# django_project01/settings.py
...
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstApp'  # add firstApp to the project
]
...
# step3 import the firstApp urls to the project urls
# django_project01/urls.py
from django.contrib import admin
from django.urls import path, include
from firstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("first_request/", views.my_first_request),
    path("login/", views.login),
    path("get_settings_config/", views.get_setting_config),
    path("first_app/", include("firstApp.urls"))  # import all app urls with keyword "include"
]
# step4 visit the app url by using browser, notice that the app name should be added to the front url
# visit app url: http://localhost:8000/first_app/login/ 
# visit project url: http://localhost:8000/login/ 

```

### generate a uuid

```python
import uuid

print(uuid.uuid1())
```

### custom converter

```python
# step1 create a converter file to define the custom converter
# firstApp/converter.py
class MyYearConverter(object):
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value


# step2 register the custom converter in the urls.py
# firstApp/urls.py
from django.urls import path, register_converter
from . import conventers

# register custom converter
# "yyyy" is the sign of the custom converter 
register_converter(conventers.MyYearConverter, 'yyyy')

# step3 then define the urlpatterns 
# firstApp/urls.py
#     use the custom converter
from firstApp import views

urlpatterns = [
    # ...
    #  the sign yyyy should be equals with the custom converter definition
    path("<yyyy:year>", views.custom_year_converter)
    #     ...
]

# step3 then define the views 
# firstApp/views.py
from django.http import HttpResponse


def custom_year_converter(request, year):
    return HttpResponse(f"This is a example of the custom converter, the year is:{year}")

```

### error handler

```python
# step1 modify the project settings.py
# django_project01/settings.py

debug: False

ALLOWED_HOSTS = ["*"]

# step2 create a page_not_found handler in the app views.py
# firstApp/views.py
from django.http import HttpResponse


def page_not_found(request, exception):
    return HttpResponse(exception)


# step3 import the handler in the project urls.py
from firstApp import views

handler404 = 'firstApp.views.page_not_found'

```

### divide urlpatterns into many small modules

* method 1

```python
#   step 1: generate a sub urlpatterns :
#   firstApp/urls.py
from firstApp import views
from django.urls import path, include

submodule_patterns = [
    path("blog", views.blog),
    path("blog/<int:num>", views.blog),
]
#   step 2:
#   include submodule_patterns into the urlpatterns:

urlpatterns = [
    # ... other patterns
    path('', include(submodule_patterns))
]
```

* method 2 combine the urlpatterns which has the same prefix

```python
from firstApp import views
from django.urls import path, register_converter, re_path, include

#  before divide
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

#  after divide:

path('article/', include([
    path("", views.article_list),
    path("<int:article_id>/", views.article),
    path("<int:article_id>/<str:section_name>/", views.article_section),
    path("<slug:slug_parameter>/", views.article_search),
    path("path/<path:path>/", views.article_path),
    path("<str:str>/", views.article_str),
    path("<uuid:uuid>", views.article_uuid),
]))
```

### url redirect

```python
# step1: define the view that user will visited directly
#  reverse_url_app/views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def first_request(request):
    return HttpResponseRedirect(reverse("new-year-archive", args=(
        2222)))  # this name('new-year-archive') must equals with the name defined in the urlpatterns


# step2: then define the view which will be visited via first_request indirectly
#  reverse_url_app/views.py
def year_archive(request, year):
    return HttpResponse(f"year-archive:year:{year}")


# step3: define the urls:
# reverse_url_app/urls.py
from django.urls import path

from reverse_url_app import views

urlpatterns = [
    path("reverse_first_request/", views.first_request),
    path("articles/<int:year>/", views.year_archive, name="new-year-archive")
    # this name('new-year-archive') must equals with the name defined in the views
]

```

### html redirect

* step1 creat a template html int the sub app template directory

```html
<!-- path: reverse_url_app/templates/redirect.html -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<a href="{% url 'new-year-archive' 2004 %}">url redirect test</a>
</body>
</html>
```

* step2 define the html redirect view in the sub app views and define the redirect view

```python
# path: reverse_url_app/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def html_redirect(request):
    return render(request, "redirect.html")


def year_archive(request, year):
    return HttpResponse(f"year-archive:year:{year}")
```
