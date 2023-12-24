from django.urls import path, re_path
from django.views.generic.base import TemplateView
from main.views import main, support, download, news, games
from django.conf.urls import handler400, handler403, handler404, handler500

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

handler404 = 'main.views.custom_page_not_found_view'
handler500 = 'main.views.custom_error_view'
handler403 = 'main.views.custom_permission_denied_view'
handler400 = 'main.views.custom_bad_request_view'