from django.urls import path, re_path
from django.views.generic.base import TemplateView
from main.views import main, support, download, news, games

urlpatterns = [
    path('', main, name='home'),
    #path('news/', news, name='news'),
    path('games/', games, name='games'),
    path('support/', support, name='support'),
    path('download/', download),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]
