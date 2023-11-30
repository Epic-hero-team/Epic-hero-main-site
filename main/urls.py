from django.urls import path, re_path
from django.views.generic.base import TemplateView
from main.views import main, about, help, download

urlpatterns = [
    path('', main),
    path('about/', about),
    path('help/', help),
    path('download/', download),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]
