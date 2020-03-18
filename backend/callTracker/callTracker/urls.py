from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('callApp/', include('callApp.urls')),
    path('admin/', admin.site.urls),
]