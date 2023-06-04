from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls')),
    path("accounts/", include('accounts.urls')),
    path("info/", include('school_teachers.urls')),
    path("search/", include('search.urls')),
]
