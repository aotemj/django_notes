# Environment

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
