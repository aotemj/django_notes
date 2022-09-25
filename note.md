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
