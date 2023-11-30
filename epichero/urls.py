from django.contrib import admin
from django.urls import path, include

from main.urls import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
