from django.urls import path

from reverse_url_app import views

app_name = 'reverse_url'

urlpatterns = [
    path("reverse_first_request/", views.first_request),
    path("articles/<int:year>/", views.year_archive, name="new-year-archive"),
    path('html_render/', views.html_redirect)
]
