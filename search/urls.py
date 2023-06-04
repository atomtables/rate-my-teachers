from django.urls import path
from . import views

urlpatterns = [
    path("<str:query>/", views.search_query, name="register"),
]
