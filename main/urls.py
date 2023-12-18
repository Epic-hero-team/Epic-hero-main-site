from django.urls import path, re_path
from django.views.generic.base import TemplateView
from main.views import main, support, download, news, games

urlpatterns = [
    path('', main),
    path('news/', news),
    path('games/', games),
    path('support/', support),
    path('download/', download),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]
