from django.urls import path
from . import views

urlpatterns = [
    path("teacher/<int:teacher_id>", views.teacher_info, name="register"),
    path("school/<int:school_id>", views.school_info, name="register")
]
