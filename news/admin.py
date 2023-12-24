from django.contrib import admin
from news.models import Post # наша модель из blog/models.py

admin.site.register(Post)