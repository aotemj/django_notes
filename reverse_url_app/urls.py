from django.urls import path

from reverse_url_app import views

urlpatterns = [
    path("reverse_first_request/", views.first_request),
    path("articles/<int:year>/", views.year_archive, name="new-year-archive")
]
